#coding=utf-8

from PyQt4 import  QtGui, QtCore
from PyQt4.QtCore import pyqtSignature
from recognitionWidget import RecognitionWidget
from PyQt4.QtGui import QWidget

class FileCenterWidget(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)

        self.btn_select_file= QtGui.QPushButton(self)
        self.btn_select_file.setText(u"文件路径&D")

#         self.mainLayout.addWidget(self.btn_select_file,0,2,1,1)
        QtCore.QObject.connect(self.btn_select_file, QtCore.SIGNAL(QtCore.QString.fromUtf8("clicked()")),self.onSelectDir)
        QtCore.QMetaObject.connectSlotsByName(self)

    @pyqtSignature("")        
    def onSelectDir(self):
        path = QtGui.QFileDialog.getOpenFileName()
#         self.lin_show_dir.setText(unicode(path))
    