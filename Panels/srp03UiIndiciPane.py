# python srp03UiIndiciPane.py

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QScrollArea, \
    QWidget
from PyQt5.QtWidgets import QStyleFactory, QComboBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot as Slot, pyqtProperty as Property
from PyQt5.QtCore    import pyqtSlot


class IndiciRowList(QComboBox):
    def __init__(self, parent, ValLst):
        QComboBox.__init__(self)
        self.IndiciItems = parent

        self.setFixedWidth(100)
        for Val in ValLst:
            self.addItem(Val)

    @Property(str)
    def Value(self):
        return self.currentText()


class IndiciItems(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.UiIndiciPnl = parent

        IndiciItms = {}
        IndiciItms = self.GetIndiciItems()  # Dizionario composto da "Item n" e ["5","4","3","2","1"]

        self.IndiciItmIdx = 0
        self.IndiciItmObj = {}  # Dizionario vuoto
        FrmBox = QFormLayout()  # Crea un'istanza del FormLayout
        for ItmDesc in IndiciItms.keys():  # Per ogni chiave nel dizionario composto da item n + 54321:
            self.IndiciItmIdx += 1  # Aumenta l'index, cosi parte da 1 subito e si incrementa
            ValList = IndiciItms[ItmDesc]  # Assegna a ValList la lista delle opzioni ["5","4","3","2","1"]
            self.IndiciItmObj[self.IndiciItmIdx] = IndiciRowList(self,
                                                                 ValList)  # assegna all'id attuale il combo box custom!
            FrmBox.addRow(ItmDesc, self.IndiciItmObj[self.IndiciItmIdx])
            # Aggiunge una riga al Form Box, composta da ItmDesc (la variabile di iterazione, corrispondente a Item 1, 2, 3 ecc...)
            # e composta dal dizionario che stiamo creando alla posizione self.PsiItmIdx, che è il nuovo combo box!
        FrmBox.setSpacing(10)
        self.setLayout(FrmBox)

    # In case you want to access the individual items
    @Property(int)
    def Value(self, Indx):
        RetVal = ''
        if Indx in self.IndiciItmObj.keys():
            RetVal = self.IndiciItmObj[Indx].Value

        return RetVal

    @Property(object)
    def ValuSet(self):
        RetVal = {}
        for Indx in self.IndiciItmObj.keys():
            RetVal[Indx] = self.IndiciItmObj[Indx].Value

        return RetVal

    def GetIndiciItems(self):
        # This can be replaced by a dynamic call to a Database
        # Item and Contents
        Indici_list = ["1. Povertà cronica", "2. Basso livello di istruzione", "3. Giovane età della madre",
                       "4. Carenza di relazioni interpersonali", "5. Carenza di reti e di integrazione sociale",
                       "6. Famiglia monoparentale", "7. Esperienze di rifiuto, violenza, abuso subite nell'infanzia",
                       "8. Sfiducia verso le norme sociali e le istituzioni",
                       "9. Accettazione della violenza e delle punizioni come pratiche educative",
                       "10. Accettazione della pornografia infantile",
                       "11. Scarse conoscenze e disinteresse per lo sviluppo del bambino",
                       "12. Psicopatologia genitori", "13. Devianza sociale genitori", "14. Abuso sostanze",
                       "15. Debole/assente capacità di assunzione responsabilità", "16. Sindrome da risarcimento",
                       "17. Distorsione emozioni / capacità empatiche", "18. Impulsività",
                       "19. Scarsa tolleranza frustrazioni", "20. Ansia da separazione",
                       "21. Gravidanza/maternità non desiderate",
                       "22. Relazioni difficili con famiglia d'origine del partner",
                       "23. Conflitti di coppia / violenza domestica", "24. Malattie fisiche/disturbi alla nascita",
                       "25. Temperamento difficile", "26. Sentimenti di inadeguatezza per dipendenza dai servizi",
                       "27. Rielaborazione rifiuto/violenza subiti nell'infanzia", "28. Capacità empatiche",
                       "29. Capacità di assunzione di responsabilità", "30. Desiderio di migliorarsi",
                       "31. Autonomia personale", "32. Buon livello di autostima",
                       "33. Relazione attuale soddisfacente con almeno un membro fam. Origine",
                       "34. Rete di supporto parentale / amicale", "35. Capacità di gestire i conflitti",
                       "36. Temperamento facile"]
        ItmAndContnts = {}
        # Content List for Each Item currently static but
        # could be dynamic if pulled from a Database
        for Idx in range(1, 37):
            Text = Indici_list[Idx - 1]
            ItmAndContnts[Text] = ["Non rilevato", "Assente", "Presente"]

        # Note this returns a copy of the pointers but that is
        # all we need for this

        return ItmAndContnts.copy()


# ------
class UiIndiciPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 2

        #WinLeft = 150;
        #WinTop = 150;
        #WinWidth = 550;
        #WinHigh = 500;
        #self.setGeometry(WinLeft, WinTop, WinWidth, WinHigh)

        #self.setStyle(QStyleFactory.create('Cleanlooks'))

        def set_indici_item_text(indici_object):
            indici_object.addItem("Non rilevato")
            indici_object.addItem("Assente")
            indici_object.addItem("Presente")

        HdrFont = QFont()
        HdrFont.setFamily("Times New Roman")
        HdrFont.setPointSize(15)
        HdrFont.setWeight(100)
        HdrFont.setBold(True)

        title_lbl = QLabel("INDICI: Fattori di rischio e protettivi")
        title_lbl.setFont(HdrFont)
        title_lbl.setFixedWidth(320)

        self.IndiciItemList = IndiciItems(self)
        # -------
        self.scaIndiciItems = QScrollArea()
        self.scaIndiciItems.resize(170, 400)
        self.scaIndiciItems.setSizeIncrement(0, 0)
        self.scaIndiciItems.setWidgetResizable(True)
        self.scaIndiciItems.setWidget(self.IndiciItemList)

        title_box = QHBoxLayout()
        title_box.addWidget(title_lbl)

        Base = QVBoxLayout()
        Buttons = QHBoxLayout()

        Avanti_btn = QPushButton("Avanti")
        Avanti_btn.clicked.connect(self.ProcessIndiciData)
        Spazio = QLabel(" ")
        Exit_btn = QPushButton("Exit")
        Exit_btn.clicked.connect(self.Exit)

        Buttons.addStretch(1)
        Buttons.addWidget(Avanti_btn)
        Buttons.addWidget(Spazio)
        Buttons.addWidget(Exit_btn)

        Base.addLayout(title_box)
        Base.addWidget(self.scaIndiciItems)
        Base.addSpacing(20)
        Base.addLayout(Buttons)

        self.setLayout(Base)

    @pyqtSlot()
    def NextPane(self):
        NextIdx = self.PaneIdx + 1
        self.CntrPane.Panes.setCurrentIndex(NextIdx)

    def UpdateView(self):
        pass

    def ProcessIndiciData(self):
        # Okay collecting this back in the CenterPane so that they can be easily
        # accessible by each subsequent Pane as well as can the Main Window if
        # needed there
        self.CntrPane.IndiciData = self.IndiciItemList.ValuSet
        # Now we go to the next Pane
        NextPane = self.PaneIdx + 1
        self.CntrPane.UpdateNext(NextPane)


    def Exit(self):
        # This did not do anything but I put this place holder in place
        # to allow you to fill in what it supposed to do
        pass


