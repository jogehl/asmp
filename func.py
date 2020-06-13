import numpy as np

def array_transfer_vector(u,v,frequency):

    positions=1/100 * np.array([[-1.808, -2.39,-0.44],    [3.398,2.163,-2.385],\
                                [-5.648, 6.876,  3.928],  [-1.789, -9.256, -1.255],\
                                [5.752,  3.134,  4.559],  [-2.467, -4.962, -6.543],\
                                [4.058,  -4.927, 2.834],  [-4.684, 3.996,  -6.812],\
                                [-7.206, 0.592,  -0.005], [-5.375, -3.333, 6.708],\
                                [0.729,  8.731,  0.717],  [-2.037, 2.156,  4.846],\
                                [7.092,  -4.499, -3.317], [-7.178, -5.793, -1.598],\
                                [-0.674, -7.188, 6.603],  [0.333,  7.047,  -5.119]])


    data_transfer_vector = np.zeros((16,),dtype=complex)
    w = np.sqrt(1 - u**2 - v**2)


    for n in range(0,16):
        out = np.exp(1j * 2.0  * np.pi * (frequency / 343.0) * np.array([u,v,w]) @ positions[n])
        data_transfer_vector[n] = out
        # print(out)
    # print(data_transfer_vector)
    return data_transfer_vector

def array_factor(u,v,frequency):
    return array_transfer_vector(0,0,frequency).conj().T @ array_transfer_vector(u,v,frequency)

def broadband_beamforming(u,v, Z : np.array, freq_bins:np.array):
    BF = np.sum([abs(array_transfer_vector(u,v,freq_bins[k]).conj().T @ Z[:,k])**2 for k in range(200)], axis = 0)
    return BF

def doa_estimator(steps, Z, freq_bins):
    bf = [(u,v,broadband_beamforming(u,v,Z, freq_bins)) for v in np.arange(-1, 1, 1/steps) for u in np.arange(-1, 1, 1/steps) if u**2 + v**2 <1]
    maximum = max(bf ,key = lambda a: a[2])

    u = maximum[0]
    v = maximum[1]
    w = np.sqrt(1 - u**2 - v**2)

    print(u,v)
    # azimuth_angle = np.arctan(u/w)
    # elevation_angle = np.arcsin(v)

    elevation_angle = np.arccos(w)
    azimuth_angle = np.arcsin(u/elevation_angle)

    if azimuth_angle < 0:
        azimuth_angle = 2*np.pi + azimuth_angle

    if elevation_angle < 0:
        elevation_angle = 2*np.pi + elevation_angle

    return (azimuth_angle,elevation_angle)
