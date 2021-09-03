import subprocess, sys, os, shutil

try:
    import ffmpeg
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'ffmpeg-python'])
    import ffmpeg

try:
    from PIL import Image
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pillow'])
    from PIL import Image

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
    from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 350)
        MainWindow.setMinimumSize(QtCore.QSize(563, 350))
        MainWindow.setMaximumSize(QtCore.QSize(563, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shakalizatorHeader = QtWidgets.QLabel(self.centralwidget)
        self.shakalizatorHeader.setGeometry(QtCore.QRect(0, 0, 561, 71))
        self.shakalizatorHeader.setText("")
        self.shakalizatorHeader.setPixmap(QtGui.QPixmap("resources/shakalizator.jpg"))
        self.shakalizatorHeader.setObjectName("shakalizatorHeader")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 561, 252))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgbutton.sizePolicy().hasHeightForWidth())
        self.imgbutton.setSizePolicy(sizePolicy)
        self.imgbutton.setMinimumSize(QtCore.QSize(250, 250))
        self.imgbutton.setStyleSheet("font: 20pt \"Comic Sans MS\";")
        self.imgbutton.setObjectName("imgbutton")
        self.horizontalLayout.addWidget(self.imgbutton)
        self.vidbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.vidbutton.sizePolicy().hasHeightForWidth())
        self.vidbutton.setSizePolicy(sizePolicy)
        self.vidbutton.setMinimumSize(QtCore.QSize(250, 250))
        self.vidbutton.setStyleSheet("font: 20pt \"Comic Sans MS\";")
        self.vidbutton.setObjectName("vidbutton")
        self.horizontalLayout.addWidget(self.vidbutton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shakalizator"))
        self.imgbutton.setText(_translate("MainWindow", "Shakalize image"))
        self.vidbutton.setText(_translate("MainWindow", "Shakalize video"))

class Ui_VideoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 585)
        MainWindow.setMinimumSize(QtCore.QSize(790, 585))
        MainWindow.setMaximumSize(QtCore.QSize(790, 620))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 90, 591, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.soundqual = QtWidgets.QSlider(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundqual.sizePolicy().hasHeightForWidth())
        self.soundqual.setSizePolicy(sizePolicy)
        self.soundqual.setMaximumSize(QtCore.QSize(70, 16777215))
        self.soundqual.setOrientation(QtCore.Qt.Vertical)
        self.soundqual.setObjectName("soundqual")
        self.gridLayout.addWidget(self.soundqual, 0, 1, 1, 1)
        self.vidqual = QtWidgets.QSlider(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vidqual.sizePolicy().hasHeightForWidth())
        self.vidqual.setSizePolicy(sizePolicy)
        self.vidqual.setMaximumSize(QtCore.QSize(16777215, 70))
        self.vidqual.setOrientation(QtCore.Qt.Horizontal)
        self.vidqual.setObjectName("vidqual")
        self.gridLayout.addWidget(self.vidqual, 1, 0, 1, 1)
        self.bassboostlevel = QtWidgets.QDial(self.gridLayoutWidget)
        self.bassboostlevel.setObjectName("bassboostlevel")
        self.gridLayout.addWidget(self.bassboostlevel, 0, 0, 1, 1)
        self.backgroung = QtWidgets.QLabel(self.centralwidget)
        self.backgroung.setEnabled(True)
        self.backgroung.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.backgroung.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.backgroung.setText("")
        self.backgroung.setPixmap(QtGui.QPixmap("D:\\RAZNOE\\prgrming\\PyQtUIs\\../../!программирование/KOTIKOTstandalone/shakalizator/resources/videoshakal_bg.jpg"))
        self.backgroung.setObjectName("backgroung")
        self.bassboostTsiframi = QtWidgets.QSpinBox(self.centralwidget)
        self.bassboostTsiframi.setGeometry(QtCore.QRect(340, 240, 42, 22))
        self.bassboostTsiframi.setObjectName("bassboostTsiframi")
        self.bassboostNadpis = QtWidgets.QLabel(self.centralwidget)
        self.bassboostNadpis.setGeometry(QtCore.QRect(340, 260, 61, 16))
        self.bassboostNadpis.setObjectName("bassboostNadpis")
        self.vidQualTsiframi = QtWidgets.QSpinBox(self.centralwidget)
        self.vidQualTsiframi.setGeometry(QtCore.QRect(340, 440, 42, 22))
        self.vidQualTsiframi.setObjectName("vidQualTsiframi")
        self.VideoQualNadpis = QtWidgets.QTextBrowser(self.centralwidget)
        self.VideoQualNadpis.setGeometry(QtCore.QRect(330, 470, 71, 31))
        self.VideoQualNadpis.setObjectName("VideoQualNadpis")
        self.soundQualTsiframi = QtWidgets.QSpinBox(self.centralwidget)
        self.soundQualTsiframi.setGeometry(QtCore.QRect(630, 240, 42, 22))
        self.soundQualTsiframi.setObjectName("soundQualTsiframi")
        self.SoundQualNadpis = QtWidgets.QTextBrowser(self.centralwidget)
        self.SoundQualNadpis.setGeometry(QtCore.QRect(620, 270, 71, 41))
        self.SoundQualNadpis.setObjectName("SoundQualNadpis")
        self.pathToVideo = QtWidgets.QTextEdit(self.centralwidget)
        self.pathToVideo.setGeometry(QtCore.QRect(10, 10, 601, 31))
        self.pathToVideo.setObjectName("pathToVideo")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(610, 10, 131, 31))
        self.openButton.setObjectName("openButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 490, 171, 51))
        self.pushButton.setStyleSheet("font: 14pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 120, 151, 16))
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(30, 490, 31, 41))
        self.dial.setObjectName("dial")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(90, 520, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(760, 220, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 60, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(20, 90, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(60, 100, 22, 160))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(440, 500, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 570, 81, 16))
        self.label_2.setObjectName("label_2")
        self.backgroung.raise_()
        self.gridLayoutWidget.raise_()
        self.bassboostTsiframi.raise_()
        self.bassboostNadpis.raise_()
        self.vidQualTsiframi.raise_()
        self.VideoQualNadpis.raise_()
        self.soundQualTsiframi.raise_()
        self.SoundQualNadpis.raise_()
        self.pathToVideo.raise_()
        self.openButton.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.dial.raise_()
        self.horizontalScrollBar.raise_()
        self.verticalScrollBar.raise_()
        self.horizontalSlider.raise_()
        self.verticalSlider.raise_()
        self.verticalSlider_2.raise_()
        self.horizontalSlider_2.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Shakalizator"))
        self.bassboostNadpis.setText(_translate("MainWindow", "Bassboost"))
        self.VideoQualNadpis.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Video quality</p></body></html>"))
        self.SoundQualNadpis.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sound quality</p></body></html>"))
        self.pathToVideo.setPlaceholderText(_translate("MainWindow", "Path/To/Original/video.mp4"))
        self.openButton.setText(_translate("MainWindow", "Open video or sound file"))
        self.pushButton.setText(_translate("MainWindow", "SHAKALIZE!"))
        self.label.setText(_translate("MainWindow", "KOTIKOT, script by BarsTiger"))
        self.label_2.setText(_translate("MainWindow", "Its joke ui guys ;)"))

class Ui_PictureWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quailty = QtWidgets.QSlider(self.centralwidget)
        self.quailty.setGeometry(QtCore.QRect(0, 340, 1191, 131))
        self.quailty.setOrientation(QtCore.Qt.Horizontal)
        self.quailty.setObjectName("quailty")
        self.opisanie = QtWidgets.QTextBrowser(self.centralwidget)
        self.opisanie.setGeometry(QtCore.QRect(10, 0, 1171, 81))
        self.opisanie.setObjectName("opisanie")
        self.pathToPict = QtWidgets.QTextBrowser(self.centralwidget)
        self.pathToPict.setGeometry(QtCore.QRect(10, 100, 1171, 21))
        self.pathToPict.setReadOnly(False)
        self.pathToPict.setObjectName("pathToPict")
        self.openPict = QtWidgets.QPushButton(self.centralwidget)
        self.openPict.setGeometry(QtCore.QRect(10, 120, 1171, 221))
        self.openPict.setObjectName("openPict")
        self.shakalize = QtWidgets.QPushButton(self.centralwidget)
        self.shakalize.setGeometry(QtCore.QRect(0, 470, 1191, 23))
        self.shakalize.setObjectName("shakalize")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.opisanie.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Shakalizator</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">media files quality lowering program based on python, ffmpeg, pillow libs and PyQT5 UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Shakalize picture menu</span></p></body></html>"))
        self.pathToPict.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pathToPict.setPlaceholderText(_translate("MainWindow", "Path/To/picture.jpg"))
        self.openPict.setText(_translate("MainWindow", "Open picture"))
        self.shakalize.setText(_translate("MainWindow", "Shakalize!"))

def compress_video(video_full_path, output_file_name):
    # Target audio bitrate, in bps
    # Target video bitrate, in bps.
    # audio_bitrate min 20000, shakal 30000
    # video_bitrate min 100000, shakal 150000
    audio_bitrate = 20000
    video_bitrate = 150000

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                  ).overwrite_output().run()

def bassboost(video_full_path, output_file_name):
    audio_bitrate = 200000
    video_bitrate = 500000

    i = ffmpeg.input(video_full_path)

    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4',
                     'af': 'bass=g={0}:f=110:w=0.6'.format(10)}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate,
                     'af': 'bass=g={0}:f=110:w=0.6'.format(10)}
                  ).overwrite_output().run()

videoname = "nominalo"
imagename = 'dababy'
im1 = Image.open(imagename + ".jpg")
IMAGE_10 = imagename + "_shakalized.jpg"
im1.save(IMAGE_10, "JPEG", quality=0)


# compress_video(videoname + '.mp4', 'output.mp4')
# bassboost(videoname + '.mp4', 'outputbass.mp4')

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
uimain = Ui_MainWindow()
uimain.setupUi(MainWindow)
MainWindow.show()

# VideoWindow = QtWidgets.QMainWindow()
# uivideo = Ui_VideoWindow()
# uivideo.setupUi(VideoWindow)
# VideoWindow.show()

# PictureWindow = QtWidgets.QMainWindow()
# uipict = Ui_PictureWindow()
# uipict.setupUi(PictureWindow)
# PictureWindow.show()

sys.exit(app.exec_())

