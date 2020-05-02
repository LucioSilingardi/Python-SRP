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
        self.PaneIdx = 1

        HdrFont = QFont()
        HdrFont.setFamily("Times New Roman")
        HdrFont.setPointSize(18)
        HdrFont.setWeight(100)




        lblHedr = QLabel('Strenghts and Difficulties Questionnarire, S.D.Q.')
        lblHedr.setFont(HdrFont)





        GridBox = QGridLayout()


        x = 0
        y = 0
        idx = 0
        self.spin_dict = {}
        for n in range(1, 26):
            label = QLabel("Item " + str(n))
            label.setFixedWidth(50)
            #SpinBox = QSpinBox()
            #SpinBox.setMaximum(2)
            #SpinBox.setFixedWidth(50)
            GridBox.addWidget(label, x, y)
            y += 1
            if y == 6:
                x += 1
                y = 0
            idx += 1
            self.spin_dict[idx] = QSpinBox()

            self.spin_dict[idx].setMaximum(2)
            self.spin_dict[idx].setFixedWidth(50)
            GridBox.addWidget(self.spin_dict[idx], x, y)

            y += 1
            if y == 6:
                x += 1
                y = 0
        GridBox.setSpacing(10)









        BtnBox = QHBoxLayout()
        Avanti_btn = QPushButton("Avanti")
        Exit_btn = QPushButton("Exit")
        Exit_btn.clicked.connect(self.Exit)
        Avanti_btn.clicked.connect(self.ProcessSdqData)
        BtnBox.addStretch(1)
        BtnBox.addWidget(Avanti_btn)
        BtnBox.addWidget(QLabel(' '))
        BtnBox.addWidget(Exit_btn)

        VBox = QVBoxLayout()
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


        #---SALVARE I DATI!

        SDQ_values = {}
        for spinbox in self.spin_dict.keys():
          SDQ_values[spinbox] = self.spin_dict[spinbox].value()
        self.CntrPane.SdqData = SDQ_values

        #---Next panel
        NextPane = self.PaneIdx + 1
        self.CntrPane.UpdateNext(NextPane)


    def Exit(self):
      # This did not do anything but I put this place holder in place
      # to allow you to fill in what it supposed to do
        pass





