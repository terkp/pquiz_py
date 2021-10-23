import json

class FragenHandler():
    currentQuestion = ("".encode())

    def __init__(self, liste):
        self.__liste_Fragen=liste

    def readMessage(self,frage):
        print(frage)
        if(frage[0] == "normal"):
            questionType =  "standard";
            title = frage[1]
            jasonFile = json.dumps({'questionType': 'standard','title': frage[1], 'id': 4,"answers": [frage[2][0], frage[2][1], frage[2][2], frage[2][3]]})
            FragenHandler.currentQuestion = jasonFile.encode()
