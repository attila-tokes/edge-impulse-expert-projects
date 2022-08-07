import sys, getopt
import pyaudio
import numpy as np

from cloudml import *

# Audio recording and playback
class Audio:
    SILENCE_TH_AVG = 250
    SILENCE_TH_MAX = 1250

    # Record audio up to a duration (or silence)
    def record(self, duration=3, silence_seconds=2, sample_rate=16000):
        result = np.array([], dtype='int16')
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=sample_rate)
        for i in range(duration):
          buffer = stream.read(sample_rate)
          sample = np.frombuffer(buffer, dtype='int16')
          result = np.append(result, sample)
          print("%", end="", flush=True);

          # silence detection
          avgV = np.average(np.absolute(sample))
          maxV = np.max(np.absolute(sample))
          if avgV <= Audio.SILENCE_TH_AVG and maxV <= Audio.SILENCE_TH_MAX:
            break

        stream.stop_stream()
        stream.close()
        audio.terminate()
        return result