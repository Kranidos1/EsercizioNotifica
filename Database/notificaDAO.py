import MySQLdb

class notificaDAO :
    
    def getNotifiche(self ,username ,cursor) :
        
        #cursor = connection.connection.cursor()
        query = "SELECT * FROM message WHERE mes_userDestinatario = %s AND mes_Stato = 0"
        cursor.execute(query ,[username])
        
        result = self.toDict(cursor)
        
        return result
                
                
    def toDict(self ,cursor):
        
        dizionarioRisultante = {}
        
        colonne = [col[0] for col in cursor.description]
        
        for riga in cursor:
            # Stampa di tutti gli attributi e i loro valori per ogni riga
            for i, attr in enumerate(colonne):
                val = riga[i]
                
                dizionarioRisultante.update({attr : val})
                
        return dizionarioRisultante