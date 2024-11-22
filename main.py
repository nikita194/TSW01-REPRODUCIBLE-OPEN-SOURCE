import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c  # Speed of light

def generate_gaussian(t, pulsewidth):
    """
    Generates a Gaussian waveform.

    Parameters:
    t (array-like): Input array representing time values.
    pulsewidth (float): The width of the pulse.

    Returns:
    np.ndarray: Gaussian waveform.
    """
    # Calculate tau based on the pulse width
    tau = pulsewidth / (2 * np.sqrt(np.log(2)))
    # Compute the Gaussian waveform
    gaussian = np.exp(-t**2 / (2 * tau**2))
    return gaussian

def generate_square(t, pulsewidth):
    """
    Generates a square waveform.

    Parameters:
    t (array-like): Input array representing time values.
    pulsewidth (float): The width of the pulse.

    Returns:
    np.ndarray: Square wave with values 1 within pulsewidth and 0 outside.
    """
    # Initialize the square wave array with ones
    square = np.ones_like(t)
    # Set values to 0 where abs(t) is greater than pulsewidth / 2
    square[np.abs(t) > pulsewidth / 2] = 0
    return square


def generate_lorentzian(t, pulsewidth):
    """
    Generates a Lorentzian waveform.

    Parameters:
    t (array-like): Input array representing time values.
    pulsewidth (float): The width of the pulse.

    Returns:
    np.ndarray: Lorentzian waveform.
    """
    # Calculate tau based on the pulse width
    tau = pulsewidth / 1.287
    # Compute the Lorentzian waveform
    lorentz = 1 / (1 + (t / tau) ** 2)
    return lorentz


def generate_sech(t, pulsewidth):
    """
    Generates a hyperbolic secant (sech) waveform.

    Parameters:
    t (array-like): Input array representing time values.
    pulsewidth (float): The width of the pulse.

    Returns:
    np.ndarray: Sech waveform.
    """
    # Calculate tau based on the pulse width
    tau = pulsewidth / 1.7627
    # Compute the sech waveform
    sechpulse = 1 / np.cosh(t / tau)
    return sechpulse

class OpticalSignal:
    def __init__(self, wavelength, ts, Et):
        """
        Initialize the OpticalSignal class.

        Parameters:
        wavelength (float): Wavelength of the optical signal in nanometers.
        ts (float): Sampling period in seconds.
        Et (array-like): Complex amplitude envelope of the signal in time.
        """
        self.wavelength = wavelength
        self.ts = ts
        self.Et = np.array(Et, dtype=complex)

    @property
    def Pt(self):
        """Power of the signal in time."""
        return np.abs(self.Et) ** 2

    @property
    def meanpower(self):
        """Mean power of the signal."""
        return np.mean(np.abs(self.Et) ** 2)

    @property
    def N(self):
        """Number of samples in each polarization."""
        return self.Et.size

    @property
    def frequency(self):
        """Signal frequency based on the wavelength."""
        c = 299792485  # Speed of light in m/s
        return c / self.wavelength

def apply_dispersion(SigIn, CD):
    """
    Applies chromatic dispersion to an input optical signal.

    Parameters:
    SigIn (OpticalSignal): Input signal object with attributes `Et`, `wavelength`, and `ts`.
    CD (float): Dispersion coefficient in ps/nm.

    Returns:
    OpticalSignal: Output signal with dispersion applied.
    """
    # Copy the input signal to the output
    SigOut = SigIn
    N = SigIn.Et.size

    # Conversion from D to beta_2
    beta2L = -SigIn.wavelength**2 / (2 * np.pi * c) * (CD * 1e-12 / 1e-9)

    # Frequency vector in the Fourier domain
    Omega = 2 * np.pi / (N * SigIn.ts) * np.concatenate((np.arange(0, N//2), np.arange(-N//2, 0)))

    # Dispersion operator in the frequency domain
    DD = 1j / 2 * beta2L * Omega**2

    # Apply dispersion in the frequency domain
    SigOut.Et = np.fft.ifft(SigIn.Et)
    SigOut.Et = np.exp(DD) * SigOut.Et
    SigOut.Et = np.fft.fft(SigOut.Et)

    return SigOut


if __name__ == '__main__':
    # Set up parameters
    pulsewidth = 1e-12  # ns
    sampleperiod = pulsewidth / 64
    numsamples = 2**12
    samplerate = 1 / sampleperiod
    wavelength = 1550e-9  # meters

    # Time vector centered around zero
    t = (np.arange(1, numsamples + 1) * sampleperiod) - numsamples * sampleperiod / 2
    CDvec = np.arange(0, 2.5, 0.5)  # ps/nm

    # Generate pulses in time
    gauss = generate_gaussian(t, pulsewidth)
    lorentz = generate_lorentzian(t, pulsewidth)
    sech = generate_sech(t, pulsewidth)
    square = generate_square(t, pulsewidth)

    # Create pulse objects
    pulse_g = OpticalSignal(wavelength, sampleperiod, gauss)
    pulse_l = OpticalSignal(wavelength, sampleperiod, lorentz)
    pulse_s = OpticalSignal(wavelength, sampleperiod, sech)
    pulse_sq = OpticalSignal(wavelength, sampleperiod, square)

    # Plot Amplitude and Power
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t * 1e12, np.abs(pulse_g.Et), label='Gaussian')
    plt.plot(t * 1e12, np.abs(pulse_l.Et), label='Lorentzian')
    plt.plot(t * 1e12, np.abs(pulse_s.Et), label='Hyp. sech')
    plt.plot(t * 1e12, np.abs(pulse_sq.Et), label='Square')
    plt.title('Amplitude')
    plt.xlabel('Time (ps)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(t * 1e12, pulse_g.Pt, label='Gaussian')
    plt.plot(t * 1e12, pulse_l.Pt, label='Lorentzian')
    plt.plot(t * 1e12, pulse_s.Pt, label='Hyp. sech')
    plt.plot(t * 1e12, pulse_sq.Pt, label='Square')
    plt.title('Power')
    plt.xlabel('Time (ps)')
    plt.ylabel('Power')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./amplitude_power.png')


    # Dispersion Application Loop
    gvec = np.zeros((len(CDvec), numsamples))
    lvec = np.zeros((len(CDvec), numsamples))
    svec = np.zeros((len(CDvec), numsamples))
    sqvec = np.zeros((len(CDvec), numsamples))

    for i, CD in enumerate(CDvec):
        dpulse_g = apply_dispersion(pulse_g, CD)
        dpulse_l = apply_dispersion(pulse_l, CD)
        dpulse_s = apply_dispersion(pulse_s, CD)
        dpulse_sq = apply_dispersion(pulse_sq, CD)
        
        gvec[i, :] = dpulse_g.Pt
        lvec[i, :] = dpulse_l.Pt
        svec[i, :] = dpulse_s.Pt
        sqvec[i, :] = dpulse_sq.Pt


    # Waterfall Plots
    fig = plt.figure(figsize=(10, 8))
    for data, title in zip([gvec, lvec, svec, sqvec], ['Gaussian', 'Lorentzian', 'Sech', 'Square']):
        ax = fig.add_subplot(2, 2, list(['Gaussian', 'Lorentzian', 'Sech', 'Square']).index(title) + 1, projection='3d')
        X, Y = np.meshgrid(t * 1e12, CDvec)
        ax.plot_surface(X, Y, data, cmap="viridis")
        ax.set_xlabel('Time (ps)')
        ax.set_ylabel('Chromatic Dispersion (ps/nm)')
        ax.set_zlabel('Power')
        ax.set_title(title)
    plt.tight_layout()

    plt.savefig('./waterfall.png')
