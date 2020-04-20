# python srpMenuToolBar.py

from PyQt5.QtWidgets import QDockWidget, QAction

class MenuToolBar(QDockWidget):
    def __init__(self, MainWin):
        QDockWidget.__init__(self)
        self.MainWin = MainWin
        self.MainMenu = MainWin.menuBar()

      # This is used to have a handle to the Menu Items
      # should you want to implement a Tool Bar later
        self.MenuActRef = {'UiPsiAct':0,
                           'UiSdqAct':0,
                           'UiIndAct':0,
                           'OutptAct':0,
                           'FinalAct':0}

        # ******* Create the SRP Menu *******
        self.SRPMenu  = self.MainMenu.addMenu('File')

        # ******* Create SRP Menu Items *******
        self.UiPsiAct = QAction('Ui&Psi', self)
      # In case you have or want to include an Icon
      #  self.UiPsiAct = QAction(QIcon('Images/uipsi.png'), 'Ui&Psi', self)
        self.UiPsiAct.setShortcut("Ctrl+P")
        self.UiPsiAct.setStatusTip('Clicca per accedere al P.S.I.') # <<< Your Explanatory Text in Your Language Goes Here
        self.UiPsiAct.triggered.connect(self.UiPsiPane)
        self.MenuActRef['UiPsiAct'] = self.UiPsiAct

        self.UiSdqAct = QAction('Ui&Sdq', self)
      # In case you have or want to include an Icon
      #  self.UiSdqAct = QAction(QIcon('Images/uisqd.png'), 'Ui&Sdq', self)
        self.UiSdqAct.setShortcut("Ctrl+S")
        self.UiSdqAct.setStatusTip('Clicca per accedere all\'S.D.Q.') # <<< Your Explanatory Text in Your Language Goes Here
        self.UiSdqAct.triggered.connect(self.UiSdqPane)
        self.MenuActRef['UiSdqAct'] = self.UiSdqAct

        self.UiIndAct = QAction('Ui&Indici', self)
      # In case you have or want to include an Icon
      #  self.UiIndAct = QAction(QIcon('Images/UiIndici.png'), 'Ui&Indici', self)
        self.UiIndAct.setShortcut("Ctrl+I")
        self.UiIndAct.setStatusTip('Clicca per accedere agli indici') # <<< Your Explanatory Text in Your Language Goes Here
        self.UiIndAct.triggered.connect(self.UiIndiciPane)
        self.MenuActRef['UiIndAct'] = self.UiIndAct

        # ******* Create SRP Menu Items *******
        self.OutptAct = QAction('&Output', self)
      # In case you have or want to include an Icon
      #  self.OutptAct = QAction(QIcon('Images/output.png'), 'Ui&Psi', self)
        self.OutptAct.setShortcut("Ctrl+O")
        self.OutptAct.setStatusTip('Clicca per ottenere i risultati') # <<< Your Explanatory Text in Your Language Goes Here
        self.OutptAct.triggered.connect(self.OutputPane)
        self.MenuActRef['OutptAct'] = self.OutptAct

        # ******* Create SRP Menu Items *******
        self.FinalAct = QAction('&Finale', self)
      # In case you have or want to include an Icon
      #  self.FinalAct = QAction(QIcon('Images/finale.png'), '&Finale', self)
        self.FinalAct.setShortcut("Ctrl+F")
        self.FinalAct.setStatusTip('This is the Finale View') # <<< Your Explanatory Text in Your Language Goes Here
        self.FinalAct.triggered.connect(self.FinalePane)
        self.MenuActRef['FinalAct'] = self.FinalAct

        # ******* Setup the World Menu *******
        self.SRPMenu.addAction(self.UiPsiAct)
        self.SRPMenu.addAction(self.UiSdqAct)
        self.SRPMenu.addAction(self.UiIndAct)
        self.SRPMenu.addSeparator()
        self.SRPMenu.addAction(self.OutptAct)
        self.SRPMenu.addSeparator()
        self.SRPMenu.addAction(self.FinalAct)

# These are the Menu/Tool Bar Actions
    def UiPsiPane(self):
        self.MainWin.SwitchPanes(0)

    def UiSdqPane(self):
        self.MainWin.SwitchPanes(1)

    def UiIndiciPane(self):
        self.MainWin.SwitchPanes(2)

    def OutputPane(self):
        self.MainWin.SwitchPanes(3)

    def FinalePane(self):
        self.MainWin.SwitchPanes(4)
