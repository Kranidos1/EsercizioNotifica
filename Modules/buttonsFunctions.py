import wx
import time
#Struttura dizionario id
#{{'obj':"text" ,"id" :"id" ,"idDB":idDB}}
def rispondi(dialogRef):
    
    #i valori saranno salvati come {"idObj" : id ,"value" : valore}
    #nel db saranno in mes_Messaggio come stringa [{"idObj" : id ,"value" : valore} ,{"idObj" : id1 ,"value" : valore1}]
    valuesList = []
    
    for dict in dialogRef.idDict :
        
        nomeOggetto = dict['obj']
        idInFrame = dict['id']
        idDB = dict['idDB']
        
        if nomeOggetto == "bottone":
            continue
                
        if nomeOggetto == "testo":
            
            value = dialogRef.FindWindowById(idInFrame).GetValue()
            valuesList.append({'idObj' : idDB ,"value" : value})
            
        if nomeOggetto == "combo":
            
            combo = dialogRef.FindWindowById(idInFrame)
            index = combo.GetSelection()
            
            #index error sul combo
            try:
                value = combo.GetString(index)
            except:
                value = ''
                
            valuesList.append({'idObj' : idDB ,"value" : value})
        
        if nomeOggetto == "calendario":
            
            value = dialogRef.FindWindowById(idInFrame).GetDate()
            value = value.Format(format=f"%Y-%m-%d")
            valuesList.append({'idObj' : idDB ,"value" : value})
        
        if nomeOggetto == "timePicker":
            
            value = dialogRef.FindWindowById(idInFrame).GetValue(as_wxDateTime=True)
            value = value.Format(format=f"%H:%M:%S")
            valuesList.append({'idObj' : idDB ,"value" : value})
        
        if nomeOggetto == "checkboxlist":
            
            value = dialogRef.FindWindowById(idInFrame).GetCheckedStrings()
            valuesList.append({'idObj' : idDB ,"value" : value})
        
    #eventuali controlli
    #quindi query per inserimento
    dictRisposta = {"messaggioRicevuto" : dialogRef.msg ,"message" : str(valuesList)}
    dialogRef.ref.notifica.insertRisposta(dictRisposta)
    #update status messaggio padre (volendo si può creare trigger)
    dialogRef.ref.notifica.updateStatus(dialogRef.msg['mes_id'])
    
    dialogRef.Destroy()

def rispostaSemplice(dialogRef):

    dialogRef.ref.notifica.updateStatus(dialogRef.msg['mes_id'])
    dialogRef.Destroy()
    