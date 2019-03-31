# making a PD controller from the example in NISE

import control as c
import numpy as np
import matplotlib.pyplot as plt

# make the transfer function

G = c.tf([1],[1,7,0])
print(G)
Gcl = c.feedback(G)
t,yout = c.step_response(Gcl)


# so we plot the open loop system
r = c.root_locus(G) 
print(r[1])
#plt.subplot(2,1,1)
#plt.plot(t,yout)
#plt.subplot(2,1,2)
#plt.plot(np.real(A),np.imag(A))
#plt.show()
