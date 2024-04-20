
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
        return abs(c[:(d - 1)])
    else:
        return abs(c[:(d - 1)])
#def secant_method(list):
#def gradient_descent(array, guess):
def simple_localmax(arr, slope_thresh, index, floor):
    if arr[index+1]-arr[index] < slope_thresh and arr[index] >floor:
        return index
    elif arr[index+1]-arr[index] < 0:
        return simple_localmax(arr, slope_thresh, index + 1, floor)
    else:
        return simple_localmax(arr, slope_thresh, index - 1, floor)

def brute_force_max(arr):
    start_time = time.time()
    index = 0
    max = 0
    for i in range(0, arr.size):
        if int(arr[i]) > max:
            index = i
            max = arr[i]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time brute force: {elapsed_time} seconds")
    return index

if __name__ == '__main__':
    slice_size = 0.5
    for i in range(0, 1):
        slice = get_fft_at_slice(i, slice_size, 'sample_1.wav', plot=False)
        #print(len(slice))
        freq = brute_force_max(slice)
        print(freq)