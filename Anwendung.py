import Buffer
import FragenHandler
import fragenEinlesen
from Spieler import Spieler
from time import*
import time
class Anwendung():
    def __init__(self,Buff,Ausgabe,Buff2):

        self.__ListeSpieler =[]
        #self.__ListeFragen = [["normal", "wie heißt das Quiz?", ["super", "PQuiz", "TQuiz", "toll"],1],
        #                      ["normal", "wie heißt das Quiz23?", ["super", "PQuiz", "TQuiz", "toll"],3],
        #                      ["schaetzen", "Wie groß bin ich?",230 ],
        #                      ["normal", "Wer bin ich??", ["2super", "2PQuiz", "2TQuiz", "2toll"],2],
        #                      ["sortier", "wie heißt das Quiz?", ["i", "P", "z", "Qu"],[2,4,1,3]]]
        self.__ListeFragen = []
        self.__aFrag = -1
        self.__neueFrage = True
        self.__neueFrage2 = True
        Ausgabe.ak_Frage.insert(0,"0")
        while True:
            #time.sleep(1)
            VonClient = Buff.BufINget()
            #print(VonClient)
            if VonClient!=None:
                print("mh")
                ClientNvor = True
                if ClientNvor: #Client kann nur einer Gruppe zugeordnet werden, wenn er nicht schon einer Gruppe zugewiedsen ist
                    GruppeNvorh = True
                    for Typ in self.__ListeSpieler:
                        if VonClient[1] == Typ.Gruppe:#Prüft ob die gewünschte Gruppe existiert
                            GruppeNvorh = False
                            if Typ.Aktiv == False:
                                Typ.Aktiv = True
                                #Typ.Server = VonClient[0]
                                    #if (self.__aFrag!= -1 and Typ.aktuelleAntwort == 0): #Wenn er mitten in einer Frage abschmiert
                                    #    ZwisString = ""
                                    #    if self.__ListeFragen[self.__aFrag][0] == "normal":
                                    #        ZwisString = self.__ListeFragen[self.__aFrag][2][0]+"#" + self.__ListeFragen[self.__aFrag][2][1]+"#" + self.__ListeFragen[self.__aFrag][2][2]+"#" + self.__ListeFragen[self.__aFrag][2][3]
                                    #    if self.__ListeFragen[self.__aFrag][0] == "sortier":
                                    #        ZwisString = self.__ListeFragen[self.__aFrag][2][0]+"#" + self.__ListeFragen[self.__aFrag][2][1]+"#" + self.__ListeFragen[self.__aFrag][2][2]+"#" + self.__ListeFragen[self.__aFrag][2][3]
                                    #    Buff.BufOUTset(Typ.Server,"server:#" + self.__ListeFragen[self.__aFrag][0] + "#" +self.__ListeFragen[self.__aFrag][1] + "#" + ZwisString)
                                self.Gruppenakk(Buff2,Ausgabe)
                    if GruppeNvorh: #Nur neue Gruppe erstellen falls sie noch nicht existiert
                        Akksp = Spieler(VonClient[1])
                        self.__ListeSpieler.append(Akksp)
                        self.Gruppenakk(Buff2,Ausgabe)
                        print("Gruppe hinzugefügt")
                for Typ in self.__ListeSpieler:
                    if Typ.Gruppe == VonClient[1]:
                        ClientNvor == False
                        #if VonClient[1] == "Verbindung unterbrochen":
                        #    Typ.Aktiv = False
                        #    self.Gruppenakk(Buff2,Ausgabe)
                        #########
                        #Antwort von client:# antwort#(bei normal 1 = a usw., b)
                        print("Gruppe "+ Typ.Gruppe + " sendet "+VonClient[1])
                        Typ.Endzeit = time.perf_counter()
                        Typ.Zeit = Typ.Endzeit - t1
                        try:
                            if VonClient[2][0]==0:
                                pass
                            elif self.__ListeFragen[self.__aFrag][0] == "sortier":
                                Typ.aktuelleAntwort=[0,0,0,0]
                                for i in range(4):
                                    if VonClient[2][0+i] == "a":
                                        Typ.aktuelleAntwort[i]=1
                                    elif VonClient[2][0+i] == "b":
                                        Typ.aktuelleAntwort[i]=2
                                    elif VonClient[2][0+i] == "c":
                                        Typ.aktuelleAntwort[i]=3
                                    elif VonClient[2][0+i] == "d":
                                        Typ.aktuelleAntwort[i]=4
                                    self.Gruppenakk(Buff2,Ausgabe)
                            else:
                                if VonClient[2][0] == "a":
                                    Typ.aktuelleAntwort=1
                                elif VonClient[2][0] == "b":
                                    Typ.aktuelleAntwort=2
                                elif VonClient[2][0] == "c":
                                    Typ.aktuelleAntwort=3
                                elif VonClient[2][0] == "d":
                                    Typ.aktuelleAntwort=4
                                else:
                                    try:
                                        Typ.aktuelleAntwort=int(VonClient[2][0:])
                                        print(int(VonClient[2][0:]))
                                        self.Gruppenakk(Buff2,Ausgabe)
                                    except:
                                        pass
                                self.Gruppenakk(Buff2,Ausgabe)
                            self.Gruppenakk(Buff2,Ausgabe)
                        except:
                            pass
                        #if VonClient[1][0]=="/":
                        #    Buff.BufOUTset(0,"Gruppe "+Typ.Gruppe+" sendet " + VonClient[1][1:])
                        #else:
                        #    Buff.BufOUTset(VonClient[0],"Gruppe "+Typ.Gruppe+" sendet " + VonClient[1])
                        ########

            """
                Änderung übernehmen
            """
            self.__Gruppenaenderung = Ausgabe.Gruppenae()
            if self.__Gruppenaenderung!=True:
                try:
                    if self.__Gruppenaenderung[4]:
                        self.__ListeSpieler.pop(self.__Gruppenaenderung[0])
                        self.Gruppenakk(Buff2,Ausgabe)
                    if self.__Gruppenaenderung[1]>-1:
                        self.__ListeSpieler[self.__Gruppenaenderung[0]].aktuelleAntwort = self.__Gruppenaenderung[1]
                    if self.__Gruppenaenderung[2]>-1:
                        self.__ListeSpieler[self.__Gruppenaenderung[0]].Punkte = self.__Gruppenaenderung[2]
                    if self.__Gruppenaenderung[3]:
                        if self.__ListeSpieler[self.__Gruppenaenderung[0]].Aktiv:
                            self.__ListeSpieler[self.__Gruppenaenderung[0]].Aktiv = False
                        else:
                            self.__ListeSpieler[self.__Gruppenaenderung[0]].Aktiv = True
                except:
                    pass
                self.Gruppenakk(Buff2,Ausgabe)

            """
                In diesem Abschnitt wird jeweils eine neue Frage gesendet
            """

            if Ausgabe.getFrage():
                print("1")
                Ausgabe.setFrageF()
                if self.__neueFrage:
                    print("2")
                    self.__ListeFragen = Ausgabe.holeFragen()
                    if self.__ListeFragen != []:
                        print("3")
                        self.Gruppenakk(Buff2,Ausgabe)
                        Buff2.set__LoesungAnzeigen(False)
                        if Ausgabe.neFrag:
                            Ausgabe.neFrag=False
                            self.__aFrag=Ausgabe.Frage-1
                        self.__aFrag = self.__aFrag+1
                        #leseEingabe = fragenEinlesen.lesen()
                        #liste_Fragen = leseEingabe.fragen_einlesen(name)
                        fragenHandler = FragenHandler.FragenHandler(self.__ListeFragen)
                        fragenHandler.readMessage(self.__ListeFragen[self.__aFrag])
                        Ausgabe.ak_Frage.delete(0,'end')
                        Ausgabe.ak_Frage.insert(0,str(self.__aFrag+1))
                        #ZwisString = ""
                        try:
                            #if self.__ListeFragen[self.__aFrag][0] == "normal":
                            #    ZwisString = self.__ListeFragen[self.__aFrag][2][0]+"#" + self.__ListeFragen[self.__aFrag][2][1]+"#" + self.__ListeFragen[self.__aFrag][2][2]+"#" + self.__ListeFragen[self.__aFrag][2][3]
                            #if self.__ListeFragen[self.__aFrag][0] == "sortier":
                            #    ZwisString = self.__ListeFragen[self.__aFrag][2][0]+"#" + self.__ListeFragen[self.__aFrag][2][1]+"#" + self.__ListeFragen[self.__aFrag][2][2]+"#" + self.__ListeFragen[self.__aFrag][2][3]
                            #Buff.BufOUTset(0,"server:#" + self.__ListeFragen[self.__aFrag][0] + "#" +self.__ListeFragen[self.__aFrag][1] + "#" + ZwisString)
                            self.__neueFrage = False
                            Buff2.setFrage(self.__ListeFragen[self.__aFrag])
                            t1 = time.perf_counter()
                        except:
                            pass

            """
                 In diesem Abschnitt wird die Lösung angezeigt
            """
            if Ausgabe.getLoAn():

                Ausgabe.LoAnF()
                self.__neueFrage2 = True
                for Typ in self.__ListeSpieler: #Wenn alle Spiler die Frage beantwortet haben bleibt neue Fragen Ture
                   if (Typ.aktuelleAntwort == 0 and Typ.Aktiv):#Sonst wird es hier False gestezt
                       self.__neueFrage2 = False
                if (self.__neueFrage2 or self.__neueFrage):
                    Buff2.set__LoesungAnzeigen(True)

            """
                 In diesem Abschnitt werden dei Anworten ausgewertet wenn alle eine Anwort abgegeben haben
            """
            if Ausgabe.getWeiter():
                Ausgabe.weiterF()
                self.__neueFrage = True
                for Typ in self.__ListeSpieler: #Wenn alle Spiler die Frage beantwortet haben bleibt neue Fragen True
                   if (Typ.aktuelleAntwort == 0 and Typ.Aktiv):#Sonst wird es hier False gestezt
                       self.__neueFrage = False
                if self.__neueFrage:
                    zeitliste = []
                    for Typ in self.__ListeSpieler:
                        try:
                            zeitliste.append(Typ.Zeit)
                        except:
                            pass
                    try:
                        zeitliste.sort()
                    except:
                        pass
                    for Typ in self.__ListeSpieler:
                        try:
                            for i in len(self.__ListeSpieler):
                                if Typ.Zeit == zeitliste[i]:
                                    Typ.position = i
                        except:
                            pass
                        if len(self.__ListeFragen)>0:
                            if self.__ListeFragen[self.__aFrag][0] == "normal":
                                if Typ.aktuelleAntwort == self.__ListeFragen[self.__aFrag][3]:#Wenn der Spieler die Frage Richtig beantwortet hat
                                    try:
                                        try:
                                            if self.__ListeFragen[self.__aFrag][4] == "Zeit":
                                                if Typ.position == 0:
                                                    Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_normal1.get())
                                                if Typ.position == 1:
                                                    Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_normal2.get())
                                            else:
                                                Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_normal.get())
                                        except:
                                            Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_normal.get())
                                    except:
                                        pass
                            elif self.__ListeFragen[self.__aFrag][0] == "schaetzen":
                                Sieger=2
                                for Typ2 in self.__ListeSpieler: #Ermittelt den Sieger wer am nächsten zur Lösung gelegen ist
                                    if Typ.Gruppe != Typ2.Gruppe:
                                        if abs(Typ.aktuelleAntwort-self.__ListeFragen[self.__aFrag][2])>abs(Typ2.aktuelleAntwort-self.__ListeFragen[self.__aFrag][2]):
                                            Sieger=Sieger-1
                                if Sieger==2:
                                    try:
                                        Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_schaetzen.get())
                                    except:
                                        pass
                                if Sieger==1:
                                    try:
                                        Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_schaetzen2.get())
                                    except:
                                        pass
                            elif self.__ListeFragen[self.__aFrag][0] == "sortier":
                                if Typ.aktuelleAntwort == self.__ListeFragen[self.__aFrag][3]:#Wenn der Spieler die Frage Richtig beantwortet hat
                                    try:
                                        try:
                                            if self.__ListeFragen[self.__aFrag][4] == "Zeit":
                                                if Typ.position == 0:
                                                    Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_sortier1.get())
                                                if Typ.position == 1:
                                                    Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_sortier2.get())
                                            else:
                                                Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_sortier.get())
                                        except:
                                            Typ.Punkte = Typ.Punkte+int(Ausgabe.Punkte_sortier.get())
                                    except:
                                        pass
                    self.Gruppenakk(Buff2,Ausgabe,True)
                    for Typ in self.__ListeSpieler:
                        Typ.aktuelleAntwort = 0

            Buff2.setPunkteanzeigen(Ausgabe.getPunkteanzeigen())


    def Gruppenakk(self,Buff2,Ausgabe,flag=False):
        Gruppen=[]
        if flag==False:
            for Typ in self.__ListeSpieler:
                Gruppen.append([Typ.Gruppe,0,Typ.Punkte,Typ.Aktiv])
            Buff2.setGruppen(Gruppen)
        else:
            for Typ in self.__ListeSpieler:
                Gruppen.append([Typ.Gruppe,Typ.aktuelleAntwort,Typ.Punkte,Typ.Aktiv])
            Buff2.setGruppen(Gruppen)
        Gruppen=[]
        for Typ in self.__ListeSpieler:
            Gruppen.append([Typ.Gruppe,Typ.aktuelleAntwort,Typ.Punkte,Typ.Aktiv])
        Ausgabe.setGruppen(Gruppen)




                #if b[1]=="Hallo":
                #    Buff.BufOUTset(0,"Anwedung "+str(b[0])+" sendet " + b[1])
                #else:
                #    Buff.BufOUTset(b[0],"Anwdung sendet " + b[1])

        #"""while True:
        #    b = Buff.BufINget()
        #    if b!=None:
        #        print(str(b[0]),b[1])
        #        if b[1]=="Hallo":
        #            Buff.BufOUTset(0,"Anwedung "+str(b[0])+" sendet " + b[1])
        #        else:
        #            Buff.BufOUTset(b[0],"Anwdung sendet " + b[1])"""
