import wx
import wx.stc as stc
import wx.adv as adv
from wx.lib.masked import TimeCtrl
from Modules import buttonsFunctions as func


def gestioneCreazioni(dialogRef ,txtObject ,parent ,box ,idDict):
    
    
    #crea un nuovo id
    id = wx.NewId()
    
    #salva il tipo di oggetto ,l'id per utilizzarlo se necessario ,l'id per salvare nel database sottoforma di {'idDB':idDB ,'value':value} dove idDB e' l'id dell'oggeto nel messaggio ricevuto
    idDict.append({'obj':txtObject['obj'] ,"id":id ,"idDB" :txtObject['id']})
    
    if txtObject['obj'] == 'testo':
        creaTextField(txtObject['label'] ,parent ,id ,box)
        
    if txtObject['obj'] == 'combo':
        creaCombo(txtObject['label'] ,parent ,id ,box ,txtObject['valori'])
        
    if txtObject['obj'] == 'calendario':
        creaCalendario(txtObject['label'] ,parent ,id ,box)
    
    if txtObject['obj'] == 'timePicker':
        creaTimePicker(txtObject['label'] ,parent ,id ,box)

    if txtObject['obj'] == 'checkbox':
        
        creaCheckBox(txtObject['label'] ,parent ,id ,box)
 
    if txtObject['obj'] == 'checkboxlist':
        
        creaCheckBoxList(txtObject['label'] ,parent ,id ,box)       
    
    #bottone in pannello risposta (questo viene centralizzato nel pannello risposta)
    if txtObject['obj'] == 'bottone' and dialogRef.isRisposta != -1:
        
        creaBottoneRisposta(dialogRef ,txtObject['label'] ,parent ,id ,box ,txtObject['function'])
        
    #bottone in pannello bottoni
    if txtObject['obj'] == 'bottone' and dialogRef.isRisposta == -1:
        
        creaBottone(dialogRef  ,txtObject['label'] ,parent ,id ,box ,txtObject['function'])


def creaTextField(label ,parent ,id ,box):
    
    label = wx.StaticText(parent = parent ,label=label)
    field = wx.TextCtrl(parent = parent ,size = (200,25) ,id=id)
    
    box.Add(label ,proportion = 0 ,flag = wx.TOP | wx.LEFT ,border = 10)
    box.Add(field ,proportion = 0 ,flag = wx.LEFT ,border = 10)
    
def creaCombo(label ,parent ,id ,box ,valori):
    
    label = wx.StaticText(parent = parent ,label=label)
    combo = wx.ComboBox(parent = parent ,id = id ,choices = valori ,size = (200,30) ,style = wx.CB_READONLY)
    
    box.Add(label ,proportion = 0 ,flag = wx.TOP | wx.LEFT ,border = 10)
    box.Add(combo ,proportion = 0 ,flag = wx.LEFT ,border = 10)
    
def creaCalendario(label ,parent ,id ,box):
    
    label = wx.StaticText(parent = parent ,label=label)
    calendario = adv.CalendarCtrl(parent ,id = id)
    
    box.Add(label ,proportion = 0 ,flag = wx.LEFT | wx.TOP ,border = 10)
    box.Add(calendario ,proportion = 0 ,flag = wx.LEFT ,border = 10)
    
def creaTimePicker(label ,parent ,id ,box):
    
    label = wx.StaticText(parent = parent ,label=label)
    timePicker = TimeCtrl(parent ,id = id ,fmt24hr=True)
    
    box.Add(label ,proportion = 0 ,flag = wx.LEFT | wx.TOP ,border = 10)
    box.Add(timePicker ,proportion = 0 ,flag = wx.LEFT ,border = 10)   
    
def creaCheckBox(label ,parent ,id ,box):
    
    checkbox = wx.CheckBox(parent ,label=label ,id=id)

    box.Add(checkbox ,proportion = 0 ,flag = wx.LEFT | wx.TOP ,border = 10)

def creaCheckBoxList(label ,parent ,id ,box):
    
    checkbox = wx.CheckListBox(parent ,choices=label ,id=id )
    
    box.Add(checkbox ,proportion = 0 ,flag = wx.LEFT | wx.TOP ,border = 10)       
        
def creaBottoneRisposta(dialogRef ,label ,parent ,id ,box ,function):

    bottone = wx.Button(parent = parent ,id = id ,label = label)
    bottone.Bind(wx.EVT_BUTTON ,lambda event : eval(function)(dialogRef))
    
    box.Add(bottone ,proportion = 0 ,flag = wx.ALIGN_CENTER ,border = 10)

def creaBottone(dialogRef ,label ,parent ,id ,box ,function):
    
    boxTmp = wx.BoxSizer(wx.VERTICAL)
    
    bottone = wx.Button(parent = parent ,id = id ,label = label)
    bottone.Bind(wx.EVT_BUTTON ,lambda event : eval(function)(dialogRef))
    
    boxTmp.Add(bottone ,proportion = 0 ,flag = wx.TOP ,border = 15)
    
    box.Add(boxTmp ,proportion = 0 ,flag = wx.LEFT ,border = 25)


