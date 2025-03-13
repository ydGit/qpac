import numpy as np
import matplotlib.pyplot as plt
import os


def Ek_GN(v):
    return np.power(v, 2)/2


def Ek_SR(v):
    return 1/np.sqrt(1-np.power(v, 2)) - 1



if __name__ == "__main__":
    v = np.linspace(0, 0.5, 200)
    ek_gn = Ek_GN(v)
    ek_sr = Ek_SR(v)

    fsize = [8, 5]
    plt.figure(figsize=fsize)
    plt.plot(v, ek_gn, 'r-', alpha=0.6, linewidth=2, label="GN")
    plt.plot(v, ek_sr, 'b--', alpha=0.6, linewidth=2, label="SR")

    plt.xlabel("v/c")
    plt.ylabel("Ek/Mc^2")
    plt.grid(1)
    plt.legend(loc="upper left")

    fname_base = "KineticEnergyCompare"

    fname_svg = os.path.join(".", "..", "pics", fname_base + ".svg")
    plt.savefig(fname_svg, format="svg")

    fname_pdf = os.path.join(".", "..", "pics", fname_base + ".pdf")
    plt.savefig(fname_pdf, format="pdf")
    # plt.show()
