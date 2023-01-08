from datetime import time ,datetime
from Frames.mainDialog import PersonalizedDialog
from Frames.dialogoRimanda import RimandaDialog
from Database.ConnectionDAO import ConnectionDAO
#ricorda di distruggere modale
import ast
import wx

class threadNotifica :
    
    def __init__(self ,username):
        
        self.username = username
        self.conn = ConnectionDAO()
        
        #self.notificheApparse = []
        
        wx.CallLater(4000 ,self.checkNotifiche)
    
    def openDialog(self ,msg):
            
        '''
            #come arriva il messaggio
            r={
                "mittente":"Michele",
                "destinatario":"Mattia",
                "dataNotifica":"2023-01-03",
                "messaggio":"Ricorda di fare fatturesdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "risposta":{
                    "campiRisposta":[{"obj":"testo" ,"label":"Testo","id":"txt1"},
                                    {"obj":"combo","valori":["1","5","6"] ,"label":"Combo","id":"combo1"},
                                    {"obj":"calendario" ,"label":"calendario" ,"id":"calendar"},
                                    {"obj":"timePicker" ,"label":"Scegli ora" ,"id":"timepicker"},
                                    {"obj":"bottone" ,"label":"Scegli ora" ,"id":"bottone"},
                                    {"obj":"checkboxlist" ,"label":["Value A","Value B","Value C"] ,"id":"checkboxlist"}
                                    ],
                    "bottoni":[{"label":"OK","function":"self.close"},{"label":"Registra","function":""}]
                },
                "opzioniMess":{"posticipa":True,"richiediNotifica":True ,"maxPosticipa":"20-01-2023"},
                "buttons":[{"obj":"bottone" ,"label":"Si" ,"function" : "func.testing" ,"id":"si"},{"obj":"bottone" ,"label":"No" ,"function" : "func.testing","id":"no"},{"obj":"bottone" ,"label":"BOoh" ,"function" : "func.testing","id":"boh"}],
            }
        '''
        dialog = PersonalizedDialog(msg=msg)
        
        dialog.ShowModal()
            
        dialog.Destroy()
            
            
    def checkNotifiche(self):
            
        notifica = self.conn.notifica.getNotifiche("Test" ,self.conn.cursor)
            
        if len(notifica) != 0:
               
            print(notifica)
            #trasforma da lista sottoforma di stringa in lista 
            notifica['mes_campiRisposta'] = ast.literal_eval(notifica['mes_campiRisposta'])
            
            #trasforma da lista sottoforma di stringa in lista  
            notifica['mes_bottoni'] = ast.literal_eval(notifica['mes_bottoni'])
                
            self.openDialog(notifica)
                
        wx.CallLater(4000 ,self.checkNotifiche)
            
    #controlla se una notiifca e' gia stata visualizzata dall'utente attualmente
    def controllaApparse(self):
        pass