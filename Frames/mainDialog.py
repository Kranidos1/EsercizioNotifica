import wx
import wx.lib.scrolledpanel
import Modules.ObjectsCreator as creator
from Modules import buttonsFunctions as func
from res.font.FontCreator import createFont
from Frames.dialogoRimanda import RimandaDialog

from datetime import datetime ,timedelta 
import time

class PersonalizedDialog(wx.Dialog):
    
    def __init__(self ,msg ,threadRef):
        
        #lista di dizionari degli oggetti del tipo {'obj': tipoOggetto, 'id': id, 'idDB': idDB} .
        #Questo dizionario serve a salvare la risposta nel database sottoforma di {"idObj" : idDB ,"value" : valore} .idDB e' l'id dell'oggetto passato nel messaggio ricevuto
        self.idDict = []
        #messaggio ricevuto
        self.msg = msg
        #riferimento al thread
        self.ref = threadRef
        #serve a valutare se si sta creando ancora qualcosa per il pannello risposta
        self.isRisposta = 1
        
        super().__init__(parent = None ,title = "Notifica")
        
        #setta il font
        font = self.GetFont()
        font = createFont(font)
        self.font = font
       
        self.SetSize(500,699)
        self.Centre()
        self.SetIcon(wx.Icon('res/images/notification.png' ,wx.BITMAP_TYPE_PNG))
        self.SetBackgroundColour('white')
        self.EnableCloseButton(False)
        
        #inizio pannello messaggio ricevuto
        panel = wx.Panel(self)
        panel.SetFont(font)
        
        boxMessaggioRicevuto = wx.BoxSizer(wx.VERTICAL)
        
        boxMittenteData = wx.BoxSizer(wx.HORIZONTAL)
        
        boxMittente = wx.BoxSizer(wx.HORIZONTAL)
        
        labelMittente = wx.StaticText(panel ,-1 ,label="Mittente :  " + msg['mes_userCreator'])
        boxMittente.Add(labelMittente ,flag = wx.LEFT | wx.TOP | wx.BOTTOM ,border = 10)
        
        boxData = wx.BoxSizer(wx.HORIZONTAL)
        
        dataInvio = msg['mes_datacreazione'].strftime(f"%d-%m-%Y %H:%M")
        data = wx.StaticText(panel ,-1 ,label="Data di invio :  " + dataInvio)
        boxData.Add(data ,flag = wx.LEFT ,border = 10)
        
        boxMittenteData.Add(boxMittente ,proportion = 0 ,flag = wx.RIGHT ,border = 25)
        boxMittenteData.Add(boxData ,proportion = 0 ,flag = wx.TOP ,border = 10)
        
        boxMessaggio = wx.BoxSizer(wx.VERTICAL)
        
        labelOggetto = wx.StaticText(panel ,-1 ,label="Oggetto :  " + msg['mes_Oggetto'])
        #aggiungi oggetto
        labelMessaggio = wx.StaticText(panel ,-1 ,label="Messaggio :  ")
        
        self.fieldMessaggio = wx.TextCtrl(panel ,size=(455,100) ,value=msg['mes_Messaggio'] ,style = wx.TE_MULTILINE | wx.TE_READONLY)

        boxMessaggio.Add(labelOggetto ,0 ,wx.LEFT | wx.RIGHT | wx.TOP ,border = 10)
        boxMessaggio.Add(labelMessaggio ,0 ,wx.LEFT | wx.RIGHT | wx.TOP ,border = 10)
        boxMessaggio.Add(self.fieldMessaggio ,0 ,wx.LEFT,border = 10)
        
        boxMessaggioRicevuto.Add(boxMittenteData)
        boxMessaggioRicevuto.Add(boxMessaggio)
        
        #fine messaggio ricevuto
        
        #inizio risposta
        if(msg['mes_campiRisposta'] != None):

            panel.SetSizerAndFit(boxMessaggioRicevuto)
            panel.SetPosition((0,0))
            panel.SetSize(500,200)
        
            self.creaPannelloRisposta()
        #fine risposta
            #setto la fine di pannello risposta
            self.isRisposta = -1
        #inizio pannello bottoni
            self.creaPannelloBottoni()
        #fine pannello bottoni
            
            self.SetSize(500,649)
        

        #se manca risposta crea solo bottoni
        else:
    
            panel.SetSizerAndFit(boxMessaggioRicevuto)
            panel.SetPosition((0,0))
            panel.SetSize(500,300)
        
            #dico alla funzione creaPannelloBottoni che il fieldMessaggio ,dato che manca il pannello di risposta ,sarà piu grande
            self.isRisposta = -2
        #inizio pannello bottoni    
            self.creaPannelloBottoni()
        #fine pannello bottoni
            self.fieldMessaggio.SetSize((455,150))
            self.SetSize(500,370)
        
        #print(self.idDict)

    #serve ad aprire il dialogo con il calendario e il timepicker per rimanda la notifica.
    def apriDialogoRimanda(self ,evt):
        
        dialogo = RimandaDialog(maxDate=self.msg["mes_dataScadenzaLettura"] ,minDate=self.msg["mes_datacreazione"])
        idRisposta = dialogo.ShowModal()
        
        if(idRisposta == -1):
            #query di update timesleep per idMessaggio
            
            #prende la data dal calendario
            date = dialogo.calendario.GetDate()

            #prende il tempo dal timepicker
            time = dialogo.timePicker.GetValue(as_wxDateTime=True)

            #formatta la data
            date = date.Format(format=f"%Y-%m-%d")

            #crea la data da inserire nella query
            queryDate = date + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)

            #fa la query
            self.ref.notifica.updateTimeSleep(queryDate ,self.msg['mes_id'])
            
            dialogo.Destroy()
            self.EndModal(0)
            self.Destroy()
        
    def creaPannelloRisposta(self):
        
        panel2 = wx.Panel(self)
        panel2.SetFont(self.font)
        panel2.SetPosition((0 ,200))
        panel2.SetSize(500,350)
            
        labelRisposta = wx.StaticText(panel2 ,label = "Risposta :" ,pos = (10,0))
        #pannello interno scrollabile (pannello risposta)
        panel3 = wx.lib.scrolledpanel.ScrolledPanel(panel2 ,-1 ,size=(454,300) ,pos=(10,20) ,style=wx.SIMPLE_BORDER)
        panel3.SetFont(self.font)
        panel3.SetBackgroundColour('white')
            
        #serve a inserire in se stesso tutti i box che verranno creati
        allBoxes = wx.BoxSizer(wx.VERTICAL)
            
        i = 0
        #serve a salvare tutte le box create creando i componenti
        #sostanzialmente in gestioneCreazioni verranno chiamate delle funzioni che creano gli oggetti.Ogni oggetto ,con la propria label, e' inserito all'interno di un boxSizer
        #questo boxSizer viene salvato in boxList ,che successivamente verrà inserito in allBoxes

        boxList = []
            
        #crea gli oggetti nel pannello di risposta inserendoli nei box
        for tmp in self.msg['mes_campiRisposta']:
                
            box = wx.BoxSizer(wx.VERTICAL)
            boxList.append(box)
            creator.gestioneCreazioni(self ,tmp ,panel3 ,box ,self.idDict)
            i += 1
                
        #aggiunge i box al pannello ,inserendoli in un box generale
        for box in boxList :
                
            allBoxes.Add(box ,flag = wx.EXPAND)
        
        panel3.SetSizer(allBoxes)
        panel3.SetupScrolling()
        #fine risposta
        
    def creaPannelloBottoni(self):
        
        pos=(0,550)
        if(self.isRisposta == -2):
            pos = (0,271)
            
        #inizio bottoni
        panel4 = wx.lib.scrolledpanel.ScrolledPanel(self ,-1 ,size=(500,60) ,pos=pos ,style=wx.SIMPLE_BORDER)
        panel4.SetFont(self.font)
            
        boxBottoni = wx.BoxSizer(wx.HORIZONTAL)
            
        validate = 0

        #controlla che possa effettivamente rimandare oltre la notifica
        if (datetime.now() + timedelta(minutes=30)) < self.msg["mes_dataScadenzaLettura"]:
            validate = 1
                   
        #chiede se e' possibile posticipare la notifica e nel caso crea il bottone per permettere all'utente di rimandarla
        if(self.msg["mes_tipoAlert"] == "1" and validate == 1):
                
            boxRimanda = wx.BoxSizer(wx.VERTICAL)
            bottoneRimanda = wx.Button(panel4 ,label = 'Rimanda')
            bottoneRimanda.Bind(wx.EVT_BUTTON ,self.apriDialogoRimanda)
                   
            boxRimanda.Add(bottoneRimanda ,proportion = 0 ,flag = wx.TOP ,border = 15)
                
            boxBottoni.Add(boxRimanda ,proportion = 0 ,flag = wx.LEFT ,border = 25)
            
        for tmp in self.msg['mes_bottoni']:
                
            creator.gestioneCreazioni(self ,tmp ,panel4 ,boxBottoni ,self.idDict)
                
        panel4.SetSizer(boxBottoni)
        panel4.SetupScrolling()
            
        #fine bottoni
        
    #con la nuova struttura i bottoni vengono bindati qui ,senza passare riferimento frame


        
        