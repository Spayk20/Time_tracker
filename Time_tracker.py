import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings

import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Уход-Приход")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(400, 420)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 361, 41))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 20, 80, 50))
        self.spinBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(True)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setFont(QtGui.QFont('Times', 22))
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(300, 20, 80, 50))
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setFont(QtGui.QFont('Times', 20))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(180, 110, 80, 50))
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setFont(QtGui.QFont('Times', 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(300, 110, 80, 50))
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_4.setFont(QtGui.QFont('Times', 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(180, 200, 80, 50))
        self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_5.setFont(QtGui.QFont('Times', 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(300, 200, 80, 50))
        self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_6.setFont(QtGui.QFont('Times', 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 290, 141, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(QtGui.QFont('Times', 18))
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Приход"))
        self.label_2.setText(_translate("MainWindow", "Перерыв"))
        self.label_3.setText(_translate("MainWindow", "Уход"))
        self.label_4.setText(_translate("MainWindow", "Указать в ТИ:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


CONFIG_FILE_NAME = 'history.ini'


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("ПОСЧИТАТЬ")
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton.clicked.connect(self.save_conf)

        self.load_settings()

    def btnClicked(self):
        pri1 = self.ui.spinBox.value()
        pri2 = self.ui.spinBox_2.value()
        per1 = self.ui.spinBox_3.value()
        per2 = self.ui.spinBox_4.value()
        uhod1 = self.ui.spinBox_5.value()
        uhod2 = self.ui.spinBox_6.value()
        start_time = f'{pri1}:{pri2}'
        brake_time = f'{per1}:{per2}'
        finish_time = f'{uhod1}:{uhod2}'
        start_date_time = datetime.datetime.strptime(start_time, '%H:%M')
        brake_date_time = datetime.datetime.strptime(brake_time, '%H:%M')
        finish_date_time = datetime.datetime.strptime(finish_time, '%H:%M')

        work_time = finish_date_time - start_date_time
        work_time_wt_brake = datetime.datetime.strptime(str(work_time), '%H:%M:%S') - brake_date_time
        working_hour = work_time_wt_brake.seconds // 3600
        working_minutes = ((work_time_wt_brake.seconds // 60) % 60) if ((work_time_wt_brake.seconds // 60) % 60 != 0) else str('00')
        self.ui.textEdit.setText(str(f'{working_hour}:{working_minutes}'))
        self.ui.textEdit.setAlignment(QtCore.Qt.AlignCenter)

    def save_conf(self):
        settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)
        settings.setValue('Start_hour', self.ui.spinBox.value())
        settings.setValue('Start_minute', self.ui.spinBox_2.value())
        settings.setValue('break_hour', self.ui.spinBox_3.value())
        settings.setValue('break_minute', self.ui.spinBox_4.value())
        settings.setValue('end_hour', self.ui.spinBox_5.value())
        settings.setValue('end_minute', self.ui.spinBox_6.value())
        settings.setValue('rez', self.ui.textEdit.toPlainText())

    def load_settings(self):
        settings = QSettings(CONFIG_FILE_NAME, QSettings.IniFormat)

        self.ui.textEdit.setText(settings.value('rez'))
        self.ui.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.spinBox.setValue(int(settings.value('Start_hour')))
        self.ui.spinBox_2.setValue(int(settings.value('Start_minute')))
        self.ui.spinBox_3.setValue(int(settings.value('break_hour')))
        self.ui.spinBox_4.setValue(int(settings.value('break_minute')))
        self.ui.spinBox_5.setValue(int(settings.value('end_hour')))
        self.ui.spinBox_6.setValue(int(settings.value('end_minute')))


    def closeEvent(self, e):
        self.save_conf()
        super().closeEvent(e)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
