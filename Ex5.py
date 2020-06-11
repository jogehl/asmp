from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from func import broadband_beamforming

data_dict = {}
fourier_channel_dict = {}

sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

N = 400

for n in tqdm(range(0,16)):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]
    data_dict[n] = data_dict[n][0:192000]

    fourier_channel_dict[n] = np.fft.fft(data_dict[0],N)[0:200]

fourier_channel_matrix = np.array(list(fourier_channel_dict.values()))

freq_bins = np.fft.fftfreq(N, 1/sample_rate)[:200]



steps = 100

u_v_array = np.zeros((2 * steps, 2 * steps))

for u in tqdm(range(-steps,steps)):
    for v in range(-steps,steps):
        if (u/steps)**2 + (v/steps)**2 <= 1:
            u_v_array[u+steps][v+steps] = broadband_beamforming(u/steps,v/steps,fourier_channel_matrix, freq_bins)

plt.clf()
im = plt.imshow(u_v_array)
plt.colorbar(im)
plt.savefig("broadband_beamforming_heatmap.png")
plt.show()