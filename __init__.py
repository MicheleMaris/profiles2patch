__DESCRIPTION__="""converts a couple of XY profiles into a patch"""

class profiles2patch :
  """converts a couple of XY profiles into a patch"""
  def __init__(self,xylow,xyup) :
    """xylow, xyup = two rows columns forl ower and upper profile"""
    import numpy as np
    x=[]
    y=[]
    for k in range(len(xyup[0])) :
      x.append(xyup[0][k])
      y.append(xyup[1][k])
    for k in range(len(xylow[0])-1,-1,-1) :
      x.append(xylow[0][k])
      y.append(xylow[1][k])
    x.append(xyup[0][0])
    y.append(xyup[1][0])
    self.xy = np.array([x,y]).transpose()
  def __call__(self,*arg,**karg) :
    """creates a patch, keyowrds from patches"""
    from matplotlib import patches
    return patches.Polygon(self.xy,**karg)
  

