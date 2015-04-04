import wx
import wx.xrc

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Download Manager", pos = wx.DefaultPosition, size = wx.Size( 747,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( 747,520 ) )
		self.SetFont( wx.Font( 11, 74, 90, 90, False, "Arial Unicode MS" ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"  Enter URL to download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.DownloadURL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.DownloadURL, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"  Enter Path at which the file is to be downloaded", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.DirectoryValue = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a path for download", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
		bSizer1.Add( self.DirectoryValue, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.TextForError = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TextForError.Wrap( -1 )
		bSizer1.Add( self.TextForError, 0, wx.ALL, 5 )
		
		self.DownloadButton = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.DownloadButton, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"\n----------------------------------------------------------------------------------------------------------------------------------------------------------------", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer1.Add( self.m_staticText8, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.FileNameText = wx.StaticText( self, wx.ID_ANY, u"\n  File Name: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileNameText.Wrap( -1 )
		bSizer1.Add( self.FileNameText, 0, wx.ALL, 5 )
		
		self.DownloadURLText = wx.StaticText( self, wx.ID_ANY, u"  Download URL: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DownloadURLText.Wrap( -1 )
		bSizer1.Add( self.DownloadURLText, 0, wx.ALL, 5 )
		
		self.StatusText = wx.StaticText( self, wx.ID_ANY, u"  Status: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatusText.Wrap( -1 )
		bSizer1.Add( self.StatusText, 0, wx.ALL, 5 )
		
		self.StatusGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.StatusGauge.SetValue( 0 ) 
		bSizer1.Add( self.StatusGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ResultText = wx.StaticText( self, wx.ID_ANY, u"  Result: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ResultText.Wrap( -1 )
		bSizer1.Add( self.ResultText, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.DownloadButton.Bind( wx.EVT_BUTTON, self.StartDownload )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def StartDownload( self, event ):
		event.Skip()
	

