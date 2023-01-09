import MySQLdb
import wx
import wx.adv
from Database.ConnectionDAO import ConnectionDAO

class notificaDAO :
    
    def __init__(self):

        self.conn = ConnectionDAO()


    def getNotifiche(self ,username ) :
        
        self.conn.connection = self.conn.creaConnessione()
        
        try:

            cursor =  self.conn.connection.cursor()
            #cursor = connection.connection.cursor()
            query = "SELECT * FROM message WHERE mes_userDestinatario = %s AND mes_Stato = 0 AND (mes_sleep IS NULL OR mes_sleep <= NOW()) AND (mes_dataImpostata IS NULL OR mes_dataImpostata <= NOW())"
            cursor.execute(query ,[username])

            self.conn.chiudiConnessione(self.conn.connection)
            
            result = self.toDict(cursor)
            
            return result

        except AttributeError:

            notification = wx.adv.NotificationMessage("Errore chiavi configurazione", "Errore nella configurazione del database", parent=None)
            notification.Show(5)          


    def updateTimeSleep(self ,time ,mesId ):

        self.conn.connection = self.conn.creaConnessione()

        cursor =  self.conn.connection.cursor()

        query = "UPDATE message SET mes_sleep = %s WHERE mes_id = %s"
        cursor.execute(query ,[time ,mesId])

        self.conn.connection.commit()

        notification = wx.adv.NotificationMessage("Notifica Rimanda", "Notifica rimandata correttamente", parent=None)
        notification.Show(5)
        
        cursor.close()
        self.conn.chiudiConnessione(self.conn.connection)


    def updateStatus(self ,mesId):

        self.conn.connection = self.conn.creaConnessione()

        cursor =  self.conn.connection.cursor()

        query = "UPDATE message SET mes_Stato = 1,mes_dataLettura = NOW() WHERE mes_id = %s"

        cursor.execute(query ,[mesId])

        self.conn.connection.commit()
        cursor.close()
        self.conn.chiudiConnessione(self.conn.connection)       

    
    def insertRisposta(self ,dictRisposta):

        self.conn.connection = self.conn.creaConnessione()

        cursor =  self.conn.connection.cursor()

        creatore = dictRisposta['messaggioRicevuto']['mes_userDestinatario']
        oggetto = dictRisposta['messaggioRicevuto']['mes_Oggetto']
        idPadre = dictRisposta['messaggioRicevuto']['mes_id']
        messaggio = dictRisposta['message']
        
        query = "INSERT INTO message (mes_datacreazione ,mes_userCreator ,mes_idPadre ,mes_Oggetto ,mes_Messaggio) VALUES (NOW() ,%s ,%s ,%s ,%s)"
        cursor.execute(query ,[creatore ,idPadre ,oggetto ,messaggio])
        
        self.conn.connection.commit()
        cursor.close()
        self.conn.chiudiConnessione(self.conn.connection)   
                         
    def toDict(self ,cursor):
        
        listaDialoghi = []
        dizionarioRisultante = {}
        
        colonne = [col[0] for col in cursor.description]
        
        for riga in cursor:
               
            # Stampa di tutti gli attributi e i loro valori per ogni riga
            for i, attr in enumerate(colonne):
                val = riga[i]
                
                dizionarioRisultante.update({attr : val})

            listaDialoghi.append(dizionarioRisultante)
                
        return listaDialoghi