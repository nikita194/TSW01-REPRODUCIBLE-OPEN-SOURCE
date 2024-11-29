import numpy as np
from scipy.constants import c  # Speed of light


def apply_dispersion(sigin, cd):
    """
    Applies chromatic dispersion to an input optical signal.

    Parameters:
    SigIn (OpticalSignal): Input signal object with attributes `Et`, `wavelength`,
    and `ts`.
    CD (float): Dispersion coefficient in ps/nm.

    Returns:
    OpticalSignal: Output signal with dispersion applied.
    """
    # Copy the input signal to the output
    sigout = sigin
    n = sigin.et.size

    # Conversion from D to beta_2
    beta2l = -(sigin.wavelength**2) / (2 * np.pi * c) * (cd * 1e-12 / 1e-9)

    # Frequency vector in the Fourier domain
    omega = (
        2
        * np.pi
        / (n * sigin.ts)
        * np.concatenate((np.arange(0, n // 2), np.arange(-n // 2, 0)))
    )

    # Dispersion operator in the frequency domain
    dd = 1j / 2 * beta2l * omega**2

    # Apply dispersion in the frequency domain
    sigout.Et = np.fft.ifft(sigin.et)
    sigout.Et = np.exp(dd) * sigout.et
    sigout.Et = np.fft.fft(sigout.et)

    return sigout
