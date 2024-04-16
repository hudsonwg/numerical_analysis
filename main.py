
import numpy as np
from scipy.io import wavfile
import warnings
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import winsound
import time
'''
make getfftattimeslice(time slice)
make rootfind(fftslice)
then make map that maps frequencies to notes
then map to midi

'''
warnings.simplefilter("ignore", category=wavfile.WavFileWarning)

def get_fft_at_slice(start, duration, path, plot):


    fs, data = wavfile.read(path)
    time_slice = duration
    start_samples = int(start*fs)
    num_samples = int(time_slice * fs)

    transform_data = data[start_samples:start_samples + num_samples]
    a = transform_data.T[0]
    b = [(ele / 2 ** 8.) * 2 - 1 for ele in a]
    c = fft(b)
    d = int(len(c) / 2)

    if plot:
        d = 2000
        plt.plot(abs(c[:(d - 1)]), 'r')
        plt.show()
    else:
        return abs(c[:(d - 1)])
#def secant_method(list):

if __name__ == '__main__':

    slice_size = 0.5
    for i in range(0, 20):
        slice = get_fft_at_slice(i, slice_size, 'sample_1.wav', plot=False)
        freq = np.argmax(slice)

        print(freq)
        winsound.Beep(freq*2, 1000)
        time.sleep(1)

