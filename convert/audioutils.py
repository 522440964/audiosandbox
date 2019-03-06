import pydub
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile
import cv2

"""
Notes: 
- Normalization needs to clip extreme signals to ensure audio does go completely quiet with loud noises
- Needs ffmeg installed to work
"""


def norm_signal(arr):
    # clip max sounds if discrepence too large
    # most should exist on +- 0.5?

    # cheap way
    max = arr.max()
    arr = arr / max
    return arr


def hz_correct(arr, curRate, newRate):
    ratio = curRate / newRate
    arr = np.interp(np.arange(0, len(arr), ratio), np.arange(0, len(arr)), arr) #interpolating array by ratio
    return arr


def audio_to_arr(fname, rate=44100):

    if '.mp3' in fname:
        raw = pydub.AudioSegment.from_mp3(fname)

    elif '.wav' in fname:
        raw = pydub.AudioSegment.from_wav(fname)

    elif '.ogg' in fname:
        raw = pydub.AudioSegment.from_ogg(fname)

    elif '.flv' in fname:
        raw = pydub.AudioSegment.from_flv(fname)
    else:
        print('File Format: ".' + str(fname.split('.')[-1]) + '" is unsupported.')

    arr = np.array(raw.get_array_of_samples())

    chans = raw.channels
    if chans > 1:
        arr = arr.reshape((-1, chans))
        arr = arr.sum(axis=1) / chans

    arr = hz_correct(arr, raw.frame_rate, rate)
    lengths = len(arr) / rate

    return arr, lengths


def arr_to_stft(arr, sample_rate, nperseg=2048):
    _, _, stft_arr = sig.stft(arr, sample_rate, nperseg=nperseg)
    return stft_arr


def stft_to_arr(stft_arr, sample_rate, nperseg=2048):
    _, recon = sig.istft(stft_arr, sample_rate, nperseg=nperseg)
    recon = np.rint(recon).astype(np.int16)
    return recon


if __name__ == '__main__':
    rate = 36000
    audio_arr, length = audio_to_arr('samples/128k.mp3', rate=rate)
    stft = arr_to_stft(audio_arr, rate)
    recon = stft_to_arr(stft, rate)
    test_file = 'reconstructed.wav'
    scipy.io.wavfile.write(test_file, rate, recon)


    #plt.title(str(length) + " seconds")
    #plt.plot(audio_arr)
    #plt.show()
