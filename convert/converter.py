import pydub
import numpy as np
import matplotlib.pyplot as plt


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

    arr = np.array(raw.get_array_of_samples())


    #if a.channels == 2: #????? we want mono
        #y = y.reshape((-1, 2))



    arr = norm_signal(arr)
    arr = hz_correct(arr, raw.frame_rate, rate)

    return arr

if __name__ == '__main__':
    audio_arr = audio_to_arr('samples/16kHz.wav')

    plt.plot(audio_arr)
    plt.show()
