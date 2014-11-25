profiles2patch
==============

Tool to create a 2d patch enclosing two lists of points

Example:

import numpy as np
from matplotlib import pyplot as plt
from profiles2patch import profiles2patch as P2P

XYlow=np.array([[1,2,3],[0.1,0.05,0.3]])
XYhigh=np.array([[1.5,2.5,3.5],[1.1,1.25,1.3]])
myP=P2P(XYlow,XYhigh)

plt.figure()
plt.plot([0.9,3.6],[0,2],'.')
plt.gca().add_patch(myP())
plt.show()
