import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 2*np.cos(2*np.pi*t)+2015
t1= np.arange(0.0, 15, 0.6)
plt.figure(2)
plt.plot(t1, 2*np.cos(2*np.pi*t)+2015,'pg')
plt.title('Coseno')
plt.savefig('Coseno.png')
plt.show()

