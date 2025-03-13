import numpy as np
import matplotlib.pyplot as plt
import os


def P_GN(v):
    return v


def P_SR(v):
    return v/np.sqrt(1-np.power(v, 2))



if __name__ == "__main__":
    log_scale = True

    fsize = [8, 8]
    # plt.figure(figsize=fsize)
    plt.subplots(4, 1, figsize=fsize)

    # wavelengths
    s_min = -12 if log_scale else 1e-15
    s_max = 12 if log_scale else 1e26

    h_min = 2 if log_scale else 400
    h_max = 3 if log_scale else 700

    plt.subplot(4, 1, 1)
    plt.hlines(0, h_min, h_max, color='r', alpha=0.6, linewidth=2)
    plt.xlim([s_min, s_max])
    plt.ylim([-0.1, 0.1])
    plt.xlabel("Wavelength (nm)")
    plt.grid(1)


    # size
    s_min = -15 if log_scale else 1e-15
    s_max = 26 if log_scale else 1e26

    h_min = -4 if log_scale else 1e-4
    h_max = 4 if log_scale else 1e4

    plt.subplot(4, 1, 2)
    plt.hlines(0, h_min, h_max, color='b', alpha=0.6, linewidth=2)
    plt.xlim([s_min, s_max])
    plt.ylim([-0.1, 0.1])
    plt.xlabel("Size (m)")
    plt.grid(1)

    # time
    s_min = -13 if log_scale else 1e-15
    s_max = 19 if log_scale else 1e26

    h_min = -1 if log_scale else 1e-4
    h_max = 9 if log_scale else 1e4

    plt.subplot(4, 1, 3)
    plt.hlines(0, h_min, h_max, color='g', alpha=0.6, linewidth=2)
    plt.xlim([s_min, s_max])
    plt.ylim([-0.1, 0.1])
    plt.xlabel("Time (s)")
    plt.grid(1)

    # speed
    s_min = -40 if log_scale else 1e-15
    s_max = 8 if log_scale else 1e26

    h_min = -40 if log_scale else 1e-4
    h_max = 2 if log_scale else 1e4

    plt.subplot(4, 1, 4)
    plt.hlines(0, h_min, h_max, color='m', alpha=0.6, linewidth=2)
    plt.xlim([s_min, s_max])
    plt.ylim([-0.1, 0.1])
    plt.xlabel("Speed (m/s)")
    plt.grid(1)


    fname_base = "RangeOfExp"

    fname_svg = os.path.join(".", "..", "pics", fname_base + ".svg")
    plt.savefig(fname_svg, format="svg")

    fname_pdf = os.path.join(".", "..", "pics", fname_base + ".pdf")
    plt.tight_layout()
    plt.savefig(fname_pdf, format="pdf")
    plt.show()
