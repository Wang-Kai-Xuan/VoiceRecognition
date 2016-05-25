#coding=utf-8

import wave
from pyaudio import PyAudio,paInt16
import json
import urllib2,pycurl

from PyQt4 import  QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget
from PyQt4.QtCore import pyqtSignature

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

result = '0'
def dump_res(buf):
    print buf
    my_temp = json.loads(buf)
    my_list = my_temp['result']
#     print type(my_list)
    print my_list[0]
    
    
def get_token():
    apiKey = "ga5KXzZQ66lXWnYvUPs2gDyN"
    secretKey = "e432fdba97f5990794b907cfcb300323"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id="+apiKey+"&client_secret="+secretKey
#Open the URL url, which can be either a string or a Request object.
#This function returns a file-like object with three additional methods:
    res = urllib2.urlopen(auth_url)
#get response, save to json_data
    json_data = res.read()
    return json.loads(json_data)['access_token']

def use_cloud(token):
    fp = wave.open(u'01.wav', 'rb')
    nf = fp.getnframes()
    print "sampwidth=",fp.getsampwidth()
    print "framerate=",fp.getframerate()
    print "nchannels=",fp.getnchannels()
    f_len = nf*2
    audio_data = fp.readframes(nf)
    
    cuid = "xxxx"
#     ser_url = 'http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token+'&lan=en'
    ser_url = 'http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token
    http_header = [
                   'Content-Type: audio/pcm; rate=8000',
                   'Content-Length: %d' % f_len
                   ]
    c = pycurl.Curl()
    c.setopt(pycurl.URL,str(ser_url))
    c.setopt(c.HTTPHEADER,http_header)
    c.setopt(c.POST,1)
    c.setopt(c.CONNECTTIMEOUT,80)
    c.setopt(c.TIMEOUT,80)
    c.setopt(c.WRITEFUNCTION,dump_res)
    c.setopt(c.POSTFIELDS,audio_data)
    c.setopt(c.POSTFIELDSIZE,f_len)
    c.perform()
    
class CenterWidget(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.text_show= QtGui.QTextEdit(self)
        self.btn_record = QtGui.QPushButton(self)
        self.radbtn_zn = QtGui.QRadioButton(self)
        self.radbtn_en = QtGui.QRadioButton(self)
        
        self.text_show.setText("recognition result:\n")
        self.btn_record.setText("start record")
        self.radbtn_zn.setText("to Chinaese")
        self.radbtn_en.setText("to English")
        
        self.mainLayout = QtGui.QGridLayout(self)
        self.mainLayout.addWidget(self.radbtn_zn,0,0,1,1)
        self.mainLayout.addWidget(self.radbtn_en,0,1,1,1)
        self.mainLayout.addWidget(self.text_show,1,0,1,2)
        self.mainLayout.addWidget(self.btn_record,2,0,1,1)
        self.setLayout(self.mainLayout)
        
#槽函数没有括号
        QtCore.QObject.connect(self.btn_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onStartRecord)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    @pyqtSignature("")        
    def onStartRecord(self):
        self.text_show.setText("alreadly clear")
        record_wav()
        print 'over'    
        use_cloud(get_token())
        print 'ok'    

    
class MainWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("ChatTools")        
        self.cnwd = CenterWidget()
        self.setCentralWidget(self.cnwd)    
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = MainWidget()
    test.show()
    sys.exit(app.exec_())
    