import sys
import settings
from downloader import Skyroom_Downloader
from PyQt5 import QtCore, QtGui, QtWidgets


class GUI(object):
    def __init__(self, downloader):
        self.downloader = downloader
        
        app = QtWidgets.QApplication(sys.argv)
        
        QtGui.QFontDatabase.addApplicationFont(settings.Gui_Font_RobotoMono)
        QtGui.QFontDatabase.addApplicationFont(settings.Gui_Font_Vazir)
        self.qss = open(settings.Gui_StyleSheet, "r").read()

        self.CreateObjects()
        self.MainWindow.show()

        sys.exit(app.exec_())

    def CreateObjects(self):
        # Create Objects
        self.MainWindow = QtWidgets.QMainWindow()
        self.Widget = QtWidgets.QWidget(self.MainWindow)
        self.AppNameL = QtWidgets.QLabel(self.Widget)
        self.LinkL = QtWidgets.QLabel(self.Widget)
        self.NameL = QtWidgets.QLabel(self.Widget)
        self.PagesL = QtWidgets.QLabel(self.Widget)
        self.Link = QtWidgets.QLineEdit(self.Widget)
        self.Name = QtWidgets.QLineEdit(self.Widget)
        self.Pages = QtWidgets.QSpinBox(self.Widget)
        self.ProgressBar = QtWidgets.QProgressBar(self.Widget)
        self.Button = QtWidgets.QPushButton(self.Widget)
        
        # Set Style Objects
        self.__SetupMainWindow()
        self.Widget.setObjectName("Widget")
        self.__SetupAppNameL()
        self.__SetupLinkL()
        self.__SetupNameL()
        self.__SetupPagesL()
        self.__SetupLink()
        self.__SetupName()
        self.__SetupPages()
        self.__SetupProgressBar()
        self.__SetupButton()

        self.MainWindow.setCentralWidget(self.Widget)
        self.__retranslate(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def SetValue(self, v):
        self.ProgressBar.setValue(int(v))
    
    def start(self):
        url = self.Link.text()
        name = self.Name.text()
        page = int(self.Pages.value())
        self.ProgressBar.setMaximum(page)
        self.downloader = self.downloader(url, name, page, self.SetValue)
        self.downloader.download_images()
        self.__restart()

    def __restart(self):
        self.AppNameL.setText("Slides Downloaded")
        self.Link.setText("")
        self.Name.setText("")
        self.Pages.setValue(1)
        self.ProgressBar.setMaximum(1)
        self.ProgressBar.setValue(0)

    def __SetupMainWindow(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setEnabled(True)
        self.MainWindow.resize(550, 200)
        self.MainWindow.setStyleSheet(self.qss)
        self.MainWindow.setFixedSize(550, 200)
        self.MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

    def __SetupAppNameL(self):
        self.AppNameL.setGeometry(QtCore.QRect(10, 10, 530, 40))
        self.AppNameL.setAlignment(QtCore.Qt.AlignCenter)
        self.AppNameL.setObjectName("AppNameL")

    def __SetupLink(self):
        self.Link.setGeometry(QtCore.QRect(10, 80, 300, 25))
        self.Link.setObjectName("Link")
    
    def __SetupName(self):
        self.Name.setGeometry(QtCore.QRect(320, 80, 160, 25))
        self.Name.setObjectName("Name")
    
    def __SetupPages(self):
        self.Pages.setGeometry(QtCore.QRect(490, 80, 50, 25))
        self.Pages.setAlignment(QtCore.Qt.AlignCenter)
        self.Pages.setMinimum(1)
        self.Pages.setMaximum(999)
        self.Pages.setObjectName("Pages")

    def __SetupLinkL(self):
        self.LinkL.setGeometry(QtCore.QRect(10, 60, 40, 15))
        self.LinkL.setAlignment(QtCore.Qt.AlignCenter)
        self.LinkL.setObjectName("LinkL")
    
    def __SetupNameL(self):
        self.NameL.setGeometry(QtCore.QRect(320, 60, 40, 15))
        self.NameL.setAlignment(QtCore.Qt.AlignCenter)
        self.NameL.setObjectName("NameL")
    
    def __SetupPagesL(self):
        self.PagesL.setGeometry(QtCore.QRect(495, 60, 40, 15))
        self.PagesL.setAlignment(QtCore.Qt.AlignCenter)
        self.PagesL.setObjectName("PagesL")
    
    def __SetupProgressBar(self):
        self.ProgressBar.setGeometry(QtCore.QRect(10, 165, 530, 25))
        self.ProgressBar.setMaximum(1)
        self.ProgressBar.setValue(0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBar.setTextVisible(True)
        self.ProgressBar.setObjectName("ProgressBar")
    
    def __SetupButton(self):
        self.Button.setGeometry(QtCore.QRect(10, 115, 530, 40))
        self.Button.setAutoDefault(False)
        self.Button.setDefault(False)
        self.Button.setFlat(False)
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.start)

    def __retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skyroom Downloader"))
        self.AppNameL.setText(_translate("MainWindow", "Skyroom Downloader"))
        self.LinkL.setText(_translate("MainWindow", "Link"))
        self.NameL.setText(_translate("MainWindow", "Name"))
        self.PagesL.setText(_translate("MainWindow", "Pages"))
        self.Button.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    gui = GUI(Skyroom_Downloader)
