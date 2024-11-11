import numpy as np
from scipy.constants import c  # Speed of light

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

