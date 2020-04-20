# python srp04OutputPane.py

from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton

import numpy as np

class OutputPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 3

        Font = QFont()
        Font.setPointSize(14)
        Font.setBold(True)
        
        lblTemp = QLabel('Output Panel')
        lblTemp.setFont(Font)

        HBox1 = QHBoxLayout()
        HBox1.addStretch(1)
        HBox1.addWidget(lblTemp)
        HBox1.addStretch(1)

        self.btnNext = QPushButton('Next')
        self.btnNext.clicked.connect(self.NextPane)

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
    def NextPane(self):
        NextIdx = self.PaneIdx + 1
        self.CntrPane.Panes.setCurrentIndex(NextIdx)

'''
    def open_window(self):

        self.show()
        self.sdq()
        self.psi()
        self.indici()
        
    def chiudi(self):
        print("close")
        window5.show()
        self.close()

    def sdq(self):
        print("sdq")
        sdq = list(window2.sdq_data())

        sdq[6] = 2-(sdq[6])
        sdq[10] = 2-(sdq[10])
        sdq[13] = 2-(sdq[13])
        sdq[20] = 2 - (sdq[20])
        sdq[24] = 2 - (sdq[24])

        SintomiEmozionali_g = sdq[2]+sdq[7]+sdq[12]+sdq[15]+sdq[23]
        ProblemiComportamento_g = sdq[4]+sdq[6]+sdq[11]+sdq[17]+sdq[21]
        IperattivitaDisattenzione_g = sdq[1]+sdq[9]+sdq[14]+sdq[20]+sdq[24]
        RapportoPari_g = sdq[5]+sdq[10]+sdq[13]+sdq[18]+sdq[22]
        ComportamentiProsociali_g = sdq[0]+sdq[3]+sdq[8]+sdq[16]+sdq[19]
        TotaleDifficolta_g = SintomiEmozionali_g+ProblemiComportamento_g+IperattivitaDisattenzione_g+RapportoPari_g

        if SintomiEmozionali_g < 6:
            SintomiEmozionali_p = "Normale"
        elif DistressGenitoriale_g == 6:
            DistressGenitoriale_p = "Caso limite"
        else:
            DistressGenitoriale_p = "Anormale"

        if ProblemiComportamento_g < 4:
            ProblemiComportamento_p = "Normale"
        elif ProblemiComportamento_g == 4:
            ProblemiComportamento_p = "Caso limite"
        else:
            ProblemiComportamento_p = "Anormale"

        if IperattivitaDisattenzione_g < 6:
            IperattivitaDisattenzione_p = "Normale"
        elif IperattivitaDisattenzione_g == 6:
            IperattivitaDisattenzione_p = "Caso Limite"
        else:
            IperattivitaDisattenzione_p = "Anormale"

        if RapportoPari_g < 4:
            RapportoPari_p = "Normale"
        elif RapportoPari_g == 4 or 5:
            RapportoPari_p = "Caso limite"
        else:
            RapportoPari_p = "Anormale"

        if ComportamentiProsociali_g < 5:
            ComportamentiProsociali_p = "Anormale"
        elif ComportamentiProsociali_g == 5:
            ComportamentiProsociali_p = "Caso limite"
        else:
            ComportamentiProsociali_p = "Normale"

        if TotaleDifficolta_g < 16:
            TotaleDifficolta_p = "Normale"
        elif TotaleDifficolta_g > 15 and TotaleDifficolta_g < 20:
            TotaleDifficolta_p = "Caso limite"
        else:
            TotaleDifficolta_p = "Anormale"

        Criticita_sdq = []
        Risorse_sdq = []
        tot_sdq = [SintomiEmozionali_p, ProblemiComportamento_p, IperattivitaDisattenzione_p, RapportoPari_p, ComportamentiProsociali_p, TotaleDifficolta_p]

        for scala in tot_sdq[:4]:
            if scala == "Anormale":
                Criticita_sdq.append(2)

            elif scala == "Caso limite":
                Criticita_sdq.append(0.5)

        for scala in tot_sdq[5]:
            if scala == "Anormale":
                Criticita_sdq.append(2)

            elif scala == "Caso limite":
                Criticita_sdq.append(0.5)

        for scala in tot_sdq[5:8]:
            if scala == "Normale":
                Risorse_sdq.append(2)

        ##Scale da usare: Risorse_sdq e Criticita_sdq, sono liste con dentro i singoli valori di risorse e criticità.
        #NPIA Sintomi emozionali, Problemi Comportamento, Iperattivita Disatt.
        NPIA_sdq = []
        for data in tot_sdq[:4]:
            if data == "Anormale":
                NPIA_sdq.append(1)
            else:
                NPIA_sdq.append(0)

        ##self.psi()
        return Criticita_sdq, Risorse_sdq, NPIA_sdq

    def psi(self):
        print("psi")
        psig = list(window.psi_data()) #lista con dati, anni, nome e cognome derivante dall'input del psi
        psi = list(psig[0])
        age = int(psig[1])
        nome = str(psig[2])
        cognome = str(psig[3])

        psi_num = []

        ##item 22 e 32 da 5 a 1, item 33 da 1 a 10
        #prima sostituisco tutti gli FA ecc in numeri.
        for item in psi:

            if item == "FA":
                psi_num.append(5)
            elif item == "A":
                psi_num.append(4)
            elif item == "I":
                   psi_num.append(3)
            elif item == "D":
                psi_num.append(2)
            elif item == "FD":
                    psi_num.append(1)
            else:
                psi_num.append(item)

  ##poi creo una lista fatta dai punteggi tradotti dei reverse, e gli inverto il punteggio
        psi_reverse = list([psi_num[21],psi_num[31]])
        psi_reverse_2 = []

        for item in psi_reverse:
            if item == "5":
                psi_reverse_2.append(1)
            elif item == "4":
                psi_reverse_2.append(2)
            elif item == "3":
                psi_reverse_2.append(3)
            elif item == "2":
                psi_reverse_2.append(4)
            elif item == "1":
                psi_reverse_2.append(5)

        ##sostituisco i due item normali con la loro versione reverse
        psi_num[21] = psi_reverse_2[0]
        psi_num[31] = psi_reverse_2[1]
        psi_num[-4] = int(psi_num[-4])
        psi_num = np.array(psi_num)

        ##ora calcolo le scale in grezzo:
        DistressGenitoriale_g = np.sum(psi_num[0:12])
        InterazioneDisfunzionale_g = np.sum(psi_num[12:24])
        BambinoDifficile_g = np.sum(psi_num[24:36])
        RispostaDifensiva_g = np.sum(psi_num[:3] + psi_num[6:9] + psi_num[10])
        RispostaDifensiva_g = np.sum(RispostaDifensiva_g)
        StressTotale_g = DistressGenitoriale_g + BambinoDifficile_g + InterazioneDisfunzionale_g
        StressTotale_g = np.sum(StressTotale_g)

        ##Soglie di confronto percentili del psi:
        ##Si potrebbe selezionare proprio il tipo di test (0-3, 3-6 ecc...) cambiando le opzioni dalla gui.
        if age < 3:
            if DistressGenitoriale_g > 34:
                DistressGenitoriale_p = "Anormale ALTO"
            elif DistressGenitoriale_g < 18:
                DistressGenitoriale_p = "Anormale BASSO"
            else:
                DistressGenitoriale_p = "Normale"

            if InterazioneDisfunzionale_g > 25:
                InterazioneDisfunzionale_p = "Anormale ALTO"
            elif InterazioneDisfunzionale_g < 14:
                InterazioneDisfunzionale_p = "Anormale BASSO"
            else:
                InterazioneDisfunzionale_p = "Normale"

            if BambinoDifficile_g > 28:
                BambinoDifficile_p = "Anormale ALTO"
            elif BambinoDifficile_g < 15:
                BambinoDifficile_p = "Anormale BASSO"
            else:
                BambinoDifficile_p = "Normale"

            if RispostaDifensiva_g > 20:
                RispostaDifensiva_p = "Anormale ALTO"
            elif RispostaDifensiva_g < 11:
                RispostaDifensiva_p = "Anormale BASSO"
            else:
                RispostaDifensiva_p = "Normale"

            if StressTotale_g > 84:
                StressTotale_p = "Anormale ALTO"
            elif StressTotale_g < 50:
                StressTotale_p = "Anormale BASSO"
            else:
                StressTotale_p = "Normale"

        elif age > 2 and  window.anni_psi < 6:
            if DistressGenitoriale_g > 34:
                DistressGenitoriale_p = "Anormale ALTO"
            elif DistressGenitoriale_g < 20:
                DistressGenitoriale_p = "Anormale BASSO"
            else:
                DistressGenitoriale_p = "Normale"

            if InterazioneDisfunzionale_g > 27:
                InterazioneDisfunzionale_p = "Anormale ALTO"
            elif InterazioneDisfunzionale_g < 14:
                InterazioneDisfunzionale_p = "Anormale BASSO"
            else:
                InterazioneDisfunzionale_p = "Normale"

            if BambinoDifficile_g > 32:
                BambinoDifficile_p = "Anormale ALTO"
            elif BambinoDifficile_g < 17:
                BambinoDifficile_p = "Anormale BASSO"
            else:
                BambinoDifficile_p = "Normale"

            if RispostaDifensiva_g > 20:
                RispostaDifensiva_p = "Anormale ALTO"
            elif RispostaDifensiva_g < 12:
                RispostaDifensiva_p = "Anormale BASSO"
            else:
                RispostaDifensiva_p = "Normale"


            if StressTotale_g > 91:
                StressTotale_p = "Anormale ALTO"
            elif StressTotale_g < 53:
                StressTotale_p = "Anormale BASSO"
            else:
                StressTotale_p = "Normale"

        elif age > 5 and age < 9:
            if DistressGenitoriale_g > 30:
                DistressGenitoriale_p = "Anormale ALTO"
            elif DistressGenitoriale_g < 16:
                DistressGenitoriale_p = "Anormale BASSO"
            else:
                DistressGenitoriale_p = "Normale"

            if InterazioneDisfunzionale_g > 25:
                InterazioneDisfunzionale_p = "Anormale ALTO"
            elif InterazioneDisfunzionale_g < 14:
                InterazioneDisfunzionale_p = "Anormale BASSO"
            else:
                InterazioneDisfunzionale_p = "Normale"

            if BambinoDifficile_g > 30:
                BambinoDifficile_p = "Anormale ALTO"
            elif BambinoDifficile_g < 17:
                BambinoDifficile_p = "Anormale BASSO"
            else:
                BambinoDifficile_p = "Normale"

            if RispostaDifensiva_g > 18:
                RispostaDifensiva_p = "Anormale ALTO"
            elif RispostaDifensiva_g < 9:
                RispostaDifensiva_p = "Anormale BASSO"
            else:
                RispostaDifensiva_p = "Normale"


            if StressTotale_g > 84:
                StressTotale_p = "Anormale ALTO"
            elif StressTotale_g < 49:
                StressTotale_p = "Anormale BASSO"
            else:
                StressTotale_p = "Normale"

        else:
            if DistressGenitoriale_g > 32:
                DistressGenitoriale_p = "Anormale ALTO"

            elif DistressGenitoriale_g < 15:
                DistressGenitoriale_p = "Anormale BASSO"
            else:
                DistressGenitoriale_p = "Normale"

            if InterazioneDisfunzionale_g > 25:
                InterazioneDisfunzionale_p = "Anormale ALTO"
            elif InterazioneDisfunzionale_g < 14:
                InterazioneDisfunzionale_p = "Anormale BASSO"
            else:
                InterazioneDisfunzionale_p = "Normale"

            if BambinoDifficile_g > 30:
                BambinoDifficile_p = "Anormale ALTO"
            elif BambinoDifficile_g < 15:
                BambinoDifficile_p = "Anormale BASSO"
            else:
                BambinoDifficile_p = "Normale"


            if RispostaDifensiva_g > 20:
                RispostaDifensiva_p = "Anormale ALTO"
            elif RispostaDifensiva_g < 8:
                RispostaDifensiva_p = "Anormale BASSO"
            else:
                RispostaDifensiva_p = "Normale"


            if StressTotale_g > 87:
                StressTotale_p = "Anormale ALTO"
            elif StressTotale_g < 45:
                StressTotale_p = "Anormale BASSO"
            else:
                StressTotale_p = "Normale"

        Criticita_psi = []
        Risorse_psi = []
        tot_psi = [DistressGenitoriale_p, InterazioneDisfunzionale_p, BambinoDifficile_p]
        if RispostaDifensiva_p == "Anormale ALTO":
            Risorse_psi.append(1)
        else:
            Risorse_psi.append(0)


        if StressTotale_p == "Anormale ALTO":
            Criticita_psi.append(2)
        else:
            Criticita_psi.append(0)

        for scala in tot_psi:
            if scala == "Anormale ALTO":
                Criticita_psi.append(0.5)
            else:
                Criticita_psi.append(0)

        NPIA_psi = []
        for data in tot_psi[2]:
            if data == "Anormale ALTO":
                NPIA_psi.append(1)
            else:
                NPIA_psi.append(0)
        Consultorio_psi = []
        for data in tot_psi[:2]:
            if data == "Anormale ALTO":
                Consultorio_psi.append(1)
            else:
                Consultorio_psi.append(0)

        ##self.indici()
        return  Criticita_psi, Risorse_psi, NPIA_psi, Consultorio_psi

    def indici(self):
        print("indici")
        indici_data = list(window3.indici_data())
        Criticita_indici = []
        Risorse_indici = []

        return Criticita_indici, Risorse_indici
'''
'''

        for data in indici_data[:11]:
            if data == "Presente":
                Criticita_indici.append(1)
            elif data == "Non rilevato":
                Criticita_indici.append(0.5)
            else:
                Criticita_indici.append(0)
        for data in indici_data[11:25]:
            if data == "Presente":
                Criticita_indici.append(2)
            elif data == "Non rilevato":
                Criticita_indici.append(1)
            else:
                Criticita_indici.append(0)
        for data in indici_data[25:35]:
            if data == "Presente":
                Risorse_indici.append(2)
            else:
                Risorse_indici.append(0)

        Servizi_sociali_indici = [] #[0,2,6,7,8,9,10,13,14,21,22]
        Psi_cli_adulti_indici = [] #[3,6,11,12,16,17,18,21]
        Intervento_giudiziario_indici = [] #[9,12]
        NPIA_indici = [] #[23,24]
        Consultorio_indici = [] #[2,3,5,7,8,10,**13 errore?**,14,16,18,19,20,21,24]
        CSM_indici = [] #[11,**17 errore?**
        SERT_indici = [] #[13]
        LDV_indici = [] #[8,22]

        #for data in indici_data[0],[2],[13],[14],[21],[24]:
        #    if data == "Presente":
        #        Servizi_sociali_indici.append(1)
        #    else:
      #        Servizi_sociali_indici.append(0)
'''
