#coding=utf-8

import wave
from pyaudio import PyAudio,paInt16
class Record():
    def __init__(self):
        self.chnnels = 1
        self.sampwidth = 2
        self.framerate = 8000
        self.NUM_SAMPLES = 2000
        self.isRecording = True
    
    def save_wav_file(self,save_file_name,data):
        print save_file_name
        wf = wave.open('%s.wav' % save_file_name, 'wb')
        wf.setnchannels(self.chnnels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes("".join(data))
        wf.close()
        
    def record_wav(self,save_file_name):
        pa = PyAudio()
        stream = pa.open(format = paInt16
                         ,channels = 1
                         ,rate = self.framerate
                         ,input = True
                         ,frames_per_buffer = self.NUM_SAMPLES)
        buf = []
        while self.isRecording:
            audio_data = stream.read(self.NUM_SAMPLES)
            buf.append(audio_data)
        self.save_wav_file(save_file_name, buf)
        stream.close()
    
    def record_default_wav(self):
        self.record_wav('default_record') 
        
        