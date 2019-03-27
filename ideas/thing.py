import matplotlib.pyplot as plt
import numpy as np
import mpld3

# one thing i want to do is be able to see 'pedro martinez'
# and also what point his era is that im looking at right now

f, ax = plt.subplots()
x1 = np.array([0,100], int)
x2 = np.array([10,110], int)
y = np.array([0,100], int)

line = ax.plot(x1, y)
mpld3.plugins.connect(f, mpld3.plugins.LineLabelTooltip(line[0], label='label 1'))

line = ax.plot(x2, y)
mpld3.plugins.connect(f, mpld3.plugins.LineLabelTooltip(line[0], label='label 2'))

mpld3.show()
