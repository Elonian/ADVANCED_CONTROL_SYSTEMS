from scipy import signal
import matplotlib.pyplot as plt
import control
from control import tf

system = signal.lti([100,100], [1,110,1000])
r = range(0, 10000)
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
print(system)


