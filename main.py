# coding:utf-8

'''
author:kdxcxs@github.com
'''

import sys,base64
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QDialog,QApplication
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QByteArray
from icon import iconb64
from mainWindow import Ui_MainWindow
from dumping import Ui_dumpingDialog
from ncmdump import dump

class mainWindow(QMainWindow):
    def __init__(self, scalRate):
        super(mainWindow, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,scalRate)
        self.setupIcon()
        self.dumpingdialog = dumpingDialog(self,self.icon)
        self.initSignal()
        self.show()
    def setupIcon(self):
        self.pmap = QPixmap()
        self.pmap.loadFromData(QByteArray.fromBase64(iconb64))
        self.icon = QIcon(self.pmap)
        self.setWindowIcon(self.icon)
    def initSignal(self):
        self.ui.commandLinkButton.clicked.connect(self.dumper)
    def dumper(self):
        files,fileType = QFileDialog.getOpenFileNames(self,
                                                      "请选择ncm文件",
                                                      "./",
                                                      "NeteaseCloudMusic Files (*.ncm)")
        if files:
            outputPath = QFileDialog.getExistingDirectory(self,
                                                          '请选择输出文件夹',
                                                          './')
            if outputPath:
                self.dumpingdialog.show()
                filesTotal, filesDumped = len(files), 0
                self.dumpingdialog.ui.label.setText(f'转换中\n{filesDumped}/{filesTotal}')
                for file in files:
                    dump(file,outputPath+'/'+file.split('/')[-1][:-3]+'mp3')
                    filesDumped += 1
                    self.dumpingdialog.ui.label.setText(f'转换中\n{filesDumped}/{filesTotal}')
                self.dumpingdialog.setWindowTitle('转换完毕!')
                self.dumpingdialog.ui.label.setText('转换完毕!')

class ncmDumper(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.scalRate = self.app.screens()[0].logicalDotsPerInch()/96
        self.mainwindow = mainWindow(self.scalRate)

class dumpingDialog(QDialog):
    def __init__(self,parent,icon):
        super(dumpingDialog, self).__init__(parent)
        self.ui = Ui_dumpingDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(icon)

if __name__ == '__main__':
    dumper = ncmDumper()
    sys.exit(dumper.app.exec_())