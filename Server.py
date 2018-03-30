from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import serial

#liaison serie
ser = serial.Serial('ttyAMA0', 9600, timeout = 1)

#Variable global pour le json
valeurRGB=0
valeurONF=0
valeurPOW=[0,0,0,0,0,0]
valeurMOD=0
valeurSPEED=[0,0,0,0,0,0]




def decodeRequest(self):
    request = self.path[1:]
    self.wfile.write("Test : " + request)
    ser.write(request)
    while ser.isOpen():
        decrypt(ser.readline())
        
    
    #envoi a l'arduino
    # attente de réponse (100 ms max)

    # traitement de la réponse
    
    # if erreur (pas de réponse)
        #json = getJson("Error", "Pas de réponse");
    # else
        #json = getJson("OK", "");

    #self.wfile.write(json);
    
def decrypt(data):
    prefix=data[:3]
    valeurPref=data[3:]
    if prefix == 'RGB':
        valeurRGB=int(valeurPref,16)
    if prefix == 'ONF':
        valeurONF=valeurPref
    if prefix == 'POW':
        #separation du numero du mode et de la valeur de power
        modePower=valeurPref[:1]
        power=valeurPref[1:]
        #l'emplacement dans la liste correspond au mode et la valeur à la valeur de power.
        valeurPOW[modePower]=power
    if prefix == 'MOD':
        valeurMode=valeur[:1]
    if prefix == 'SPE':
        #separation du numero du mode et de la valeur de speed
        modeSpeed=valeur[:1]
        valeurSpeed=valeurPref[1:]
        speed=valeurPref[1:]
       #l'emplacement dans la liste correspond au mode et la valeur à la valeur de speed.
        valeurSpeed[modeSpeed]=speed
        
    
    
class S(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        decodeRequest(self)

def run():
    server_address = ('', 8890)
    httpd = HTTPServer(server_address, S)
    print ('Starting httpd...')
    while 1:
        httpd.handle_request()

run()
