#coding=utf-8

from PyQt4 import  QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

class PlayerWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.btn_scan_audio = QtGui.QPushButton(self)
        self.btn_audio_dir = QtGui.QPushButton(self)
        self.btn_play_pause= QtGui.QPushButton(self)
        self.layout= QtGui.QGridLayout(self)
        self.audio_list = QtGui.QListView(self)
        
        self.btn_scan_audio.setText(u'扫描歌曲')
        self.btn_audio_dir.setText(u'打开歌曲文件夹')
        self.btn_play_pause.setText(u'播放|暂停')
        
#         self.btn_scan_audio.setFixedWidth(120)
#         self.btn_audio_dir.setFixedWidth(120)
#         self.btn_play_pause.setFixedWidth(20)
        
        self.layout.addWidget(self.btn_play_pause,0,0,1,1)
        self.layout.addWidget(self.btn_scan_audio,0,1,1,1)
        self.layout.addWidget(self.btn_audio_dir,0,2,1,1)
        self.layout.addWidget(self.audio_list,1,0,1,3)

        self.setLayout(self.layout)
        
        QtCore.QObject.connect(self.btn_play_pause, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectDir)
        QtCore.QObject.connect(self.btn_scan_audio, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onBeginRecord)
        QtCore.QObject.connect(self.btn_audio_dir, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onAddDirAudio)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
        
    @pyqtSignature("")        
    def onBeginRecord(self):
        print 'BeginRecord'
    
    @pyqtSignature("")        
    def onAddDirAudio(self):
        path = QtGui.QFileDialog.getOpenFileName()
#         model = QtCore.QAbstractListModel
#         model.beginInsertRows('======')
#         self.audio_list.setModel(model)
        
    @pyqtSignature("")        
    def onSelectDir(self):
        path = QtGui.QFileDialog.getExistingDirectory()
        self.lin_show_dir.setText(unicode(path))
