#from http.server import BaseHTTPRequestHandler,HTTPServer
from http.server import HTTPServer, BaseHTTPRequestHandler
import fragenEinlesen
import FragenHandler
import pygame
#import Anzeige
#import Anzeige2
from _thread import start_new_thread
from tkinter.filedialog import askopenfilename
from tkinter import *
import Anwendung
import Buffer
import Buffer2
import Anzeige
import Anzeige2
import cgi
from http import HTTPStatus
import json
import time
import logging
import json



hostName = "0.0.0.0"
serverPort = 8080
Buff=Buffer.Buffer()


class Server(BaseHTTPRequestHandler):
    #def _set_response(self):
    #    self.send_response(200)
    #    self.send_header('Content-type', 'text/html')
    #    self.end_headers()


    #def _set_headers(self):
    #    self.send_response(200)
    #    self.send_header('Content-type', 'application/json')
    #    self.send_header('Access-Control-Allow-Origin', '*')
    #    self.end_headers()

    #def do_HEAD(self):
    #    self._set_headers()


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print(FragenHandler.FragenHandler.currentQuestion)
        self.wfile.write(FragenHandler.FragenHandler.currentQuestion)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        new_data=json.loads(post_data)
        print(new_data)
        Buff.Bufin(new_data)

    #def do_Post(self):
        #ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        # refuse to receive non-json content
        #if ctype != 'application/json':
        #    self.send_response(400)
        #    self.end_headers()
        #    return
    #    length = int(self.headers.get('content-length'))
    #    message = json.loads(self.rfile.read(length))
    #    print(message)
    #    self._set_headers()
    #    self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
    #def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
    #    self.send_response(HTTPStatus.NO_CONTENT.value)
    #    self.send_header('Access-Control-Allow-Origin', '*')
    #    self.send_header('Access-Control-Allow-Methods', 'GET, POST')
    #    self.send_header('Access-Control-Allow-Headers', 'content-type')
    #    self.end_headers()

def test(Buff):
    print("25")
    #Buff.Bufin(["4","gruppe1",["b"],])
    time.sleep(20)
    print("5")
    time.sleep(5)
    print("ready")
    Buff.Bufin(["4","gruppe1",["d","b","c","a"],])
    Buff.Bufin(["4","gru2",["d","b","c","a"],])
    #Bufinn.Bufin(["4","gruppe1",["b"],])

def webserverdef (Buff):
    webServer = HTTPServer((hostName, serverPort), Server)

    print("Server started http://%s:%s" % (hostName, serverPort))
    print("test")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    name = askopenfilename()
    print("running")
    leseEingabe = fragenEinlesen.lesen()
    liste_Fragen = leseEingabe.fragen_einlesen(name)
    fragenHandler = FragenHandler.FragenHandler(liste_Fragen)
    fragenHandler.readMessage(liste_Fragen[0])
    Buff2 = Buffer2.Buffer2()
    root = Tk()
    Ausgabe = Anzeige2.App(root)
    start_new_thread(Anzeige.App,(Buff2,))
    start_new_thread(Anwendung.Anwendung,(Buff,Ausgabe,Buff2))
    start_new_thread(webserverdef,(Buff,))
    start_new_thread(test,(Buff,))
    root.mainloop()
