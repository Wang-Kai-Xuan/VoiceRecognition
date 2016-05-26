#coding=utf-8

from PyQt4 import  QtGui,QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from fileCenterwidget import FileCenterWidget
from recordCenterwidget import RecordCenterWidget 
from recordWidget import RecordWidget
from playerWidget import PlayerWidget

class MainWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #定义控件
        self.menu_bar_sel_mode = QtGui.QMenuBar(self)        
        self.menu_sel = QtGui.QMenu(self)
        self.menu_setting = QtGui.QMenu(self)
        
        self.act_recognition_file = QtGui.QAction(self)
        self.act_recognition_record = QtGui.QAction(self)
        self.act_record = QtGui.QAction(self)
        self.act_player = QtGui.QAction(self)

        self.act_theme_1 = QtGui.QAction(self)
        self.act_theme_2 = QtGui.QAction(self)
        
        self.cnwd = RecordCenterWidget()
        
        #设置控件
        self.menu_setting.setTitle(u'系统设置&S')
        self.menu_sel.setTitle(u'模式选择&M')
        self.act_recognition_record.setText(u'识别录音')
        self.act_recognition_file.setText(u'识别文件')
        self.act_record.setText(u'录音')
        self.act_player.setText(u'播放音乐')
        
        self.act_theme_1.setText(u'主题1')
        self.act_theme_2.setText(u'主题2')
        
        self.menu_bar_sel_mode.addMenu(self.menu_sel)
        self.menu_bar_sel_mode.addMenu(self.menu_setting)
        
        self.menu_sel.addAction(self.act_recognition_record)
        self.menu_sel.addAction(self.act_recognition_file)
        self.menu_sel.addAction(self.act_record)
        self.menu_sel.addAction(self.act_player)
        self.menu_setting.addAction(self.act_theme_1)
        self.menu_setting.addAction(self.act_theme_2)
        
        #设置自身属性
        self.setMenuBar(self.menu_bar_sel_mode)
        self.setWindowTitle(u"语音识别工具")        
        self.setCentralWidget(self.cnwd)
        self.resize(800,600)    
        
        #设置信号和槽
        QtCore.QObject.connect(self.act_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("triggered()")),self.onRecord)
        QtCore.QObject.connect(self.act_player, QtCore.SIGNAL(QtCore.QString.fromUtf8("triggered()")),self.onPlayer)
        QtCore.QObject.connect(self.act_recognition_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("triggered()")),self.onRecognitionRecord)
        QtCore.QObject.connect(self.act_recognition_file, QtCore.SIGNAL(QtCore.QString.fromUtf8("triggered()")),self.onRecognitionFile)
        QtCore.QMetaObject.connectSlotsByName(self)

    @pyqtSignature("")        
    def onRecognitionRecord(self):
        test = RecordCenterWidget()
        self.setCentralWidget(test)
        test.show()
    
    @pyqtSignature("")        
    def onRecognitionFile(self):
        test = FileCenterWidget()
        self.setCentralWidget(test)
        test.show()
    
    @pyqtSignature("")        
    def onRecord(self):
        test = RecordWidget()
        self.setCentralWidget(test)
        self.resize(400,300)
        test.show()
    
    @pyqtSignature("")        
    def onPlayer(self):
        test = PlayerWidget()
        self.setCentralWidget(test)
        test.show()
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = MainWidget()
    test.show()
    sys.exit(app.exec_())
    