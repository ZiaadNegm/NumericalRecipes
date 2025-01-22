"""
Naam:			Thijmen Batelaan
UvAID:			15198235
Beschrijving:	Nummerieke afgeleide met ruis met 31 en 101 punten

"""

# Imports...
import numpy as np
import matplotlib.pyplot as plt


def diff1(x, h):
    differentie_array = np.array([1, -8, 0, 8, -1]) / (12 * h)
    return np.convolve(x, differentie_array, mode="valid")


def diff2(x, h):
    differentie_array = np.array([-1, 16, -30, 16, -1]) / (12 * h**2)
    return np.convolve(x, differentie_array, mode="valid")


t = np.linspace(-1, 1, 31)
h = t[1] - t[0]


def f(x):
    return x**2


def teken_grafieken(t, f_afgeleide, f_dubbel_afgeleide):
    plt.figure(figsize=(10, 6))
    plt.plot(t, f(t), label="f(x) = x^2", color="blue")
    plt.plot(t[2:-2], f_afgeleide, label="f'(x) numeriek", color="red")
    plt.plot(t[2:-2], f_dubbel_afgeleide, label="f''(x) numeriek", color="green")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Numerieke afgeleiden van verstoorde data")
    plt.show()


if __name__ == "__main__":
    # De opdracht bestaat uit vier deelopdrachten.
    # 1.
    # ...
    # 2.
    np.random.seed(0)
    functie_met_ruis = f(t) + np.random.uniform(-0.001, 0.001, t.shape)
    f_afgeleide = diff1(functie_met_ruis, h)
    f_dubbel_afgeleide = diff2(functie_met_ruis, h)
    teken_grafieken(t, f_afgeleide, f_dubbel_afgeleide)
    # 3.
    t = np.linspace(-1, 1, 101)
    h = t[1] - t[0]
    functie_met_ruis = f(t) + np.random.uniform(-0.001, 0.001, t.shape)
    f_afgeleide = diff1(functie_met_ruis, h)
    f_dubbel_afgeleide = diff2(functie_met_ruis, h)
    teken_grafieken(t, f_afgeleide, f_dubbel_afgeleide)
