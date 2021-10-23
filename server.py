from http.server import BaseHTTPRequestHandler,HTTPServer
import fragenEinlesen
import FragenHandler
from tkinter.filedialog import askopenfilename

hostName = "localhost"
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
    fragenHandler.readMessage(liste_Fragen[0])
    webServer = HTTPServer((hostName, serverPort), Server)

    print("Server started http://%s:%s" % (hostName, serverPort))
    print("test")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
