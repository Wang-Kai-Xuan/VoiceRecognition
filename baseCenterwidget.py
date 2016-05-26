#coding=utf-8

import wave
import json
import urllib2,pycurl
# from record import write_wav_file,record_wav 
from PyQt4 import  QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget
from PyQt4.QtCore import pyqtSignature

class BaseCenterWidget(QWidget):
    
    def __init__(self):
        QMainWindow.__init__(self)
        #定义的变量
        self.select_lang = 'zh'
        
        #定义的控件
        self.text_show= QtGui.QTextEdit(self)
        self.radbtn_zn = QtGui.QRadioButton(self)
        self.btn_push = QtGui.QPushButton(self)
        self.radbtn_en = QtGui.QRadioButton(self)
        self.lab_show_result = QtGui.QLabel(self)
        self.mainLayout = QtGui.QGridLayout(self)
        self.lin_show_dir = QtGui.QLineEdit(self)
                
        #对控件进行设置\初始化
        self.radbtn_en.setFixedWidth(120)        
        self.radbtn_zn.setFixedWidth(120)        
        
        self.radbtn_zn.setText(u"中文识别&C")
        self.radbtn_zn.setChecked(True)
        self.radbtn_en.setText(u"英文识别&E")
        self.btn_push.setText(u"识别&R")
        self.lab_show_result.setText(u'识别结果:')
        #对控件进行布局
        self.mainLayout.addWidget(self.radbtn_zn,0,0,1,1)
        self.mainLayout.addWidget(self.radbtn_en,0,1,1,1)
        self.mainLayout.addWidget(self.lin_show_dir,0,3,1,1)
        self.mainLayout.addWidget(self.btn_push,1,0,1,1)
        self.mainLayout.addWidget(self.lab_show_result,1,2,1,1)
        self.mainLayout.addWidget(self.text_show,2,0,1,4)
        self.setLayout(self.mainLayout)
        
        #槽函数没有括号
        QtCore.QObject.connect(self.btn_push, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onRecord)
        QtCore.QObject.connect(self.radbtn_zn, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectChinese)
        QtCore.QObject.connect(self.radbtn_en, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectEnglish)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    #接收百度云语音识别后返回的语音
    def dump_res(self,buf):
        my_temp = json.loads(buf)
        my_list = my_temp['result']
        self.text_show.append(my_list[0])            
    
    #获取验证字符串
    def get_token(self):
        apiKey = "ga5KXzZQ66lXWnYvUPs2gDyN"
        secretKey = "e432fdba97f5990794b907cfcb300323"
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id="+apiKey+"&client_secret="+secretKey
        #Open the URL url, which can be either a string or a Request object.
        #This function returns a file-like object with three additional methods:
        res = urllib2.urlopen(auth_url)
        #get response, save to json_data
        json_data = res.read()
        return json.loads(json_data)['access_token']
    
    #上传百度云语音进行识别
    def use_cloud(self,token):
        fp = wave.open(u'01.wav', 'rb')
        nf = fp.getnframes()
        #self.text_show.append(str(fp.getsampwidth()))
        #self.text_show.append(fp.getframerate())
        #self.text_show.append(fp.getnchannels())
        f_len = nf*2
        audio_data = fp.readframes(nf)
        
        cuid = "xxxx"
        #ser_url = 'http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token+'&lan=en'
        ser_url = 'http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token+'&lan='+self.select_lang
        http_header = ['Content-Type: audio/pcm; rate=8000',
                       'Content-Length: %d' % f_len]
        c = pycurl.Curl()
        c.setopt(pycurl.URL,str(ser_url))
        c.setopt(c.HTTPHEADER,http_header)
        c.setopt(c.POST,1)
        c.setopt(c.CONNECTTIMEOUT,80)
        c.setopt(c.TIMEOUT,80)
        c.setopt(c.WRITEFUNCTION,self.dump_res)
        c.setopt(c.POSTFIELDS,audio_data)
        c.setopt(c.POSTFIELDSIZE,f_len)
        c.perform()
    
    @pyqtSignature("")        
    def onRecord(self):
        self.text_show.append('onRecord...')
        #record_wav()
        self.use_cloud(self.get_token())
    
    @pyqtSignature("")        
    def onSelectChinese(self):
        self.select_lang = "zh"
    
    @pyqtSignature("")        
    def onSelectEnglish(self):
        self.select_lang = "en"
    