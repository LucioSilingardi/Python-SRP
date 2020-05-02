# python srp04OutputPane.py

from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtWidgets import QLabel, QPushButton

import numpy as np



class OutputPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.CntrPane = parent
        self.PaneIdx = 3

        Font_titl = QFont()
        Font_titl.setPointSize(10)
        Font_titl.setBold(True)

        Font_norm = QFont()
        Font_norm.setPointSize(8)
        #--Titolo label
        empty_lbl_1 = QLabel(" ")
        empty_lbl_1.setFixedHeight(50)
        empty_lbl_2 = QLabel(" ")
        empty_lbl_2.setFixedHeight(50)
        scr_rslts_lbl = QLabel("SCORING E RISULTATI")
        scr_rslts_lbl.setFont(Font_titl)
        scr_rslts_lbl.setFixedHeight(50)
        #--Utente labels
        paz_titl_lbl = QLabel("Utente")
        paz_titl_lbl.setFont(Font_titl)
        paz_nome_lbl = QLabel("Nome: ")
        paz_nome_lbl.setFont(Font_norm)
        paz_cognome_lbl = QLabel("Cognome: ")
        paz_cognome_lbl.setFont(Font_norm)
        paz_anni_lbl = QLabel("Anni: ")
        paz_anni_lbl.setFont(Font_norm)
        #--PSI labels
        psi_lbl = QLabel("P.S.I., Parenting Stress Index")
        psi_lbl.setFont(Font_titl)
        distress_gen_lbl = QLabel("Distress genitoriale: ")
        distress_gen_lbl.setFont(Font_norm)
        int_disf_lbl = QLabel("Interazione gen/bamb disfunzionale: ")
        int_disf_lbl.setFont(Font_norm)
        bamb_dif_lbl = QLabel("Bambino difficile: ")
        bamb_dif_lbl.setFont(Font_norm)
        risp_dif_lbl = QLabel("Risposta difensiva: ")
        risp_dif_lbl.setFont(Font_norm)
        stress_tot_lbl = QLabel("Stress totale: ")
        stress_tot_lbl.setFont(Font_norm)
        #--SDQ labels
        sdq_lbl = QLabel("S.D.Q., Strenghts and Difficulties Questionnaire")
        sdq_lbl.setFont(Font_titl)
        sint_emoz_lbl = QLabel("Sintomi emozionali: ")
        sint_emoz_lbl.setFont(Font_norm)
        prob_comp_lbl = QLabel("Problemi di comportamento: ")
        prob_comp_lbl.setFont(Font_norm)
        iperat_dis_lbl = QLabel("Iperattivita/disattenzione: ")
        iperat_dis_lbl.setFont(Font_norm)
        rapp_pari_lbl = QLabel("Rapporto con i pari: ")
        rapp_pari_lbl.setFont(Font_norm)
        comp_pro_lbl = QLabel("Comportamenti prosociali: ")
        comp_pro_lbl.setFont(Font_norm)
        tot_diff_lbl = QLabel("Totale difficoltà: ")
        tot_diff_lbl.setFont(Font_norm)
        #--Servizi labels
        servizi_lbl =QLabel("Servizi consigliati")
        servizi_lbl.setFont(Font_titl)
        servizi_soc_lbl = QLabel("Servizi sociali: ")
        servizi_soc_lbl.setFont(Font_norm)
        psi_cli_adu_lbl = QLabel("Psicologia clinica adulti: ")
        psi_cli_adu_lbl.setFont(Font_norm)
        int_giud_lbl = QLabel("Intervento giudiziario: ")
        int_giud_lbl.setFont(Font_norm)
        npia_lbl = QLabel("NPIA: ")
        npia_lbl.setFont(Font_norm)
        consult_lbl = QLabel("Consultorio: ")
        consult_lbl.setFont(Font_norm)
        csm_lbl = QLabel("CSM: ")
        csm_lbl.setFont(Font_norm)
        sert_lbl = QLabel("SERT: ")
        sert_lbl.setFont(Font_norm)
        ldv_lbl = QLabel("LDV: ")
        ldv_lbl.setFont(Font_norm)

        #--Buttons
        grafici_btn = QPushButton("Grafici")
        ext_btn = QPushButton("Exit")
        empty_lbl = QLabel(" ")

        #--Layouts
        Vlayout = QVBoxLayout()
        Form = QFormLayout()
        Buttons = QHBoxLayout()
        Titl_lyt = QHBoxLayout()

        #--Positioning
        Vlayout.addLayout(Titl_lyt)
        Vlayout.addLayout(Form)
        Vlayout.addLayout(Buttons)

        # --Output's instances for Labels
        nome = self.calc.nome
        nome_otp = QLabel(nome)
        nome_otp.setFont(Font_norm)

        #--Positioning Form Layout
        Form.addRow(paz_titl_lbl)
        Form.addRow(paz_nome_lbl, nome_otp)
        Form.addRow(paz_cognome_lbl)
        Form.addRow(paz_anni_lbl)
        Form.addRow(psi_lbl)
        Form.addRow(distress_gen_lbl)
        Form.addRow(int_disf_lbl)
        Form.addRow(bamb_dif_lbl)
        Form.addRow(risp_dif_lbl)
        Form.addRow(stress_tot_lbl)
        Form.addRow(sdq_lbl)
        Form.addRow(sint_emoz_lbl)
        Form.addRow(prob_comp_lbl)
        Form.addRow(iperat_dis_lbl)
        Form.addRow(rapp_pari_lbl)
        Form.addRow(comp_pro_lbl)
        Form.addRow(tot_diff_lbl)
        Form.addRow(servizi_lbl)
        Form.addRow(servizi_soc_lbl)
        Form.addRow(psi_cli_adu_lbl)
        Form.addRow(int_giud_lbl)
        Form.addRow(npia_lbl)
        Form.addRow(consult_lbl)
        Form.addRow(csm_lbl)
        Form.addRow(sert_lbl)
        Form.addRow(ldv_lbl)


        #--Positioning Buttons Layout
        Buttons.addStretch(1)
        Buttons.addWidget(grafici_btn)
        Buttons.addWidget(empty_lbl)
        Buttons.addWidget(ext_btn)

        #--Positioning Title Layout
        Titl_lyt.addWidget(empty_lbl_1)
        Titl_lyt.addWidget(scr_rslts_lbl)
        Titl_lyt.addWidget(empty_lbl_2)







        self.setLayout(Vlayout)












        


        #self.btnNext = QPushButton('Next')
        #self.btnNext.clicked.connect(self.NextPane)






    def calc(self):
        age = self.CntrPane.Age
        self.nome = self.CntrPane.Nome
        cognome = self.CntrPane.Cognome
        psi_raw = self.CntrPane.PsiData
        sdq_raw = self.CntrPane.SdqData
        indici_raw = self.CntrPane.IndiciData

        #---PSI---
        #Item reverse: 22, 32. Item particolare 33.
        psi = list(psi_raw.values()) #converte i valori del dizionario in una lista di valori

        psi_num = []

        # item 22 e 32 da 5 a 1, item 33 da 1 a 10
        # prima sostituisco tutti gli FA ecc in numeri.
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
            elif item == "10+":
                psi_num.append(5)
            elif item == "8-9":
                psi_num.append(4)
            elif item == "6-7":
                psi_num.append(3)
            elif item == "4-5":
                psi_num.append(2)
            elif item == "1-3":
                psi_num.append(1)
            else:
                psi_num.append(int(item))

        ##poi creo una lista fatta dai punteggi tradotti dei reverse, e gli inverto il punteggio
        psi_reverse = list([psi_num[21], psi_num[31]])
        psi_reverse_2 = []


        for item in psi_reverse:
            if item == 5:
                psi_reverse_2.append(1)
            elif item == 4:
                psi_reverse_2.append(2)
            elif item == 3:
                psi_reverse_2.append(3)
            elif item == 2:
                psi_reverse_2.append(4)
            elif item == 1:
                psi_reverse_2.append(5)


        ##sostituisco i due item normali con la loro versione reverse
        psi_num[21] = psi_reverse_2[0]
        psi_num[31] = psi_reverse_2[1]
        psi_num[-4] = int(psi_num[-4])


        ##ora calcolo le scale in grezzo:
        DistressGenitoriale_g = sum(psi_num[0:12])
        InterazioneDisfunzionale_g = sum(psi_num[12:24])
        BambinoDifficile_g = np.sum(psi_num[24:36])
        RispostaDifensiva_g = sum(list([sum(psi_num[:3]), sum(psi_num[6:9]), psi_num[10]]))
        StressTotale_g = sum(list([DistressGenitoriale_g, BambinoDifficile_g, InterazioneDisfunzionale_g]))

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




        elif age > 2 and age < 6:
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

        #Calcolo criticita e risorse del PSI
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


        #---SDQ---
        sdq = list(sdq_raw.values())
        sdq[6] = 2 - (sdq[6])
        sdq[10] = 2 - (sdq[10])
        sdq[13] = 2 - (sdq[13])
        sdq[20] = 2 - (sdq[20])
        sdq[24] = 2 - (sdq[24])

        SintomiEmozionali_g = sdq[2] + sdq[7] + sdq[12] + sdq[15] + sdq[23]
        ProblemiComportamento_g = sdq[4] + sdq[6] + sdq[11] + sdq[17] + sdq[21]
        IperattivitaDisattenzione_g = sdq[1] + sdq[9] + sdq[14] + sdq[20] + sdq[24]
        RapportoPari_g = sdq[5] + sdq[10] + sdq[13] + sdq[18] + sdq[22]
        ComportamentiProsociali_g = sdq[0] + sdq[3] + sdq[8] + sdq[16] + sdq[19]
        TotaleDifficolta_g = SintomiEmozionali_g + ProblemiComportamento_g + IperattivitaDisattenzione_g + RapportoPari_g

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
        tot_sdq = [SintomiEmozionali_p, ProblemiComportamento_p, IperattivitaDisattenzione_p, RapportoPari_p,
                   ComportamentiProsociali_p, TotaleDifficolta_p]

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
        # NPIA Sintomi emozionali, Problemi Comportamento, Iperattivita Disatt.
        NPIA_sdq = []
        for data in tot_sdq[:4]:
            if data == "Anormale":
                    NPIA_sdq.append(1)
            else:
                    NPIA_sdq.append(0)


        #---INDICI---
        #Servizi sociali
        Servizi_sociali_items = [1,2,7,8,9,10,11,13,15,22,23]
        servizi_sociali_indici = []
        for idx in Servizi_sociali_items:
            if indici_raw[idx] == "Presente":
                servizi_sociali_indici.append(1)
            else:
                servizi_sociali_indici.append(0)

        servizi_sociali_indici = sum(servizi_sociali_indici)
        servizi_sociali = servizi_sociali_indici

        #Psicologia clinica adulti
        PsiCliAdu_items = [4,7,12,13,17,18,19,22]
        psicliadu_indici = []
        for idx in PsiCliAdu_items:
            if indici_raw[idx] == "Presente":
                psicliadu_indici.append(1)
            else:
                psicliadu_indici.append(0)

        psi_cli_adu = sum(psicliadu_indici)


        #Intervento giudiziario
        Int_giu_items = [10,13]
        intgiu_indici = []
        for idx in Int_giu_items:
            if indici_raw[idx] == "Presente":
                intgiu_indici.append(1)
            else:
                intgiu_indici.append(0)
        int_giud = sum(intgiu_indici)

        #NPIA
        Npia_items = [24,25]
        npia_indici = []
        for idx in Npia_items:
            if indici_raw[idx] == "Presente":
                npia_indici.append(1)
            else:
                npia_indici.append(0)
        npia_indici = sum(npia_indici)
        NPIA_sdq = sum(NPIA_sdq)
        NPIA_psi = sum(NPIA_psi)

        NPIA = sum(list([NPIA_psi, NPIA_sdq, npia_indici]))

        #Consultorio
        Consult_items = [3,4,6,8,9,11,14,15,17,19,20,21,22,25]
        consult_indici = []
        for idx in Consult_items:
            if indici_raw[idx] == "Presente":
                consult_indici.append(1)
            else:
                consult_indici.append(0)
        consult_indici = sum(consult_indici)
        Consultorio_psi = sum(Consultorio_psi)
        Consultorio = sum(list([consult_indici, Consultorio_psi]))

        #CSM
        CSM_items = [12,18,17]
        csm_indici = []
        for idx in CSM_items:
            if indici_raw[idx] == "Presente":
                csm_indici.append(1)
            else:
                csm_indici.append(0)
        CSM = sum(csm_indici)

        #SERT
        SERT_items = [14]
        sert_indici = []
        for idx in SERT_items:
            if indici_raw[idx] == "Presente":
                sert_indici.append(1)
            else:
                sert_indici.append(0)
        SERT = sum(sert_indici)

        #LDV
        LDV_items = [9,23]
        ldv_indici = []
        for idx in LDV_items:
            if indici_raw[idx] == "Presente":
                ldv_indici.append(1)
            else:
                ldv_indici.append(0)
        LDV = sum(ldv_indici)

        #Calcolo criticita e risorse INDICI

        Rischio_distali_items = [1,2,3,4,5,6,7,8,9,10,11]
        rischio_distali_indici = []
        for idx in Rischio_distali_items:
            if indici_raw[idx] == "Presente":
                rischio_distali_indici.append(1)
            elif indici_raw[idx] == "Non rilevato":
                rischio_distali_indici.append(0.5)
            else:
                rischio_distali_indici.append(0)

        Rischio_prossimali_items = [12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        rischio_prossimali_indici = []
        for idx in Rischio_prossimali_items:
            if indici_raw[idx] == "Presente":
                rischio_prossimali_indici.append(2)
            elif indici_raw[idx] == "Non rilevato":
                rischio_prossimali_indici.append(1)
            else:
                rischio_prossimali_indici.append(0)
        rischio_distali_indici = sum(rischio_distali_indici)
        rischio_prossimali_indici = sum(rischio_prossimali_indici)

        Criticita_indici = sum(list([rischio_prossimali_indici, rischio_distali_indici]))

        Protettivi_prossimali_items = [26,27,28,29,30,31,32,33,34,35,36]
        protettivi_prossimali_indici = []
        for idx in Protettivi_prossimali_items:
            if indici_raw[idx] == "Presente":
                protettivi_prossimali_indici.append(2)
            else:
                protettivi_prossimali_indici.append(0)

        Risorse_indici = sum(protettivi_prossimali_indici)

        #---Risorse e criticita TOTALI---

        Risorse_psi = float(Risorse_psi[0])
        Risorse_sdq = float(Risorse_sdq[0])


        Risorse_tot = sum([Risorse_psi,Risorse_sdq,Risorse_indici])


        Criticita_psi = float(sum(Criticita_psi))
        Criticita_sdq = float(sum(Criticita_sdq))

        Criticita_tot = sum([Criticita_psi,Criticita_sdq,Criticita_indici])

        return nome



















    @pyqtSlot()
    def NextPane(self):
        NextIdx = self.PaneIdx + 1
        self.CntrPane.Panes.setCurrentIndex(NextIdx)




