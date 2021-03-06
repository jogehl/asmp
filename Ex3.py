import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt, atan2
from tqdm import tqdm

from func import array_transfer_vector


# set step size for the uv coordinates. The calculation time is increasing quadratic to the number of steps
steps = 50

# initilialization of the uv coordinate array
u_v_arrays = [np.zeros((2 * steps, 2 * steps)) for _ in range(16)]

# calculation of the array transfer vector with a given frequency of 9000 Hz
for u in tqdm(range(-steps,steps)):
    for v in range(-steps,steps):
        if (u/steps)**2 + (v/steps)**2 < 1:
            for i,ret in enumerate(array_transfer_vector(u/steps,v/steps,9000)):
                u_v_arrays[i][v+steps][u+steps] = np.angle(ret)

# u_v_arrays = [np.flip(u_v_array,axis = 0) for u_v_array in u_v_arrays]

# Set axis ranges of the plot
extend = [-1,1,-1,1]

# generation of all images of all the audio tracks
for i in range(0,16):
    plt.clf()
    im = plt.imshow(u_v_arrays[i],extent = extend,cmap = "hsv",origin = 'lower')
    plt.colorbar(im)
    plt.savefig("array_transfer_vector_heatmap" + str(i+1) + ".png")
    plt.show()
