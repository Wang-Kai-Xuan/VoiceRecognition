#coding=utf-8

import wave
from pyaudio import PyAudio,paInt16

chnnels = 1
sampwidth = 2
framerate = 8000
NUM_SAMPLES = 2000
TIME = 2

def write_wav_file(filename,data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(chnnels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes("".join(data))
    wf.close()
    
def record_wav():
    pa = PyAudio()
    stream = pa.open(format = paInt16
                     ,channels = 1
                     ,rate = framerate
                     ,input = True
                     ,frames_per_buffer = NUM_SAMPLES)
    buf = []
    count = 0
    while count < TIME * 5:
        audio_data = stream.read(NUM_SAMPLES)
        buf.append(audio_data)
        count += 1
        print '...'
    write_wav_file('01.wav', buf)
    stream.close()
    