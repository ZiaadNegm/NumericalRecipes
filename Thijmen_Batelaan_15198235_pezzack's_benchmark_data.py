'''
Naam:			...
UvAID:			...
Beschrijving:	...

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, wiener
# ...

# Voel je vrij om meer functies toe te voegen als je dat wilt.

def centrale_differentie(tijd, hoek):
    dt = tijd[1] - tijd[0]
    a_numeriek = np.zeros_like(hoek)
    for i in range(1, len(hoek) - 1):
        a_numeriek[i] = (hoek[i + 1] - 2 * hoek[i] + hoek[i - 1]) / (dt**2)
    return a_numeriek

def savitzky_golay(tijd, hoek):
    h = tijd[1] - tijd[0]
    a_numeriek = savgol_filter(hoek, window_length=5, polyorder=2, deriv=2, delta=h)
    return a_numeriek

def wiener_filter(tijd, hoek):
    dt = tijd[1] - tijd[0]
    hoek_filtered = wiener(hoek)
    a_numeriek = np.zeros_like(hoek_filtered)
    for i in range(1, len(hoek_filtered) - 1):
        a_numeriek[i] = (hoek_filtered[i + 1] - 2 * hoek_filtered[i] + hoek_filtered[i - 1]) / (dt**2)
    return a_numeriek

if __name__ == "__main__":

	tijd, hoek, hoek2, a_analoog = np.loadtxt('Pezzack.txt', skiprows=6, unpack=True)
	# a_numeriek = centrale_differentie(tijd, hoek)
	# a_numeriek = savitzky_golay(tijd, hoek)
	a_numeriek = wiener_filter(tijd, hoek)
	plt.figure(figsize=(11,4))
	plt.suptitle("Pezzack's benchmark data", fontsize=20)
	plt.subplot(1,2,1)
	plt.plot(tijd, hoek, 'b-')
	plt.xlabel('tijd (s)', fontsize=12)
	plt.ylabel('hoek (rad)', fontsize=12)
	plt.subplot(1,2,2)
	plt.plot(tijd, a_analoog, 'g-')
	plt.plot(tijd, a_numeriek, 'r--', label='Numeriek')
	plt.xlabel('tijd (s)')
	plt.ylabel('versnelling (rad/s$^2$)', fontsize=12)
	plt.subplots_adjust(wspace=0.3)
	plt.show()
 
 
	


	# ...