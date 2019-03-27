# first ready some data
import numpy as np
import matplotlib.pyplot as plt

L = 7
w = np.linspace(0, 2*np.pi, 400)
y = (np.sin(L*w/2))/(L*np.sin(w/2))

fig, ax = plt.subplots()
print(fig)
print(ax)
ax.set_title('Simple Plot')
plt.plot(w,y)
plt.show()

# creates four polar axes, access theme thru returned array
fig, axes = plt.subplots(2,2, subplot_kw=dict(polar=True))
axes[0,0].plot(w,y)
axes[0,0].set_title('line')
axes[1,1].scatter(w,y)
axes[1,1].set_title('scatter')
plt.show()
