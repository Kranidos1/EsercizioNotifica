from Frames.mainDialog import PersonalizedDialog
from Database.notificaDAO import notificaDAO
#ricorda di distruggere modale
import ast
import wx

class threadNotifica :
    
    def __init__(self ,username):
        
        #username da settare
        self.username = username
        self.notifica = notificaDAO()
        
        wx.CallLater(4000 ,self.checkNotifiche)
    
    def openDialog(self ,msg):
        
        #apre mainDialog
        dialog = PersonalizedDialog(threadRef = self ,msg=msg)
        
        dialog.ShowModal()
            
        dialog.Destroy()
            
            
    def checkNotifiche(self):
            
        #controlla notifiche presenti per un determinato user
        notifiche = self.notifica.getNotifiche("Test")

        try:

            #controlla se in lista ci sono effettivamente delle notifiche ,che nel caso verranno visualizzate una dopo l'altra
            if len(notifiche) != 0:
               
                for notifica in notifiche :

                    
                    #trasforma da lista sottoforma di stringa in lista 
                    notifica['mes_campiRisposta'] = ast.literal_eval(str(notifica['mes_campiRisposta']))
                    
                    #trasforma da lista sottoforma di stringa in lista  
                    notifica['mes_bottoni'] = ast.literal_eval(str(notifica['mes_bottoni']))
            
                    self.openDialog(notifica)
            
            #quando tutte le notifiche saranno visualizzate chiamerà se stessa
            wx.CallLater(4000 ,self.checkNotifiche)

        except TypeError :
            #errore rilevato nella configurazione.Tuttavia gia notificato
            pass
        