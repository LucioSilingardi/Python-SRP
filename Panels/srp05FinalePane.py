# python srp05FinalePane.py

from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton

class FinalePanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 4

        Font = QFont()
        Font.setPointSize(14)
        Font.setBold(True)
        
        lblTemp = QLabel('Finale Panel')
        lblTemp.setFont(Font)

        HBox1 = QHBoxLayout()
        HBox1.addStretch(1)
        HBox1.addWidget(lblTemp)
        HBox1.addStretch(1)

        self.btnNext = QPushButton('Done')
        self.btnNext.clicked.connect(self.AllDone)

        HBox2 = QHBoxLayout()
        HBox2.addStretch(1)
        HBox2.addWidget(self.btnNext)

        VBox = QVBoxLayout()
        VBox.addStretch(1)
        VBox.addLayout(HBox1)
        VBox.addStretch(1)
        VBox.addLayout(HBox2)

        self.setLayout(VBox)

    @pyqtSlot()
    def AllDone(self):
        self.CntrPane.MainWin.Close()

'''
        self.calcoli()

    def calcoli(self):
        ##indici_tot = list(window4.indici())
        ##indici_criticita = sum(list(indici_tot[0]))
        ##indici_risorse = sum(list(indici_tot[1]))

        sdq_tot = list(window4.sdq())
        sdq_criticita = sum(list(sdq_tot[0]))
        sdq_risorse = sum(list(sdq_tot[1]))


        psi_tot = list(window4.psi())
        psi_criticita = sum(list(psi_tot[0]))
        psi_risorse = sum(list(psi_tot[1]))

        ##criticita_tot = indici_criticita + sdq_criticita + psi_criticita

        ##risorse_tot = sdq_risorse + psi_risorse + indici_risorse
'''
