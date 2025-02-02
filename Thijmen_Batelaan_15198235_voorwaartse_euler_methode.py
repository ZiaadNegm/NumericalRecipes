"""
Naam:			Thijmen Batelaan; Ziaad Negmel-Din
UvAID:			15198235; 15260925
Beschrijving:	De voorwaarste euler methode

"""

# Imports...
import numpy as np
import matplotlib.pyplot as plt

def Euler(phi, t0, t1, y0, n):
    #  phi is de functie bij de GDV dy/dt = phi(t,y)
    #  beginwaare y(t0) = y0
    #  tijdinterval is [t0, t1]
    # n is het aantal stappen in de Euler metode
    # t is de numpy array van tijdstippen
    # y is de numpy array van berekende functiewaarden
    t = np.array([t0])
    y = np.array([y0])

    dt = (t1 - t0) / n

    for _ in range(0, n):
        t2 = t[-1] + dt
        t = np.append(t, t2)
        y_nieuw = y[-1] + phi(t2, y[-1]) * dt
        y = np.append(y, y_nieuw)

    return t, y


def Heun(phi, t0, t1, y0, n):
    #  phi is de functie bij de GDV dy/dt = phi(t,y)
    #  beginwaare y(t0) = y0
    #  tijdinterval is [t0, t1]
    # n is het aantal stappen in de Euler metode
    # t is de numpy array van tijdstippen
    # y is de numpy array van berekende functiewaarden
    t = np.array([t0])
    y = np.array([y0])

    dt = (t1 - t0) / n

    for _ in range(n):
        t_huidig = t[-1]
        y_huidig = y[-1]

        y_gok = y_huidig + phi(t_huidig, y_huidig) * dt

        t_volgende = t_huidig + dt
        y_volgende = (
            y_huidig + 0.5 * (phi(t_huidig, y_huidig) + phi(t_volgende, y_gok)) * dt
        )

        t = np.append(t, t_volgende)
        y = np.append(y, y_volgende)

    return t, y


# Voel je vrij om meer functies toe te voegen als je dat wilt.

if __name__ == "__main__":
    dy = lambda t, y: y
    y1 = lambda t: 8 * np.e**t
    y2 = lambda t: -(3*np.e**(t +1 )) /(1-np.e**(t + 1))

    t, y = Euler(dy, -1, 1, 0.25,  100)
    t2, y2 = Euler(dy, 0, 5, 8,  50)
    t3, y3 = Heun(dy,-1, 1, 0.25,  100)
    t4, y4 = Heun(dy, 0, 5, 8,  50)

    # plt.plot(t, y, label='Euler y(-1) = 0.25')
    plt.plot(t4, y1(t4), label="y(t)", linestyle="-.")
    # plt.plot(t3, y3, label='Heun y(-1) = 0.25')
    plt.plot(t2, y2, label='Euler y(-1) = 2.5')
    plt.plot(t4, y4, label='Heun y(-1) = 2.5', linestyle="--")

    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title('dy/dt = y, y(0) = 8, n = 50')
    plt.show()
