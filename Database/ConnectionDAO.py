import MySQLdb
import wx
import wx.adv
from Database.notificaDAO import notificaDAO
import os

class ConnectionDAO :
   
    #Tenta la connessione al database e ritorna la connessione. Se non riesce a connettersi esce dal programma
    def creaConnessione(self):
        
        data = self.getData()
                    
        try:
                    
            connection = MySQLdb.connect(host = data['host'] ,user = data["user"] ,passwd = data["password"] ,db = data["database"])
                    
            return connection
                
        except MySQLdb.OperationalError :
                    
            notification = wx.adv.NotificationMessage("Errore di connessione al database", "Errore imprevisto di connessione al database.Riprovare piu tardi.", parent=None)
            notification.Show(True)
            quit()
        
        except KeyError :
            
            notification = wx.adv.NotificationMessage("Errore chiavi database", "Controlla le chiavi per la connessione al database", parent=None)
            notification.Show(True)
            
    def __init__(self) :
        
        self.connection = self.creaConnessione()
        self.notifica = notificaDAO()
        self.cursor = self.connection.cursor()
        
    #Chiusura sicura della connessione
    def chiudiConnessione(self ,connessione):
                
        if connessione.open:
            
            connessione.close()
            print("Chiusura avvenuta con successo.")
                    
        else:
            print("La connessione non e' aperta ,quindi non si può chiudere.")
            
    def getData(self):
        
        data = {}
        path = os.getenv('APPDATA') + "\\databaseData.txt"
        
        f = open(path ,"r+")
        
        tmp = f.readline()
        #controlla EOF
        while tmp != '':
            
            tmp = tmp.split("=")
            
            key = tmp[0]
            value = tmp[1]
            value = value.replace("\n","")
            
            data.update({key:value})
            
            tmp = f.readline()
        
        return data
            