from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1903, 1065)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(620, 270, 800, 500))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 650, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 760, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 760, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 870, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 760, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 710, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 820, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(860, 780, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(200,200,200);\n"
"font-size: 40px;")
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 320, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(90, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox.setMinimum(-385.25)
        self.doubleSpinBox.setMaximum(385.25)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(270, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox_2.setMinimum(-385.25)
        self.doubleSpinBox_2.setMaximum(385.25)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(450, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox_3.setMinimum(-385.25)
        self.doubleSpinBox_3.setMaximum(385.25)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 400, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 400, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(270, 130, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox_4.setMinimum(-180.0)
        self.doubleSpinBox_4.setMaximum(180.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_8.setObjectName("label_8")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(90, 130, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox_5.setFont(font)
        self.doubleSpinBox_5.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox_5.setMinimum(-180.0)
        self.doubleSpinBox_5.setMaximum(180.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(450, 130, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.doubleSpinBox_6.setFont(font)
        self.doubleSpinBox_6.setStyleSheet("color: rgb(200,200,200);\n"
"border: 1px solid white;\n"
"font-size: 25px;")
        self.doubleSpinBox_6.setMinimum(-180.0)
        self.doubleSpinBox_6.setMaximum(180.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1580, 150, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1620, 520, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1580, 800, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1580, 330, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1580, 230, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1580, 600, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1580, 430, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1580, 700, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1520, 50, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 50px;")
        self.label_18.setObjectName("label_18")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1620, 220, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(1620, 320, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(1620, 420, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(1620, 590, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber_4.setFont(font)
        self.lcdNumber_4.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(1620, 690, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber_5.setFont(font)
        self.lcdNumber_5.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(1620, 790, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(23)
        self.lcdNumber_6.setFont(font)
        self.lcdNumber_6.setStyleSheet("border: 1px solid rgb(200,200,200);")
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 220, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    font-size: 20px;\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_5.setObjectName("label_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 480, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    font-size: 20px;\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 580, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(200, 200, 200);\n"
"font-size: 30px;")
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(640, 30, 761, 211))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1903, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        dpi = 100  #Puedes ajustar esto según la configuración de tu pantalla
        width_in_inches = 800 / dpi
        height_in_inches = 500 / dpi
        self.figure = Figure(figsize=(width_in_inches, height_in_inches), dpi=dpi)

        #Matplotlib Figure
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.frame)
        self.ax = self.figure.add_subplot(111, projection='3d')

        #Set plot limits
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 400)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Controller"))
        self.pushButton.setText(_translate("MainWindow", "Y+"))
        self.pushButton_2.setText(_translate("MainWindow", "X+"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.pushButton_4.setText(_translate("MainWindow", "Y-"))
        self.pushButton_5.setText(_translate("MainWindow", "X-"))
        self.pushButton_6.setText(_translate("MainWindow", "Z+"))
        self.pushButton_7.setText(_translate("MainWindow", "Z-"))
        self.checkBox.setText(_translate("MainWindow", "Draw tool path"))
        self.label.setText(_translate("MainWindow", " Linear path generator"))
        self.label_2.setText(_translate("MainWindow", "Xf:"))
        self.label_3.setText(_translate("MainWindow", "Yf:"))
        self.label_4.setText(_translate("MainWindow", "Zf:"))
        self.label_6.setText(_translate("MainWindow", "θ<sub>2<sub>"))
        self.label_7.setText(_translate("MainWindow", "θ<sub>1</sub>"))
        self.label_8.setText(_translate("MainWindow", "θ<sub>3<sub>"))
        self.label_10.setText(_translate("MainWindow", "End effector"))
        self.label_11.setText(_translate("MainWindow", "Angles"))
        self.label_12.setText(_translate("MainWindow", "θ<sub>3<sub>"))
        self.label_13.setText(_translate("MainWindow", "Yf"))
        self.label_14.setText(_translate("MainWindow", "Xf"))
        self.label_15.setText(_translate("MainWindow", "θ<sub>1</sub>"))
        self.label_16.setText(_translate("MainWindow", "Zf"))
        self.label_17.setText(_translate("MainWindow", "θ<sub>2<sub>"))
        self.label_18.setText(_translate("MainWindow", "Current pose"))
        self.pushButton_9.setText(_translate("MainWindow", "Move robot"))
        self.label_5.setText(_translate("MainWindow", "Forward kinematics"))
        self.pushButton_10.setText(_translate("MainWindow", "Move robot"))
        self.label_9.setText(_translate("MainWindow", "Manual operation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
