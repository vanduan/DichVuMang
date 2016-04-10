# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import re
from PyQt4 import QtCore, QtGui
import vlc
import sys

ins_vlc = vlc.Instance('--verbose 2'.split())
player_vlc = ins_vlc.media_player_new()

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
        MainWindow.resize(583, 91)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pic/windows_media_player_w.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.labelURL = QtGui.QLabel(self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(42, 20, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelURL.setFont(font)
        self.labelURL.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelURL.setObjectName(_fromUtf8("labelURL"))
        # Button Delete
        self.butdel = QtGui.QPushButton(self.centralwidget)
        self.butdel.setGeometry(QtCore.QRect(490, 17, 51, 25))
        self.butdel.setObjectName(_fromUtf8("butdel"))
        # Delete URL on click button Delete
        self.butdel.clicked.connect(self.deleteURL)

        # Button Play
        self.butplay = QtGui.QPushButton(self.centralwidget)
        self.butplay.setGeometry(QtCore.QRect(190, 50, 31, 31))
        self.butplay.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pic/media_player.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butplay.setIcon(icon1)
        self.butplay.setIconSize(QtCore.QSize(30, 30))
        self.butplay.setObjectName(_fromUtf8("butplay"))
        # Play media on click Button Play
        self.butplay.clicked.connect(self.play_video)

        # Button Pause
        self.butpause = QtGui.QPushButton(self.centralwidget)
        self.butpause.setGeometry(QtCore.QRect(260, 50, 31, 31))
        self.butpause.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pic/gtk_media_pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butpause.setIcon(icon2)
        self.butpause.setIconSize(QtCore.QSize(30, 30))
        self.butpause.setObjectName(_fromUtf8("butpause"))
        # Pause play media on click
        self.butpause.clicked.connect(self.pause_media)
        # Button Stop
        self.butstop = QtGui.QPushButton(self.centralwidget)
        self.butstop.setGeometry(QtCore.QRect(330, 50, 31, 31))
        self.butstop.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pic/gtk_media_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butstop.setIcon(icon3)
        self.butstop.setIconSize(QtCore.QSize(30, 30))
        self.butstop.setObjectName(_fromUtf8("butstop"))
        # Stop play media on click
        self.butstop.clicked.connect(self.stop_media)
        self.lineRUL = QtGui.QLineEdit(self.centralwidget)
        self.lineRUL.setGeometry(QtCore.QRect(80, 19, 401, 21))
        self.lineRUL.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sreaming Media Player", None))
        self.labelURL.setText(_translate("MainWindow", "URL: ", None))
        self.butdel.setText(_translate("MainWindow", "Delete", None))

    # Delete URL
    def deleteURL(self):
        self.lineRUL.clear()

    # Play media
    def play_video(self):

        url = str(self.lineRUL.text())
        state = self.check_url(url)
        if state and (str(player_vlc.get_state()) == 'State.NothingSpecial' or str(player_vlc.get_state()) == 'State.Stopped'):
            player_vlc.set_mrl(url)
            #if value_play==-1:
            #    # Pop up Info, Could'n play
            #    msg = QtGui.QMessageBox()
            #    msg.setIcon(QtGui.QMessageBox.Warning)
            #    msg.setText('''Couldn't Play it ''' + url + '!!!')
            #    msg.setWindowTitle('Error!')
            #    msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Close)
            #    msg.show()
            #    msg.exec_()
        # Unpause
        elif state and str(player_vlc.get_state()) == 'State.Paused':
            player_vlc.set_pause(0)
            print 'value_play 2', player_vlc.get_state()
            self.isPause = False


    # Check URL
    # If True => Return True
    # Else
    def check_url(self, url_check):
        # print url_check
        data = re.findall('.*://.*', url_check)
        if len(data) > 0:
            # Check protocol support
            list_protocols = ['http', 'mms', 'rtsp', 'mmsh']
            urls = url_check.split('://')
            if urls[0] not in list_protocols:
                # Pop up Info, Protocol not support
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText('Protocol ' + urls[0] + ' is not support !!!')
                msg.setWindowTitle('Info!')
                msg.setDetailedText('''Support {'http','mms','rtmp','rtsp','mmsh'}''')
                msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Close)
                msg.show()
                msg.exec_()

                return False
            return True
        else:
            # Pop up Error, URL not true
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setText('URL not true !!!')
            msg.setWindowTitle('Error!')
            msg.setDetailedText('URL like is: http://vanduan.com/path')
            msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Close)
            msg.show()
            msg.exec_()
        return False

    # Stop play media
    def stop_media(self):
        player_vlc.stop()
        print 'value_play 3', player_vlc.get_state()

    # Pause play media
    def pause_media(self):
        player_vlc.pause()
        print 'value_play 4', player_vlc.get_state()
        self.isPause = True


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
