"""
Naam:            Thijmen Batelaan
UvAID:           15198235
Beschrijving:    Afgeleide berekenen met numpy functies.

"""

# Imports...
import numpy as np
import matplotlib.pyplot as plt

# Voel je vrij om meer functies toe te voegen als je dat wilt.


def plot_signals(t, signals, opdracht_naam):
    """
    Plot signals onder elkaar in een plot met een bepaalde titel
    t: tijd array
    signals: array van arrays met daarin de signals
    opdracht_naam: titel van de graph
    """
    num_signals = len(signals)
    fig, axs = plt.subplots(num_signals, 1, figsize=(10, 2 * num_signals), sharex=True)

    if num_signals == 1:
        axs = [axs]

    for i, (name, signal) in enumerate(signals):
        axs[i].plot(t[: len(signal)], signal) # :len(signal) voor differentie signaal die korter is.
        axs[i].set_ylabel(f"{name}")
        axs[i].grid(True)

    axs[-1].set_xlabel("Time") # zet alleen bij de onderste graph een x as
    plt.suptitle(opdracht_naam)
    plt.show()


if __name__ == "__main__":
    # De opdracht bestaat uit vier deelopdrachten.
    # 1.
    #

    t = np.linspace(0, 2 * np.pi, 25)
    t_h = t[1] - t[0]
    sinus_signaal = ("Normale Sinus", np.sin(t))
    d_sinus_signaal = ("Voorwaarts gedifferentie sinus", np.diff(sinus_signaal[1]) / t_h)

    signals = [sinus_signaal, d_sinus_signaal]

    plot_signals(t, signals, "Opdracht 1")

    # 2.
    def opdracht2(t_2, sin, opdrachtnaam): # in een functie voor makkelijke herhaling in 4
        t_h_2 =  (t_2[1] - t_2[0])
        centrale_diff = (
            "Centrale differentie",
            np.convolve(sin[1], [1, 0, -1], mode="same") / (t_h_2 * 2),
        )
        kruiscorrelatie = (
            "Kruiscorrelatie",
            np.correlate(sin[1], [-1, 0, 1], mode="same") / (t_h_2 * 2),
        )
        signals = [
            ("Voorwaarts gedifferentie sinus", np.diff(sin[1]) / t_h_2),
            centrale_diff,
            kruiscorrelatie,
        ]
        plot_signals(t_2, signals, opdrachtnaam)

    opdracht2(t, sinus_signaal, "Opdracht 2")

    # 3.
    centrale_diff_roll = (
        "Centrale differentie (roll)",
        (np.roll(sinus_signaal[1], -1) - np.roll(sinus_signaal[1], 1))
        / (2 * (t[1] - t[0])),
    )
    signals = [
        ("Voorwaarts gedifferentie sinus", np.diff(sinus_signaal[1]) / t_h),
        centrale_diff_roll,
    ]
    plot_signals(t, signals, "Opdracht 3")

    # 4.
    for points in [101, 1001, 1000001]:
        t = np.linspace(0, 2 * np.pi, points)
        sinus_signaal = ("Normale Sinus", np.sin(t))
        opdracht2(t, sinus_signaal, f"Opdracht 4 met {points} punten")

    # Beantwoord de volgende vraag in commentaar (zie SOWISO):
    # Verbeteren de benaderingen als je meer punten op het interval neemt?
    # De benadering vebeterd een klein beetje aan het begin, alleen het begin is nog stijl door
    # dat de eerste sample te laag is.
