import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt, atan2
from tqdm import tqdm

from func import array_transfer_vector



steps = 100

u_v_arrays = [np.zeros((2 * steps, 2 * steps)) for _ in range(16)]

for u in tqdm(range(-steps,steps)):
    for v in range(-steps,steps):
        if (u/steps)**2 + (v/steps)**2 <= 1:
            for i,ret in enumerate(array_transfer_vector(u/steps,v/steps,9000)):
                u_v_arrays[i][u+steps][v+steps] = ret

for i in range(0,16):
    plt.clf()
    im = plt.imshow(u_v_arrays[i])
    plt.colorbar(im)
    plt.savefig("array_transfer_vector_heatmap" + str(i+1) + ".png")
    plt.show()
