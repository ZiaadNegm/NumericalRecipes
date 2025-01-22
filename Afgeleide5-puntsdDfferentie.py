"""
Naam: Ziaad Negmel-Din, Thijmen Batelaan
UvAID: 15260925, 15198235
Beschrijving: Dit is de opdracht 'Afgeleide via 5-punts differentie' 
We benaderen de afgeleide van een sinusfunctie op het interval (0,2pi)
en verdelen dit interval in verschillende aantallen punten
"""

import numpy as np
import matplotlib.pyplot as plt


def estimatedDifferentiationKernel(y, h):
    """
    Bereken de afgeleide van y met behulp van de centrale 5-punts differentieformule via kruiscorrelatie.
    """
    kernel = np.array([-1, 8, 0, -8, 1]) / (12 * h)
    return np.convolve(y, kernel, mode="same")


def estimatedDifferentiationRoll(y, h):
    """
    Bereken de afgeleide van y met behulp van de centrale 5-punts differentieformule via numpy.roll.
    """
    y_m2 = np.roll(y, -2)
    y_m1 = np.roll(y, -1)
    y_p1 = np.roll(y, 1)
    y_p2 = np.roll(y, 2)
    return (-y_m2 + 8 * y_m1 - 8 * y_p1 + y_p2) / (12 * h)


def executeAndPlot(num_points_list):
    for num_points in num_points_list:
        # Stap 1: Interval en punten verdelen
        interval = [0, 2 * np.pi]
        equalDistancePoints = np.linspace(interval[0], interval[1], num=num_points)
        y = np.sin(equalDistancePoints)

        # Stap 2: Bereken stapgrootte
        h = equalDistancePoints[1] - equalDistancePoints[0]

        # Stap 3: Benader de afgeleide met de centrale 5-punts formule
        derivative_kernel = estimatedDifferentiationKernel(y, h)
        derivative_roll = estimatedDifferentiationRoll(y, h)

        # Stap 4: Plot de originele functie en de benaderde afgeleide
        plt.figure(figsize=(12, 6))
        plt.plot(
            equalDistancePoints,
            y,
            label="sin(x)",
            marker="o",
            linestyle="-",
            markersize=4,
        )
        plt.plot(
            equalDistancePoints,
            derivative_kernel,
            label="Afgeleide (kruiscorrelatie)",
            marker="x",
            linestyle="--",
        )
        plt.plot(
            equalDistancePoints,
            derivative_roll,
            label="Afgeleide (numpy.roll)",
            marker="+",
            linestyle=":",
        )
        plt.title(f"Afgeleide van sin(x) met {num_points} punten")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    # Uitvoeren met verschillende aantallen punten
    num_points_list = [25, 101, 1001, 1000001]
    executeAndPlot(num_points_list)
