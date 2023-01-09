import wx
import os
import shutil

def createFont(font):

       #fonts_folder = os.path.join(os.environ['WINDIR'],'Fonts')
       
       #shutil.copy("./res/font/BRLNSR.TTF",fonts_folder)

       #inc = wx.Font.AddPrivateFont("BRLNSR.TTF")
       
       label_font = font
       
       label_font.SetFamily(wx.FONTFAMILY_DEFAULT)
       label_font.SetStyle(wx.FONTSTYLE_NORMAL)
       label_font.SetWeight(wx.FONTWEIGHT_NORMAL)
       label_font.SetUnderlined(False)
       label_font.SetFaceName("Arial Grassetto")
       label_font.SetEncoding(wx.FONTENCODING_DEFAULT)
       label_font.SetPointSize(16)
       
       return label_font