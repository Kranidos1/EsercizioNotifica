import wx
from datetime import datetime , timedelta, date
import wx.adv as adv
import wx.lib.scrolledpanel
from wx.lib.masked import TimeCtrl


from wx.lib.masked import TimeUpdatedEvent
import Modules.ObjectsCreator as creator
from Modules import buttonsFunctions as func
from res.font.FontCreator import createFont

class RimandaDialog(wx.Dialog):
    
    def __init__(self ,maxDate ,minDate):
        
        #da maxDate e minDate vanno presi una serie di attributi
        
        super().__init__(parent = None ,title = "Scegli data e ora")

        #date + tempo
        self.maxTime = maxDate
        
        #solo date formattate
        self.maxDate = datetime.strftime(maxDate, '%d-%m-%Y')
        self.minDate = datetime.strftime(minDate, '%d-%m-%Y')
        
        font = self.GetFont()
        font = createFont(font)
        
        self.SetSize(450,300)
        self.Centre()
        self.SetIcon(wx.Icon('res/images/notification.png' ,wx.BITMAP_TYPE_PNG))
        self.SetBackgroundColour('white')
        
        
        panel = wx.Panel(self)
        panel.SetFont(font)
        
        mainBox = wx.BoxSizer(wx.VERTICAL)
        
        dataBox = wx.BoxSizer(wx.HORIZONTAL)
        
        boxCalendario = wx.BoxSizer(wx.VERTICAL)
        
        labelCalendario = wx.StaticText(parent = panel ,label="Calendario :")
        
        #crea calendario
        self.idCalendario = wx.NewId()
        self.calendario = adv.CalendarCtrl(panel ,id = self.idCalendario)
        
        #di default si può rimandare da 30minuti in avanti
        self.minTime = datetime.now() + timedelta(minutes=30)
        #data massima
        upper = datetime.strptime(self.maxDate, f"%d-%m-%Y").date()
        
        #setta i limiti del calendario
        self.calendario.SetDateRange(lowerdate = self.minTime  ,upperdate=upper)
        self.calendario.Bind(adv.EVT_CALENDAR_SEL_CHANGED ,self.checkDateCalendario)
        
        boxCalendario.Add(labelCalendario ,proportion = 0 ,flag = wx.TOP | wx.LEFT ,border = 20)
        boxCalendario.Add(self.calendario ,proportion = 0 ,flag = wx.LEFT ,border = 20)
        
        boxTimePicker = wx.BoxSizer(wx.VERTICAL)
        
        labelTimePicker = wx.StaticText(parent = panel ,label="Ora :")
        
        self.idTimePicker = wx.NewId()
        self.timePicker = TimeCtrl(panel ,id = self.idTimePicker ,fmt24hr=True)
        
        dataCreazione = datetime(self.minTime.year ,self.minTime.month ,self.minTime.day)
        dataOggi = datetime.now()
        dataOggi = datetime(dataOggi.year ,dataOggi.month ,dataOggi.day)   
        
        #valuta se e' necessario settare dei bounds per il time picker da subito
        if(dataOggi == dataCreazione):
            
            dictTime = {"minTime":{"hour": self.minTime.hour ,"minute": self.minTime.minute},"maxTime":{"hour":23 ,"minute":59}}
            self.changeTimePickerBounds(self.timePicker ,dictTime)  
        
        boxTimePicker.Add(labelTimePicker ,proportion = 0 ,flag = wx.TOP | wx.LEFT ,border = 20)
        boxTimePicker.Add(self.timePicker ,proportion = 0 ,flag = wx.LEFT ,border = 20)
        
        dataBox.Add(boxCalendario)
        dataBox.Add(boxTimePicker ,proportion = 0 ,flag = wx.LEFT ,border = 25)
        
        buttonBox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.buttonRimanda = wx.Button(panel ,label = "Rimanda!" )
        self.buttonRimanda.Bind(wx.EVT_BUTTON ,self.returnValues)
        
        buttonBox.Add(self.buttonRimanda ,proportion = 0 ,flag = wx.CENTER ,border = 0)
       
        mainBox.Add(dataBox)
        mainBox.Add(buttonBox ,proportion = 0 ,flag = wx.CENTER | wx.TOP ,border = 25)
        
        panel.SetSizerAndFit(mainBox)
        
    def returnValues(self ,evt):
        
        #checkValues

        #-1 indica che e' effettivamente l'utente ha cliccato sul bottone "Rimanda!"
        self.EndModal(-1)
        
    #serve a settare dei bounds di scelta sia per la data che per l'ora  nel caso in cui viene selezionata la data massima o minima(di creazione o (attuale +30minuti))
    def checkDateCalendario(self ,evt):
        
        date = self.calendario.GetDate().Format(format=f"%d-%m-%Y")
        
        if date == self.maxDate:
            
            dictTime = {"minTime":{"hour": 0 ,"minute": 0},"maxTime":{"hour":self.maxTime.hour ,"minute":self.maxTime.minute}}
            self.changeTimePickerBounds(self.timePicker ,dictTime)           
        
        elif date == self.minDate:
            
            dictTime = {"minTime":{"hour": self.minTime.hour ,"minute":self.minTime.minute},"maxTime":{"hour":23,"minute":59}}
            self.changeTimePickerBounds(self.timePicker ,dictTime)
            
        else :
            self.timePicker.SetBounds(None ,None)
            
            
    def changeTimePickerBounds(self ,ref ,dictTime):
        
        maxTime = wx.DateTime.Now()
        maxTime.SetHour(dictTime["maxTime"]['hour'])
        maxTime.SetMinute(dictTime["maxTime"]['minute'])
            
        minTime = wx.DateTime.Now()
        minTime.SetHour(dictTime["minTime"]['hour'])
        minTime.SetMinute(dictTime["minTime"]['minute'])
            
        ref.SetBounds(minTime ,maxTime)
        ref.SetLimited(True)    