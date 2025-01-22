"""
Naam: Ziaad Negmel-Din, Thijmen Batelaan
UvAID: 15260925, 15198235
Beschrijving: Dit is de opdracht 'Berekenen van een eerste afgeleide' 
We benaderen de afgeleide van een sinusfunctie op het interval (0,2pi)
"""

import numpy as np
import matplotlib.pyplot as plt


def forward_difference(y, h):
    """
    Bereken de eerste afgeleide met voorwaartse differentie.
    """
    return np.diff(y) / h


def central_difference_kernel(y, h):
    """
    Bereken de eerste afgeleide met centrale differentie via kruiscorrelatie.
    """
    kernel = np.array([-1, 0, 1]) / (2 * h)
    return np.convolve(y, kernel, mode="same")


def central_difference_roll(y, h):
    """
    Bereken de eerste afgeleide met centrale differentie via numpy.roll.
    """
    y_m1 = np.roll(y, -1)
    y_p1 = np.roll(y, 1)
    return (y_p1 - y_m1) / (2 * h)


def executeAndPlot(num_points_list):
    for num_points in num_points_list:
        # interval en punten eerlijk verdelen
        interval = [0, 2 * np.pi]
        equalDistancePoints = np.linspace(interval[0], interval[1], num=num_points)
        y = np.sin(equalDistancePoints)

        # De stapgrootte berekenen
        h = equalDistancePoints[1] - equalDistancePoints[0]

        # voorwaarste afgeleide
        derivative_forward = forward_difference(y, h)

        # Centrale differentie via kernel
        derivative_central_kernel = central_difference_kernel(y, h)

        # Centrale differentie via roll
        derivative_central_roll = central_difference_roll(y, h)

        # Plots
        plt.figure(figsize=(12, 6))
        plt.plot(
            equalDistancePoints[:-1],
            derivative_forward,
            label="Afgeleide (voorwaartse)",
            linestyle="--",
            marker="o",
        )
        plt.plot(
            equalDistancePoints,
            derivative_central_kernel,
            label="Afgeleide (centrale - kernel)",
            linestyle="-",
            marker="x",
        )
        plt.plot(
            equalDistancePoints,
            derivative_central_roll,
            label="Afgeleide (centrale - roll)",
            linestyle=":",
            marker="+",
        )
        plt.title(f"Eerste afgeleide van sin(x) met {num_points} punten")
        plt.xlabel("x")
        plt.ylabel("y'")
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    num_points_list = [25, 101, 1001, 1000001]
    executeAndPlot(num_points_list)
