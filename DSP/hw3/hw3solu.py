# plotting the frequency response
import numpy as np
import matplotlib.pyplot as plt

wh = np.linspace(0,np.pi,1000)
H = 2*np.cos(wh) + 2
plt.figure()
plt.title('total frequency response')
plt.subplot(211)
plt.plot(wh,H)
plt.xlabel('normalized radian frequency')
plt.ylabel('magnitude response')
plt.subplot(212)
plt.plot(wh,-wh)
plt.xlabel('normalized radian frequency')
plt.ylabel('phase response')
plt.show()
