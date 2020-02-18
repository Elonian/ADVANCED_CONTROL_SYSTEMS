from scipy import signal
import matplotlib.pyplot as plt
import control
from control import tf

system = signal.lti([2,1], [1,0.75,2,1]) # Arrange the numerator cofficients in first array and denominator coefficients in second array 
r = range(0, 10000)  # range of W (rad/sec)
w, mag, phase = signal.bode(system, w=r)
plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, mag)    # Bode magnitude plot
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, phase)  # Bode phase plot
plt.ylabel("[degrees]")
plt.xlabel("[rad/s]")
plt.show()



