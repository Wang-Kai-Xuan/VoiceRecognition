#coding=utf-8

from PyQt4 import  QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from record import record_wav

class RecordWidget(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.btn_begin_record = QtGui.QPushButton(self)
        self.btn_stop_record = QtGui.QPushButton(self)
        self.btn_sel_save_dir= QtGui.QPushButton(self)
        self.btn_postfix= QtGui.QPushButton(self)
        self.layout= QtGui.QGridLayout(self)
        self.lin_show_dir= QtGui.QLineEdit(self)
        self.lab_save_file_dir= QtGui.QLabel(self)
        self.lab_save_name= QtGui.QLabel(self)
        self.lin_save_name= QtGui.QLineEdit(self)
        self.lab_show_record_time= QtGui.QLabel(self)
        
        self.btn_begin_record.setText(u'开始录音')
        self.btn_stop_record.setText(u'停止录音')
        self.btn_sel_save_dir.setText(u'...')
        self.btn_postfix.setText(u'.wav')
        self.lab_save_file_dir.setText(u'录音保存路径:')
        self.lab_save_name.setText(u'录音保存名字:')
        self.lab_show_record_time.setText(u'录音时长:')
        
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
        self.layout.addWidget(self.lab_show_record_time,2,0,1,1)
        self.layout.addWidget(self.btn_begin_record,3,0,1,1)
        self.layout.addWidget(self.btn_stop_record,3,1,1,1)
        self.setLayout(self.layout)
        
        QtCore.QObject.connect(self.btn_sel_save_dir, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectDir)
        QtCore.QObject.connect(self.btn_begin_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onBeginRecord)
        QtCore.QObject.connect(self.btn_stop_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onAddDirAudio)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    @pyqtSignature("")        
    def onBeginRecord(self):
        name = self.lin_save_name.text()
        print name
        if name.isEmpty():
            print 'is empty'
        else:
            record_wav(name+'.wav')
        
    @pyqtSignature("")        
    def onAddDirAudio(self):
        print 'onAddDirAudio'
        
    @pyqtSignature("")        
    def onSelectDir(self):
        path = QtGui.QFileDialog.getExistingDirectory()
        self.lin_show_dir.setText(unicode(path))
