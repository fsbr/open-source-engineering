# first ready some data
import numpy as np
import matplotlib.pyplot as plt
import mpld3
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
fig, axes = plt.subplots(2,2)
axes[0,0].set_title('line')
axes[0,0].projection='polar'
axes[0,0].plot(w,y)
axes[1,1].scatter(w,y)
axes[1,1].projection='rectilinear'
axes[1,1].set_title('scatter')
axes[1,1].set_xlabel('units')
plt.show()

print(axes[0,0])

# what i want is a 2x2 suplot


# okay just declare each as a separate thing
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,4, projection='polar')
ax1.projection='polar'
line = ax1.plot(w,y)
ax2.scatter(w,y)
ax2.projection='rectilinear'
ax2.set_title('scatter')
ax2.set_xlabel('units')
mpld3.plugins.connect(fig,mpld3.plugins.LineLabelTooltip(line[0],label='label 1'))
mpld3.show()
