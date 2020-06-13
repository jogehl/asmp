from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from func import broadband_beamforming
from func import doa_estimator

data_dict = {}
fourier_channel_dict = {}
data_dict_second = {}

sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

N = 400

freq_bins = np.fft.fftfreq(N, 1/sample_rate)[:200]

doas = []

for n in tqdm(range(0,16)):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]



for second in tqdm(range(100)):

    for n in range(16):
        data_dict_second[n] = data_dict[n][192000 * second:192000 *(second+1)]
        fourier_channel_dict[n] = np.fft.fft(data_dict_second[n],N)[0:200]

    fourier_channel_matrix = np.array(list(fourier_channel_dict.values()))

    steps = 50

    doa = doa_estimator(steps,fourier_channel_matrix,freq_bins)
    doas.append((np.rad2deg(doa[0]),np.rad2deg(doa[1])))


plt.ylim(0,400)
plt.xlabel("time [s]")
plt.ylabel("Angle [deg]")
plt.title("DOA Azimuth angle")
plt.scatter(list(range(100)), [ a[0] for a in doas])
plt.savefig("doa_azimuth.png")
plt.show()

plt.ylim(20,100)
plt.xlabel("time [s]")
plt.ylabel("Angle [deg]")
plt.title("DOA Elevation angle")
plt.scatter(list(range(100)), [ a[1] for a in doas])
plt.savefig("doa_elevation.png")
plt.show()
