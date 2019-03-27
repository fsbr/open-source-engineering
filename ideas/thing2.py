# i want these mfing tool tips

import matplotlib.pyplot as plt
import numpy as np
import mpld3

fig, ax = plt.subplots(subplot_kw=dict(axisbg='#FFA71A'))
N = 100

scatter = ax.scatter(np.random.normal(size=N),
                    np.random.normal(size=N),
                    c=np.random.random(size=N),
                    s=1000*np.random.random(size=N),
                    alpha=0.3,
                    cmap=plt.cm.jet)

ax.grid(color='white', linestyle='solid')
ax.set_title('scatter plot (with tooltip!)',size=20)
theLabels = ['point {0}'.format(i +1) for i in range(N)]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=theLabels)
mpld3.plugins.connect(fig,tooltip)
mpld3.show()
