import wx
import wx.lib.scrolledpanel
import Modules.ObjectsCreator as creator
from Modules import buttonsFunctions as func
from res.font.FontCreator import createBerlinFont
from Frames.dialogoRimanda import RimandaDialog

from datetime import datetime ,timedelta

class PersonalizedDialog(wx.Dialog):
    
    def __init__(self ,msg):
        
        self.idDict = {}
        self.msg = msg
        
        
        super().__init__(parent = None ,title = "Notifica")
        
        font = self.GetFont()
        font = createBerlinFont(font)
        self.font = font
       
        self.SetSize(500,699)
        self.Centre()
        self.SetIcon(wx.Icon('res/images/notification.png' ,wx.BITMAP_TYPE_PNG))
        self.SetBackgroundColour('white')
        self.EnableCloseButton(False)
        
        #inizio messaggio
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
        
        fieldMessaggio = wx.TextCtrl(panel ,size=(455,100) ,value=msg['mes_Messaggio'] ,style = wx.TE_MULTILINE | wx.TE_READONLY)

        boxMessaggio.Add(labelOggetto ,0 ,wx.LEFT | wx.RIGHT | wx.TOP ,border = 10)
        boxMessaggio.Add(labelMessaggio ,0 ,wx.LEFT | wx.RIGHT | wx.TOP ,border = 10)
        boxMessaggio.Add(fieldMessaggio ,0 ,wx.LEFT,border = 10)
        
        boxMessaggioRicevuto.Add(boxMittenteData)
        boxMessaggioRicevuto.Add(boxMessaggio)
        
        panel.SetSizerAndFit(boxMessaggioRicevuto)
        panel.SetPosition((0,0))
        panel.SetSize(500,200)
        #fine messaggio
        
        #inizio risposta
        if(msg['mes_campiRisposta'] != ''):
            
            self.creaPannelloRisposta()
            
            self.creaPannelloBottoni()
            
            self.SetSize(500,649)
        
        #se manca risposta crea solo bottoni
        else:
            
            self.creaPannelloBottoni()

            self.SetSize(500,299)
        
        print(self.idDict)

    def apriDialogoRimanda(self ,evt):
        
        dialogo = RimandaDialog(maxDate=self.msg["mes_dataScadenzaLettura"] ,minDate=self.msg["mes_datacreazione"])
        idRisposta = dialogo.ShowModal()
        
        if(idRisposta == -1):
            #query di update timesleep per idMessaggio e insert di risposta self.msg['mes_id']
            print("ok" )
            
            
        dialogo.Destroy()
        self.EndModal(0)
        self.Destroy()
        
    def creaPannelloRisposta(self):
        
        panel2 = wx.Panel(self)
        panel2.SetFont(self.font)
        panel2.SetPosition((0 ,200))
        panel2.SetSize(500,350)
            
        labelRisposta = wx.StaticText(panel2 ,label = "Risposta :" ,pos = (10,0))
        #pannello interno scrollabile
        panel3 = wx.lib.scrolledpanel.ScrolledPanel(panel2 ,-1 ,size=(454,300) ,pos=(10,20) ,style=wx.SIMPLE_BORDER)
        panel3.SetFont(self.font)
        panel3.SetBackgroundColour('white')
            
        allBoxes = wx.BoxSizer(wx.VERTICAL)
            
        i = 0
        #serve a salvare tutte le box create creando i componenti
        boxList = []
        boxDict = {"box" : boxList ,"iterazione" : i}
            
        #crea gli oggetti nel pannello di risposta inserendoli nei box
        for tmp in self.msg['mes_campiRisposta']:
                
            creator.gestioneCreazioni(tmp ,panel3 ,boxDict ,self.idDict)
            i += 1
                
        
        #aggiunge i box al pannello ,inserendoli in un box generale
        for box in boxList :
                
            allBoxes.Add(box ,flag = wx.EXPAND)
                
        panel3.SetSizer(allBoxes)
        panel3.SetupScrolling()
        #fine risposta
        
    def creaPannelloBottoni(self):
        #inizio bottoni
        panel4 = wx.lib.scrolledpanel.ScrolledPanel(self ,-1 ,size=(500,60) ,pos=(0,550) ,style=wx.SIMPLE_BORDER)
        panel4.SetFont(self.font)
            
        boxBottoni = wx.BoxSizer(wx.HORIZONTAL)
            
        validate = 0
            
        #controlla che possa effettivamente rimandare oltre la notifica
        if datetime.now() < self.msg["mes_dataScadenzaLettura"]:
            validate = 1
                
        #chiede se e' possibile posticipare la notifica e nel caso crea il bottone per permettere all'utente di rimandarla
        if(self.msg["mes_tipoAlert"] == "1" and validate == 1):
                
            boxRimanda = wx.BoxSizer(wx.VERTICAL)
            bottoneRimanda = wx.Button(panel4 ,label = 'Rimanda')
            bottoneRimanda.Bind(wx.EVT_BUTTON ,self.apriDialogoRimanda)
                   
            boxRimanda.Add(bottoneRimanda ,proportion = 0 ,flag = wx.TOP ,border = 15)
                
            boxBottoni.Add(boxRimanda ,proportion = 0 ,flag = wx.LEFT ,border = 25)
                
            id = wx.NewId()
            self.idDict.update({'posticipa':id})
            
        #bottoni successivi
        boxDict = {"box" : boxBottoni ,"iterazione" : -1}
        for tmp in self.msg['mes_bottoni']:
                
            creator.gestioneCreazioni(tmp ,panel4 ,boxDict ,self.idDict)
                
        panel4.SetSizer(boxBottoni)
        panel4.SetupScrolling()
            
        #fine bottoni
        
        
        