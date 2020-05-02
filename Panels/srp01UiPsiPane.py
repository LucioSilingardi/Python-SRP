# python srp01UiPsiPane.py

from PyQt5.QtCore    import pyqtSlot as Slot, pyqtProperty as Property
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QScrollArea
from PyQt5.QtWidgets import QSpinBox, QComboBox

class PsiRowList(QComboBox):
    def __init__(self, parent, ValLst):
        QComboBox.__init__(self)
        self.PsiItems = parent

        self.setFixedWidth(50)
        for Val in ValLst:
            self.addItem(Val)

    @Property(str)
    def Value(self):
        return self.currentText()

class PsiItems(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.UiPsiPnl = parent

        PsiItms = {}
        PsiItms = self.GetPsiItems() #Dizionario composto da "Item n" e ["5","4","3","2","1"]

        self.PsiItmIdx = 0
        self.PsiItmObj = {} #Dizionario vuoto
        FrmBox = QFormLayout() #Crea un'istanza del FormLayout
        for ItmDesc in PsiItms.keys(): #Per ogni chiave nel dizionario composto da item n + 54321:
            self.PsiItmIdx += 1 #Aumenta l'index, cosi parte da 1 subito e si incrementa
            ValList = PsiItms[ItmDesc] #Assegna a ValList la lista delle opzioni ["5","4","3","2","1"]
            self.PsiItmObj[self.PsiItmIdx] = PsiRowList(self, ValList) #assegna all'id attuale il combo box custom!
            FrmBox.addRow(ItmDesc, self.PsiItmObj[self.PsiItmIdx])

            #Aggiunge una riga al Form Box, composta da ItmDesc (la variabile di iterazione, corrispondente a Item 1, 2, 3 ecc...)
            #e composta dal dizionario che stiamo creando alla posizione self.PsiItmIdx, che è il nuovo combo box!
        self.setLayout(FrmBox)



  # In case you want to access the individual items
    @Property(int)
    def Value(self, Indx):
        RetVal = ''
        if Indx in self.PsiItmObj.keys():
            RetVal = self.PsiItmObj[Indx].Value

        return RetVal

    @Property(object)
    def ValuSet(self):
        RetVal = {}
        for Indx in self.PsiItmObj.keys():
            RetVal[Indx] = self.PsiItmObj[Indx].Value
        return RetVal
#22 32 33, 5,5, 10+
    def GetPsiItems(self):
      # This can be replaced by a dynamic call to a Database
      # Item and Contents
        ItmAndContnts = {}
      # Content List for Each Item currently static but 
      # could be dynamic if pulled from a Database
        for Idx in range(1,37):
            Text = 'Item ' + str(Idx) + '     '
            if Idx == 22 or Idx == 32:
                ItmAndContnts[Text] = ['5','4','3','2','1']
            elif Idx == 33:
                ItmAndContnts[Text] = ["10+", "8-9", "6-7", "4-5", "1-3"]
            else:
                ItmAndContnts[Text] = ["FA", "A", "I", "D", "FD"]


      # Note this returns a copy of the pointers but that is
      # all we need for this

        return ItmAndContnts.copy()

class UiPsiPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 0
       # -------
        HdrFont = QFont()
        HdrFont.setFamily("Times New Roman")
        HdrFont.setPointSize(18)
        HdrFont.setBold(True)
        HdrFont.setWeight(75)
       # -------NON SI VEDE! ->
        lblHedr = QLabel('Parenting Stress Index (P.S.I.)')
        lblHedr.setFont(HdrFont)
        lblHedr.setFixedWidth(320)
       # -------
        hbxHedr = QHBoxLayout()
        hbxHedr.addStretch(1)
        hbxHedr.addWidget(lblHedr)
        hbxHedr.addStretch(1)
       # -------
        lblNomePsi = QLabel('Nome del minore:')
        self.lneNomePsi = QLineEdit()
        self.lneNomePsi.setFixedWidth(150)
       # -------
        lblCognomePsi = QLabel('Cognome del minore:')
        self.lneCognomePsi = QLineEdit()
        self.lneCognomePsi.setFixedWidth(150)
       # -------
        lblAnniPsi = QLabel('Anni compiuti:')
        self.spbAnniPsi = QSpinBox()
        self.spbAnniPsi.setFixedWidth(50)
       # -------
        LftFrmBox = QFormLayout()
        LftFrmBox.addRow(lblNomePsi, self.lneNomePsi)
        LftFrmBox.addRow(lblCognomePsi, self.lneCognomePsi)
        LftFrmBox.addRow(lblAnniPsi, self.spbAnniPsi)
       # -------
        LftVBox = QVBoxLayout()
        LftVBox.addStretch(1)
        LftVBox.addWidget(lblHedr)
        LftVBox.addLayout(LftFrmBox)
        LftVBox.addStretch(1)
       # -------
        self.PsiItemList = PsiItems(self)
       # -------
        self.scaPsiItems = QScrollArea()
        self.scaPsiItems.resize(170, 400)
        self.scaPsiItems.setMaximumWidth(165)
        self.scaPsiItems.setSizeIncrement(0, 0)
        self.scaPsiItems.setWidgetResizable(True)
        self.scaPsiItems.setWidget(self.PsiItemList)
       # -------
        self.btnAvantiPsi = QPushButton('Avanti')
        self.btnAvantiPsi.clicked.connect(self.ProcessPsiData)
       # -------
        self.btnExitPsi = QPushButton('Exit')
        self.btnExitPsi.clicked.connect(self.ExitPsiData)
       # -------
        HBox2 = QHBoxLayout()
        HBox2.addWidget(self.btnAvantiPsi)
        HBox2.addWidget(QLabel(' '))
        HBox2.addWidget(self.btnExitPsi)
        HBox2.addStretch(1)
       # -------
        RitVBox = QVBoxLayout()
        RitVBox.addWidget(self.scaPsiItems)
        RitVBox.addLayout(HBox2)
       # -------
        FullHBox = QHBoxLayout()
        FullHBox.addLayout(LftVBox)
        FullHBox.addStretch(1)
        FullHBox.addLayout(RitVBox)
       # -------
        self.setLayout(FullHBox)

    @Slot()
    def NextPane(self):
        NextIdx = self.PaneIdx + 1
        self.CntrPane.Panes.setCurrentIndex(NextIdx)

    def ProcessPsiData(self):
      # Okay collecting this back in the CenterPane so that they can be easily
      # accessible by each subsequent Pane as well as can the Main Window if
      # needed there
        self.CntrPane.Nome = self.lneNomePsi.text()
        self.CntrPane.Cognome = self.lneCognomePsi.text()
        self.CntrPane.Age =  int(self.spbAnniPsi.value())
        self.CntrPane.PsiData = self.PsiItemList.ValuSet
      # Now we go to the next Pane
        NextPane = self.PaneIdx + 1
        self.CntrPane.UpdateNext(NextPane)

    def ExitPsiData(self):
      # This did not do anything but I put this place holder in place
      # to allow you to fill in what it supposed to do
        pass
