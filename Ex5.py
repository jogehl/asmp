from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from func import broadband_beamforming

data_dict = {}
fourier_channel_dict = {}

# reead in sample rate
sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

# number of bins for the fourier transform
N = 400

# read in the first second of all audio tracks and process the fourier transform
for n in tqdm(range(0,16)):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]
    data_dict[n] = data_dict[n][0:192000]

    fourier_channel_dict[n] = np.fft.fft(data_dict[n],N)[0:200]

fourier_channel_matrix = np.array(list(fourier_channel_dict.values()))

# get only the first 200 bins because of symmetry
freq_bins = np.fft.fftfreq(N, 1/sample_rate)[:200]


# calculate the broadband_beamforming for uv coordinates with step size of 1/50
steps = 50

u_v_array = np.zeros((2 * steps, 2 * steps))

for u in tqdm(range(-steps,steps)):
    for v in range(-steps,steps):
        if (u/steps)**2 + (v/steps)**2 < 1:
            u_v_array[v+steps][u+steps] = broadband_beamforming(u/steps,v/steps,fourier_channel_matrix, freq_bins)



extend = [-1,1,-1,1]

plt.clf()
im = plt.imshow(u_v_array,extent = extend,cmap = "hsv",origin = 'lower')
plt.colorbar(im)
plt.savefig("broadband_beamforming_heatmap.png")
plt.show()
