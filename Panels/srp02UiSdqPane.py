# python srp02UiSdqPane.py

from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QScrollArea
from PyQt5.QtWidgets import QSpinBox, QComboBox
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout


class UiSdqPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 2

        HdrFont = QFont()
        HdrFont.setFamily("Times New Roman")
        HdrFont.setPointSize(18)
        HdrFont.setWeight(100)

        VBox = QVBoxLayout()


        lblHedr = QLabel('Strenghts and Difficulties Questionnarire, S.D.Q.')
        lblHedr.setFont(HdrFont)





        GridBox = QGridLayout()


        x = 0
        y = 0
        for n in range(1, 26):
            label = QLabel("Item " + str(n))
            label.setFixedWidth(50)
            SpinBox = QSpinBox()
            SpinBox.setMaximum(2)
            SpinBox.setFixedWidth(50)
            GridBox.addWidget(label, x, y)
            y += 1
            if y == 6:
                x += 1
                y = 0
            GridBox.addWidget(SpinBox, x, y)
            y += 1
            if y == 6:
                x += 1
                y = 0
        GridBox.setSpacing(10)


        BtnBox = QHBoxLayout()
        Avanti_btn = QPushButton("Avanti")
        Reset_btn = QPushButton("Reset")
        BtnBox.addStretch(1)
        BtnBox.addWidget(Avanti_btn)
        BtnBox.addWidget(QLabel(' '))
        BtnBox.addWidget(Reset_btn)


        VBox.addWidget(lblHedr)
        VBox.addStretch(1)
        VBox.addLayout(GridBox)
        VBox.addStretch(1)
        VBox.addLayout(BtnBox)





        self.setLayout(VBox)



    @pyqtSlot()
    def NextPane(self):
        NextIdx = self.PaneIdx + 1
        self.CntrPane.Panes.setCurrentIndex(NextIdx)

    def UpdateView(self):
        pass

    def ProcessSdqData(self):
      # Okay collecting this back in the CenterPane so that they can be easily
      # accessible by each subsequent Pane as well as can the Main Window if
      # needed there

        self.CntrPane.SdqData = self.SdqItemList.ValuSet
      # Now we go to the next Pane
        NextPane = self.PaneIdx + 1
        self.CntrPane.UpdateNext(NextPane)

    def ResetSdqData(self):
      # This did not do anything but I put this place holder in place
      # to allow you to fill in what it supposed to do
        pass



'''
        HdrFont = QFont()
        HdrFont.setFamily("Times New Roman")
        HdrFont.setPointSize(18)
        HdrFont.setBold(True)
        HdrFont.setWeight(75)
        # -------NON SI VEDE! ->
        lblHedr = QLabel('Strenghts and Difficulties Questionnarire, S.D.Q.')
        lblHedr.setFont(HdrFont)
        lblHedr.setFixedWidth(200)
        lblHedr.setWordWrap(True)
        # -------
        hbxHedr = QHBoxLayout()
        hbxHedr.addStretch(1)
        hbxHedr.addWidget(lblHedr)
        hbxHedr.addStretch(1)

        self.SdqItemList = SdqItems(self)

        # -------
        self.scaSdqItems = QScrollArea()
        self.scaSdqItems.resize(170, 400)
        self.scaSdqItems.setMaximumWidth(165)
        self.scaSdqItems.setSizeIncrement(0, 0)
        self.scaSdqItems.setWidgetResizable(True)
        self.scaSdqItems.setWidget(self.SdqItemList)
        # -------
        #self.btnAvantiSdq = QPushButton('Avanti')
        #self.btnAvantiSdq.clicked.connect(self.ProcessSdqData)
        # -------
        #self.btnResetSdq = QPushButton('Reset')
        #self.btnResetSdq.clicked.connect(self.ResetSdqData)

        RitVBox = QVBoxLayout()
        RitVBox.addWidget(self.scaSdqItems)

        FullHBox = QVBoxLayout()
        FullHBox.addLayout(hbxHedr)
        FullHBox.addStretch(1)
        FullHBox.addLayout(RitVBox)

        self.setLayout(FullHBox)
'''


