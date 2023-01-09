import wx
from datetime import datetime
from wx.adv import Animation, AnimationCtrl
from Frames.mainDialog import PersonalizedDialog
from Frames.dialogoRimanda import RimandaDialog
from Database.ConnectionDAO import ConnectionDAO
from res.font.FontCreator import createFont


class MainFrame(wx.Frame):
    
    #supponendo presenza di un nickname
    
    def __init__(self):
       
       super().__init__(parent = None ,title = "Frame aperto durante thread")

       font = self.GetFont()
       font = createFont(font)
       
       panel = wx.Panel(self)
       panel.SetFont(font)

       self.username = "Test"
       self.conn = ConnectionDAO()
       self.occupato = 0
       self.SetSize(500,500)
       
       mainBox = wx.BoxSizer(wx.VERTICAL)
       
       panel.SetSizerAndFit(mainBox)
       

        
        
