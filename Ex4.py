import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt, atan2
from tqdm import tqdm

from func import array_factor


# step size for uv coordinates
steps = 100

u_v_array = np.zeros((2 * steps, 2 * steps))

# calculation of the array factor for frequency 9000 Hz
for u in tqdm(np.arange(-1,1,1/steps)):
    for v in np.arange(-1,1,1/steps):
        if(u**2 + v**2 < 1):
            u_v_array[int((u+1)*steps)][int((v+1)*steps)]= np.absolute(array_factor(u,v,9000))

extend = [-1,1,-1,1]

# flip array so that the plot shows the right way
u_v_array = np.flip(u_v_array,axis = 0)

plt.clf()
im = plt.imshow(u_v_array,extent = extend,cmap = "hsv")
plt.colorbar(im)
plt.savefig("array_factor_heatmap.png")
plt.show()
