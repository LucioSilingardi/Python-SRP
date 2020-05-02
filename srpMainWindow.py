# cd C:\DJ_Office\Students\LucioS
# python srpMainWindow.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QMenu, QStyleFactory

from srpCenterPanel import CenterPanel as CentrPane
from srpMenuToolBar import MenuToolBar as MnuTolBar

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('S.R.P. Main Window')
        WinLeft = 150; WinTop = 150; WinWidth = 500; WinHigh = 500
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHigh)

        self.CenterPane = CentrPane(self)
        self.setCentralWidget(self.CenterPane)

        self.MenuBar = MnuTolBar(self)

        self.SetStatusBar(self)
        self.setStyle(QStyleFactory.create('Cleanlooks'))

    def SetStatusBar(self, parent):
        StatusMsg = ''
        parent.StatBar = parent.statusBar()

        if len(StatusMsg) < 1:
          # This verbiage will disappear when you view menu items
            StatusMsg = 'Ready'

        parent.StatBar.showMessage(StatusMsg)

    def SwitchPanes(self, PaneIndx):
        self.CenterPane.Panes.setCurrentIndex(PaneIndx)

    def Close(self):
      # In case other things need to be done prior to concluding
        self.close()

if __name__ == '__main__':
    MainEvntThred = QApplication([])

    MainApplication = MainWindow()
    MainApplication.show()

    MainEvntThred.exec()
