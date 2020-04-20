# python srp01UiPsiPane.py

#from PyQt5.QtCore    import 
#from PyQt5.QtGui     import 
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from Panels.srp01UiPsiPane    import UiPsiPanel
from Panels.srp02UiSdqPane    import UiSdqPanel
from Panels.srp03UiIndiciPane import UiIndiciPanel
from Panels.srp04OutputPane   import OutputPanel
from Panels.srp05FinalePane   import FinalePanel

class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.MainWin = parent
     # These along with the rest of fields being collected perhaps
     # ought to be made into properties of this class but only if
     # you want to make it a more formal class structure which is
     # good programming style when making classes like this
        self.Nome = ''
        self.CogNome = ''
        self.Age =  0
        self.PsiData = []
        # -------
        self.UiPsiPane = UiPsiPanel(self)
        self.UiSdqPane = UiSdqPanel(self)
        self.UiIndPane = UiIndiciPanel(self)
        self.OutptPane = OutputPanel(self)
        self.FinalPane = FinalePanel(self)
        # -------
        self.Panes = QStackedWidget()
        self.Panes.addWidget(self.UiPsiPane)
        self.Panes.addWidget(self.UiSdqPane)
        self.Panes.addWidget(self.UiIndPane)
        self.Panes.addWidget(self.OutptPane)
        self.Panes.addWidget(self.FinalPane)
        self.Panes.setCurrentIndex(0)
        # -------
        VBox = QVBoxLayout()
        VBox.addWidget(self.Panes)
        # -------
        self.setLayout(VBox)

    def UpdateNext(self, Indx):
        self.Panes.setCurrentIndex(Indx)
        if Indx == 1:
            self.Panes.currentWidget().UpdateView()
