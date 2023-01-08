import wx
from Frames.mainFrame import MainFrame
from Thread.threadNotifica import threadNotifica

#quando chiudere la connessione ? o apri e chiudi a ogni query

app = wx.App()

window = MainFrame()

#username in input
td = threadNotifica("Test")

window.Show()

app.MainLoop()





