# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(567, 545)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startb = QtGui.QPushButton(self.centralwidget)
        self.startb.setGeometry(QtCore.QRect(70, 460, 90, 32))
        self.startb.setObjectName(_fromUtf8("startb"))
        self.temp = QtGui.QLCDNumber(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(80, 120, 64, 41))
        self.temp.setAutoFillBackground(False)
        self.temp.setFrameShape(QtGui.QFrame.Box)
        self.temp.setFrameShadow(QtGui.QFrame.Sunken)
        self.temp.setObjectName(_fromUtf8("temp"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pressure = QtGui.QLCDNumber(self.centralwidget)
        self.pressure.setGeometry(QtCore.QRect(80, 230, 64, 41))
        self.pressure.setFrameShadow(QtGui.QFrame.Sunken)
        self.pressure.setObjectName(_fromUtf8("pressure"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.flow = QtGui.QLCDNumber(self.centralwidget)
        self.flow.setGeometry(QtCore.QRect(240, 120, 64, 41))
        self.flow.setFrameShadow(QtGui.QFrame.Sunken)
        self.flow.setObjectName(_fromUtf8("flow"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.quant = QtGui.QLCDNumber(self.centralwidget)
        self.quant.setGeometry(QtCore.QRect(240, 230, 64, 41))
        self.quant.setFrameShadow(QtGui.QFrame.Sunken)
        self.quant.setObjectName(_fromUtf8("quant"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 200, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 330, 251, 101))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 310, 62, 15))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tmax_led = KLed(self.centralwidget)
        self.tmax_led.setGeometry(QtCore.QRect(410, 80, 31, 31))
        self.tmax_led.setState(KLed.Off)
        self.tmax_led.setColor(QtGui.QColor(255, 0, 0))
        self.tmax_led.setObjectName(_fromUtf8("tmax_led"))
        self.tmin_led = KLed(self.centralwidget)
        self.tmin_led.setGeometry(QtCore.QRect(480, 80, 31, 31))
        self.tmin_led.setState(KLed.Off)
        self.tmin_led.setColor(QtGui.QColor(85, 0, 255))
        self.tmin_led.setObjectName(_fromUtf8("tmin_led"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 40, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 220, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.startb_2 = QtGui.QPushButton(self.centralwidget)
        self.startb_2.setGeometry(QtCore.QRect(420, 350, 90, 32))
        self.startb_2.setObjectName(_fromUtf8("startb_2"))
        self.tmax_set = QtGui.QSpinBox(self.centralwidget)
        self.tmax_set.setGeometry(QtCore.QRect(380, 280, 67, 27))
        self.tmax_set.setObjectName(_fromUtf8("tmax_set"))
        self.tmin_set = QtGui.QSpinBox(self.centralwidget)
        self.tmin_set.setGeometry(QtCore.QRect(470, 280, 67, 27))
        self.tmin_set.setObjectName(_fromUtf8("tmin_set"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startb.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "Temperatura", None))
        self.label_2.setText(_translate("MainWindow", "Pressão", None))
        self.label_3.setText(_translate("MainWindow", "Vazão", None))
        self.label_4.setText(_translate("MainWindow", "Quantidade", None))
        self.label_5.setText(_translate("MainWindow", "LOG", None))
        self.label_6.setText(_translate("MainWindow", "Alarmes", None))
        self.label_7.setText(_translate("MainWindow", "Tmáx", None))
        self.label_8.setText(_translate("MainWindow", "Tmin", None))
        self.label_9.setText(_translate("MainWindow", "Configuração", None))
        self.startb_2.setText(_translate("MainWindow", "Enviar", None))

from PyKDE4.kdeui import KLed
