from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

data_dict = {}

sample_rate = wavfile.read("Data/Preprocessed_UAV_1.wav")[0]

for n in range(0,16):
    data_dict[n] = wavfile.read("Data/Preprocessed_UAV_" + str(n+1) + ".wav")[-1]


stepsize = 1000

plt.figure(figsize = (15,4))


for keys,values in data_dict.items():
    max_value_abs = max(np.absolute(data_dict[keys]))
    plt.plot(np.arange(len(values[::stepsize]))*stepsize/samp_rate,(values[::stepsize]/(max_value_abs*100))+(0.01*keys))

plt.xlabel('time in [s]')
plt.ylabel('Amplitude, linear scale')
plt.savefig("Images/wav.png")
plt.show()


N = 1024

raw_samp_rate,raw_data = wavfile.read("Data/UAV_1.wav")
fourier_firstchannel = np.fft.fft(data_dict[0],N)
fourier_rawchannel = np.fft.fft(raw_data,N)

fourier_firstchannel = [np.abs(n) for n in fourier_firstchannel]
freq_bins = np.fft.fftfreq(N, 1/raw_samp_rate)

fourier_firstchannel_norm = np.linalg.norm(fourier_firstchannel)
fourier_firstchannel = [20 * np.log10(n/(fourier_firstchannel_norm*N)) for n in fourier_firstchannel]


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
