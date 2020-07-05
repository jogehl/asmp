from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from func import broadband_beamforming
from func import doa_estimator

data_dict = {}
fourier_channel_dict = {}

sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

# number of bins for fourier transform
N = 400

for n in tqdm(range(0,16)):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]
    data_dict[n] = data_dict[n][0:192000]

    fourier_channel_dict[n] = np.fft.fft(data_dict[n],N)[0:200]

fourier_channel_matrix = np.array(list(fourier_channel_dict.values()))

freq_bins = np.fft.fftfreq(N, 1/sample_rate)[:200]



steps = 100

# compute the doa estimation
doa = doa_estimator(steps,fourier_channel_matrix,freq_bins)

# print the angles given by the estimator in degrees
print(np.rad2deg(doa[0]))
