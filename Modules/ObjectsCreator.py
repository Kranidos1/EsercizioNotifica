import wx
import wx.stc as stc
import wx.adv as adv
from wx.lib.masked import TimeCtrl
from Modules import buttonsFunctions as func



def gestioneCreazioni(txtObject ,parent ,boxDict ,idDict):
    
    #boxList : se pannello risposta
    #boxBottoni : se pannello bottoni
    box = boxDict["box"]
    
    #se boxList serve a prendere il box dell' i-esima iterazione del pannello risposta
    #iterazione e' uguale a -1 se box = boxBottoni
    iterazione = boxDict["iterazione"]
    
    #crea un nuovo id
    id = wx.NewId()
    #dizionario che serve a tener conto degli id dei widget con wxPythonId in modo da poter usare i widget se necessario
    idDict.update({txtObject['id'] : id})
    
    #se listBox inserire un nuovo boxSizer nel pannello risposta
    if(iterazione != -1):
        box.append(wx.BoxSizer(wx.VERTICAL))
    
    if txtObject['obj'] == 'testo':
        creaTextField(txtObject['label'] ,parent ,id ,box[iterazione])
        
    if txtObject['obj'] == 'combo':
        creaCombo(txtObject['label'] ,parent ,id ,box[iterazione] ,txtObject['valori'])
        
    if txtObject['obj'] == 'calendario':
        creaCalendario(txtObject['label'] ,parent ,id ,box[iterazione])
    
    if txtObject['obj'] == 'timePicker':
        creaTimePicker(txtObject['label'] ,parent ,id ,box[iterazione])

    if txtObject['obj'] == 'checkbox':
        
        creaCheckBox(txtObject['label'] ,parent ,id ,box[iterazione])
 
    if txtObject['obj'] == 'checkboxlist':
        
        creaCheckBoxList(txtObject['label'] ,parent ,id ,box[iterazione])       
    
    #bottone in pannello risposta
    if txtObject['obj'] == 'bottone' and iterazione != -1:
        
        creaBottoneRisposta(txtObject['label'] ,parent ,id ,box[iterazione] ,"func.testing")
        
    #bottone in pannello bottoni
    if txtObject['obj'] == 'bottone' and iterazione == -1:
        
        creaBottone(txtObject['label'] ,parent ,id ,box ,"func.testing")


def creaTextField(label ,parent ,id ,box):
    
    label = wx.StaticText(parent = parent ,label=label)
    field = wx.TextCtrl(parent = parent ,size = (200,22) ,id=id)
    
    box.Add(label ,proportion = 0 ,flag = wx.TOP | wx.LEFT ,border = 10)
    box.Add(field ,proportion = 0 ,flag = wx.LEFT ,border = 10)
    
def creaCombo(label ,parent ,id ,box ,valori):
    
    label = wx.StaticText(parent = parent ,label=label)
    combo = wx.ComboBox(parent = parent ,id = id ,choices = valori ,size = (200,23) ,style = wx.CB_READONLY)
    
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
        
def creaBottoneRisposta(label ,parent ,id ,box ,function):

    bottone = wx.Button(parent = parent ,id = id ,label = label)
    bottone.Bind(wx.EVT_BUTTON ,eval(function))
    
    box.Add(bottone ,proportion = 0 ,flag = wx.ALIGN_CENTER ,border = 10)

def creaBottone(label ,parent ,id ,box ,function):
    
    boxTmp = wx.BoxSizer(wx.VERTICAL)
    
    bottone = wx.Button(parent = parent ,id = id ,label = label)
    bottone.Bind(wx.EVT_BUTTON ,eval(function))
    
    boxTmp.Add(bottone ,proportion = 0 ,flag = wx.TOP ,border = 15)
    
    box.Add(boxTmp ,proportion = 0 ,flag = wx.LEFT ,border = 25)