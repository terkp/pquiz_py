from http.server import BaseHTTPRequestHandler,HTTPServer
import fragenEinlesen
import FragenHandler
import pygame
#import Anzeige
#import Anzeige2
from _thread import start_new_thread
from tkinter.filedialog import askopenfilename
from tkinter import *

hostName = "0.0.0.0"
serverPort = 8080

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print(FragenHandler.FragenHandler.currentQuestion)
        self.wfile.write(FragenHandler.FragenHandler.currentQuestion)

if __name__ == "__main__":
    name = askopenfilename()
    leseEingabe = fragenEinlesen.lesen()
    liste_Fragen = leseEingabe.fragen_einlesen(name)
    fragenHandler = FragenHandler.FragenHandler(liste_Fragen)
    fragenHandler.readMessage(liste_Fragen[6])

    #root = Tk()
    #Ausgabe = Anzeige2.App(root)
    #start_new_thread(Anzeige.App,(Buff2,))
    webServer = HTTPServer((hostName, serverPort), Server)

    print("Server started http://%s:%s" % (hostName, serverPort))
    print("test")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
