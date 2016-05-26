#coding=utf-8

from PyQt4 import  QtGui, QtCore
from PyQt4.QtCore import pyqtSignature
from baseCenterwidget import BaseCenterWidget
from record import record_wav 

class RecordCenterWidget(BaseCenterWidget):
    def __init__(self):
        BaseCenterWidget.__init__(self)

        self.btn_record = QtGui.QPushButton(self)
        self.btn_select_file= QtGui.QPushButton(self)

        self.btn_record.setText(u"开始录音&B")
        self.btn_select_file.setText(u"保存路径&D")

        self.mainLayout.addWidget(self.btn_select_file,0,2,1,1)
        self.mainLayout.addWidget(self.btn_record,1,1,1,1)
        
        QtCore.QObject.connect(self.btn_record, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onRecord)
        QtCore.QObject.connect(self.btn_select_file, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectDir)
        QtCore.QMetaObject.connectSlotsByName(self)

    @pyqtSignature("")        
    def onSelectDir(self):
        path = QtGui.QFileDialog.getExistingDirectory()
        self.lin_show_dir.setText(unicode(path))
    @pyqtSignature("")        
    def onRecord(self):
#         record_wav()
        pass
