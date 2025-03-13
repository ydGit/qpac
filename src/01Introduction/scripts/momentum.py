import numpy as np
import matplotlib.pyplot as plt
import os


def P_GN(v):
    return v


def P_SR(v):
    return v/np.sqrt(1-np.power(v, 2))



if __name__ == "__main__":
    v = np.linspace(0, 0.5, 200)
    p_gn = P_GN(v)
    p_sr = P_SR(v)

    fsize = [8, 4]
    plt.figure(figsize=fsize)
    plt.plot(v, p_gn, 'r-', alpha=0.6, linewidth=2, label="GN")
    plt.plot(v, p_sr, 'b--', alpha=0.6, linewidth=2, label="SR")

    plt.xlabel("v/c")
    plt.ylabel("P/Mc")
    plt.grid(1)
    plt.legend(loc="upper left")

    fname_base = "MomentumCompare"

    fname_svg = os.path.join(".", "..", "pics", fname_base + ".svg")
    plt.savefig(fname_svg, format="svg")

    fname_pdf = os.path.join(".", "..", "pics", fname_base + ".pdf")
    plt.savefig(fname_pdf, format="pdf")
    # plt.show()
