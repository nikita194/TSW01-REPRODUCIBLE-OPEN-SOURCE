import numpy as np
import matplotlib.pyplot as plt
from src.opticaldisp.waveforms import (
    generate_gaussian,
    generate_lorentzian,
    generate_sech,
    generate_square,
)
from src.opticaldisp.optical_signals import OpticalSignal
from src.opticaldisp.dispersion import apply_dispersion

if __name__ == "__main__":
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
    plt.plot(t * 1e12, np.abs(pulse_g.et), label="Gaussian")
    plt.plot(t * 1e12, np.abs(pulse_l.et), label="Lorentzian")
    plt.plot(t * 1e12, np.abs(pulse_s.et), label="Hyp. sech")
    plt.plot(t * 1e12, np.abs(pulse_sq.et), label="Square")
    plt.title("Amplitude")
    plt.xlabel("Time (ps)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(t * 1e12, pulse_g.pt, label="Gaussian")
    plt.plot(t * 1e12, pulse_l.pt, label="Lorentzian")
    plt.plot(t * 1e12, pulse_s.pt, label="Hyp. sech")
    plt.plot(t * 1e12, pulse_sq.pt, label="Square")
    plt.title("Power")
    plt.xlabel("Time (ps)")
    plt.ylabel("Power")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./amplitude_power.png")

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

        gvec[i, :] = dpulse_g.pt
        lvec[i, :] = dpulse_l.pt
        svec[i, :] = dpulse_s.pt
        sqvec[i, :] = dpulse_sq.pt

    # Waterfall Plots
    fig = plt.figure(figsize=(10, 8))
    for data, title in zip(
        [gvec, lvec, svec, sqvec], ["Gaussian", "Lorentzian", "Sech", "Square"]
    ):
        ax = fig.add_subplot(
            2,
            2,
            list(["Gaussian", "Lorentzian", "Sech", "Square"]).index(title) + 1,
            projection="3d",
        )
        X, Y = np.meshgrid(t * 1e12, CDvec)
        ax.plot_surface(X, Y, data, cmap="viridis")
        ax.set_xlabel("Time (ps)")
        ax.set_ylabel("Chromatic Dispersion (ps/nm)")
        ax.set_zlabel("Power")
        ax.set_title(title)
    plt.tight_layout()

    plt.savefig("./waterfall.png")
