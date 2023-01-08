import wx

def createBerlinFont(font):
    
       wx.Font.AddPrivateFont("BRLNSR.TTF")
       
       label_font = font
       label_font.SetPointSize(12)
       label_font.SetFamily(wx.FONTFAMILY_DEFAULT)
       label_font.SetStyle(wx.FONTSTYLE_NORMAL)
       label_font.SetWeight(wx.FONTWEIGHT_NORMAL)
       label_font.SetUnderlined(False)
       label_font.SetFaceName("Berlin Sans FB")
       label_font.SetEncoding(wx.FONTENCODING_DEFAULT)
       
       return label_font