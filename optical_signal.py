import numpy as np

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
