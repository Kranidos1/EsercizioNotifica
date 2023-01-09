import wx
from Frames.mainFrame import MainFrame
from Thread.threadNotifica import threadNotifica

app = wx.App()

window = MainFrame()

#username in input
td = threadNotifica("Test")

window.Show()

app.MainLoop()

