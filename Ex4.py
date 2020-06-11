import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt, atan2
from tqdm import tqdm

from func import array_factor



steps = 100

u_v_array = np.zeros((2 * steps, 2 * steps))

for u in tqdm(range(-steps,steps)):
    for v in range(-steps,steps):
        if (u/steps)**2 + (v/steps)**2 <= 1:
            u_v_array[u+steps][v+steps] = array_factor(u/steps,v/steps,9000)

plt.clf()
im = plt.imshow(u_v_array)
plt.colorbar(im)
plt.savefig("array_factor_heatmap.png")
plt.show()
