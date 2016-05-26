#coding=utf-8

from PyQt4 import  QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from record import Record
import os
import time
import threading

class RecordWidget(QWidget,Record,threading.Thread):
    
    def __init__(self):
        QWidget.__init__(self)
        Record.__init__(self)
        threading.Thread.__init__(self)
        
#         self.record = Record()
        self.btn_begin_record = QtGui.QPushButton(self)
        self.btn_stop_record = QtGui.QPushButton(self)
        self.btn_sel_save_dir= QtGui.QPushButton(self)
        self.btn_postfix= QtGui.QPushButton(self)
        self.layout= QtGui.QGridLayout(self)
        self.lin_show_dir= QtGui.QLineEdit(self)
        self.lab_save_file_dir= QtGui.QLabel(self)
        self.lab_save_name= QtGui.QLabel(self)
        self.lin_save_name= QtGui.QLineEdit(self)
        self.lab_begin_record_time= QtGui.QLabel(self)
        self.lin_begin_record_time= QtGui.QLineEdit(self)
        self.lab_stop_record_time= QtGui.QLabel(self)
        self.lin_stop_record_time= QtGui.QLineEdit(self)
        self.lin_record_time= QtGui.QLineEdit(self)
        self.lab_show_record_time= QtGui.QLabel(self)
        self.record_time=0
        self.lab_begin_record_time.setText(u'开始录音时间:')
        self.lab_stop_record_time.setText(u'停止录音时间:')
        self.btn_begin_record.setText(u'开始录音')
        self.btn_stop_record.setText(u'停止录音')
        self.btn_sel_save_dir.setText(u'...')
        self.btn_postfix.setText(u'.wav')
        self.lab_save_file_dir.setText(u'录音保存路径:')
        self.lab_save_name.setText(u'录音保存名字:')
        self.lab_show_record_time.setText(u'录音时长:')
        self.lin_show_dir.setText(os.getcwd())
        self.btn_begin_record.setFixedWidth(120)
        self.btn_stop_record.setFixedWidth(120)
        self.lab_save_file_dir.setFixedWidth(120)
        self.btn_sel_save_dir.setFixedWidth(20)
        
        self.layout.addWidget(self.lab_save_file_dir,0,0,1,1)
        self.layout.addWidget(self.lin_show_dir,0,1,1,1)
        self.layout.addWidget(self.btn_sel_save_dir,0,2,1,1)
        self.layout.addWidget(self.lab_save_name,1,0,1,1)
        self.layout.addWidget(self.lin_save_name,1,1,1,1)
        self.layout.addWidget(self.btn_postfix,1,2,1,1)
        self.layout.addWidget(self.lab_begin_record_time,2,0,1,1)
        self.layout.addWidget(self.lin_begin_record_time,2,1,1,1)
        self.layout.addWidget(self.lab_stop_record_time,3,0,1,1)
        self.layout.addWidget(self.lin_stop_record_time,3,1,1,1)
        self.layout.addWidget(self.lab_show_record_time,4,0,1,1)
        self.layout.addWidget(self.lin_record_time,4,1,1,1)
        self.layout.addWidget(self.btn_begin_record,5,0,1,1)
        self.layout.addWidget(self.btn_stop_record,5,1,1,1)
        self.setLayout(self.layout)
        
        QtCore.QObject.connect(self.btn_sel_save_dir, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectDir)
        QtCore.QObject.connect(self.btn_begin_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onBeginRecord)
        QtCore.QObject.connect(self.btn_stop_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onStopRecord)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    @pyqtSignature("")        
    def onStopRecord(self):
        self.lin_stop_record_time.setText(time.strftime('%Y-%m-%d %M %S',time.localtime()))
        self.lin_record_time.setText('%d secs' % (time.time()-self.record_time))
#         self.record.isRecording = True
        self.isRecording = False
        print 'in recwid'
        print self.isRecording
        self.close()
    @pyqtSignature("")        
    def onBeginRecord(self):
        
        self.record_time = time.time()
        self.lin_begin_record_time.setText(time.strftime('%Y-%m-%d %M %S',time.localtime()))
        if self.lin_save_name.text().isEmpty():
            print 'is empty'
        else:
            self.setDaemon(True)
            self.start()

    def run(self):
        threading.Thread.run(self)
        self.record_wav(self.lin_save_name.text())
                
    @pyqtSignature("")        
    def onSelectDir(self):
        path = QtGui.QFileDialog.getExistingDirectory()
        self.lin_show_dir.setText(unicode(path))
