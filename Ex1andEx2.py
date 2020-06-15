from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

data_dict = {}
# read in data for sample_rate recognition
sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

# read in all data files
for n in range(0,16):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]

# set stepsize for plotting the amplitude. There are to many values to plot each value
stepsize = 1000

# initilialization of the figure for the 16 plots of the audio data
plt.figure(figsize = (15,4))

# plot the data
for keys,values in data_dict.items():
    max_value_abs = max(np.absolute(data_dict[keys]))
    plt.plot(np.arange(len(values[::stepsize]))*stepsize/samp_rate,(values[::stepsize]/(max_value_abs*100))+(0.01*keys))

plt.xlabel('time in [s]')
plt.ylabel('Amplitude, linear scale')
plt.savefig("Images/wav.png")
plt.show()

# Fourier Transform of the data
# N is number of bins
N = 1024

raw_samp_rate,raw_data = wavfile.read("Data/UAV_1.wav")
fourier_firstchannel = np.fft.fft(data_dict[0],N)
fourier_rawchannel = np.fft.fft(raw_data,N)

fourier_firstchannel = [np.abs(n) for n in fourier_firstchannel]
# generation of the frequencies of the bins
freq_bins = np.fft.fftfreq(N, 1/raw_samp_rate)

fourier_firstchannel_norm = np.linalg.norm(fourier_firstchannel)
# calculate the dB values of the fourier transformed data
fourier_firstchannel = [20 * np.log10(n/(fourier_firstchannel_norm*N)) for n in fourier_firstchannel]

# plot the fourier transform of the first channel
plt.ylim(-100,0)
plt.ticklabel_format(style= 'sci',axis = 'x',scilimits=(0,0))
plt.plot(freq_bins,fourier_firstchannel,linewidth = 0.5)
plt.savefig("Images/channel1_data_fourier.png")
plt.show()


fourier_firstchannel_norm
fourier_rawchannel = [20 * np.log10(n/(fourier_firstchannel_norm*N)) for n in fourier_rawchannel]

plt.ylim(-100,0)
plt.ticklabel_format(style= 'sci',axis = 'x',scilimits=(0,0))
plt.plot(freq_bins,fourier_rawchannel,linewidth = 0.5)
plt.savefig("Images/raw_data_fourier.png")
plt.show()
