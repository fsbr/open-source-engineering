import matplotlib.pyplot as plt
import numpy as np
from mpldatacursor import datacursor

data = np.outer(range(10),range(1,5))
fig,ax = plt.subplots()
lines = ax.plot(data)
ax.set_title('click somewhere on a line')

datacursor(lines)
plt.show()
