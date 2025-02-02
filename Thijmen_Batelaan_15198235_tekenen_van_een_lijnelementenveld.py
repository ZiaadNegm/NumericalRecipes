"""
Naam:			Thijmen Batelaan, Ziaad
UvAID:			15198235, 
Beschrijving:	Tekenen van een lijnelementenveld voor de differentiaalvergelijking dy/dt = 1 - 2ty
"""

# Imports...
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Voel je vrij om meer functies toe te voegen als je dat wilt.
def opdracht1():
    "Voert opdracht 1 uit"
    t_min, t_max = 0, 2
    y_min, y_max = 0, 2
    lijn_lengte = 0.05

    t = np.linspace(t_min, t_max, 10)
    y = np.linspace(y_min, y_max, 10)
    t_grid, y_grid = np.meshgrid(t, y)

    dydt = 1 - 2 * t_grid * y_grid

    # Berekenen van richting en amplitude van de lijnen
    magnitude = np.sqrt(1 + dydt**2)
    dx = (lijn_lengte / 2) * (1 / magnitude)
    dy_line = (lijn_lengte / 2) * (dydt / magnitude)

    # Grid maken met start en eind van alle lijnen
    t_start = t_grid - dx
    y_start = y_grid - dy_line
    t_end = t_grid + dx
    y_end = y_grid + dy_line

    # Alle lijnen tekenen op de juiste plek
    _, ax = plt.subplots(figsize=(8, 8))
    for i in range(t_grid.shape[0]):
        for j in range(t_grid.shape[1]):
            line = Line2D(
                [t_start[i, j], t_end[i, j]],
                [y_start[i, j], y_end[i, j]],
                color="blue",
            )
            ax.add_line(line)

    ax.set_xlim(t_min - 0.1, t_max + 0.1)
    ax.set_ylim(y_min  -0.1, y_max + 0.1)

    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.axhline(y=0, color='black', linewidth=0.3)
    ax.axvline(x=0, color='black', linewidth=0.3)
    ax.set_title("Lijnelementenveld voor dy/dt = 1 - 2ty")

    plt.show()


def opdracht2():
    "Voert opdracht 2 uit"
    aantal_lijnen = 2000
    t_min, t_max = 0, 2
    y_min, y_max = 0, 2
    lijn_lengte = 0.1

    t = np.random.uniform(t_min, t_max, aantal_lijnen)
    y = np.random.uniform(y_min, y_max, aantal_lijnen)

    dydt = 1 - 2 * t * y

    # Berekenen van richting en amplitude van de lijnen
    magnitude = np.sqrt(1 + dydt**2)
    dx = (lijn_lengte / 2) * (1 / magnitude)
    dy_line = (lijn_lengte / 2) * (dydt / magnitude)

    # Arrays maken met start en eind van alle lijnen
    t_start = t - dx
    y_start = y - dy_line
    t_end = t + dx
    y_end = y + dy_line

    _, ax = plt.subplots(figsize=(8, 8))

    # Tekenen van alle gegenereerde lijnen
    for i in range(aantal_lijnen):
        line = Line2D(
            [t_start[i], t_end[i]], [y_start[i], y_end[i]], color="blue"
        )
        ax.add_line(line)

    ax.set_xlim(t_min - 0.1, t_max + 0.1)
    ax.set_ylim(y_min - 0.1, y_max + 0.1)

    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.axhline(y=0, color='black', linewidth=0.3)
    ax.axvline(x=0, color='black', linewidth=0.3)
    ax.set_title("Lijnelementenveld voor dy/dt = 1 - 2ty")

    plt.show()


if __name__ == "__main__":
    opdracht1()
    opdracht2()
