# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Success Calculator", pos = wx.DefaultPosition, size = wx.Size( 619,437 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PanelFirstYear = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"FirstYear" )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.listGradesFirst = wx.ListCtrl( self.PanelFirstYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST)		
		bSizer3.Add( self.listGradesFirst, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self.PanelFirstYear, wx.ID_ANY, u"Prosek:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.PanelFirstYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.PanelFirstYear, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.PanelFirstYear.SetSizer( bSizer3 )
		self.PanelFirstYear.Layout()
		bSizer3.Fit( self.PanelFirstYear )
		self.m_notebook1.AddPage( self.PanelFirstYear, u"First year", True )
		self.PanelSecondYear = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		self.listGradesFirst1 = wx.ListCtrl( self.PanelSecondYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer31.Add( self.listGradesFirst1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText171 = wx.StaticText( self.PanelSecondYear, wx.ID_ANY, u"Prosek:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer31.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.PanelSecondYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText181 = wx.StaticText( self.PanelSecondYear, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		bSizer31.Add( self.m_staticText181, 0, wx.ALL, 5 )
		
		self.PanelSecondYear.SetSizer( bSizer31 )
		self.PanelSecondYear.Layout()
		bSizer31.Fit( self.PanelSecondYear )
		self.m_notebook1.AddPage( self.PanelSecondYear, u"Second year", False )
		self.PanelThirdYear = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.listGradesFirst2 = wx.ListCtrl( self.PanelThirdYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer32.Add( self.listGradesFirst2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText172 = wx.StaticText( self.PanelThirdYear, wx.ID_ANY, u"Prosek:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )
		bSizer32.Add( self.m_staticText172, 0, wx.ALL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.PanelThirdYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer32.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText182 = wx.StaticText( self.PanelThirdYear, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )
		bSizer32.Add( self.m_staticText182, 0, wx.ALL, 5 )
		
		self.PanelThirdYear.SetSizer( bSizer32 )
		self.PanelThirdYear.Layout()
		bSizer32.Fit( self.PanelThirdYear )
		self.m_notebook1.AddPage( self.PanelThirdYear, u"Third year", False )
		self.PanelFourthYear = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.listGradesFirst3 = wx.ListCtrl( self.PanelFourthYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer33.Add( self.listGradesFirst3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText173 = wx.StaticText( self.PanelFourthYear, wx.ID_ANY, u"Prosek:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText173.Wrap( -1 )
		bSizer33.Add( self.m_staticText173, 0, wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.PanelFourthYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer33.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText183 = wx.StaticText( self.PanelFourthYear, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText183.Wrap( -1 )
		bSizer33.Add( self.m_staticText183, 0, wx.ALL, 5 )
		
		self.PanelFourthYear.SetSizer( bSizer33 )
		self.PanelFourthYear.Layout()
		bSizer33.Fit( self.PanelFourthYear )
		self.m_notebook1.AddPage( self.PanelFourthYear, u"Fourth year", False )
		
		bSizer41.Add( self.m_notebook1, 1, wx.EXPAND, 5 )
		
		bSizer60.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer60, 1, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel51 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"Predmet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txtSubject = wx.TextCtrl( self.m_panel51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtSubject, 1, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"Ocena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.spinGrade = wx.SpinCtrl( self.m_panel51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer1.Add( self.spinGrade, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"Datum polaganja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.datDatum = wx.DatePickerCtrl( self.m_panel51, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer1.Add( self.datDatum, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer27.Add( fgSizer1, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		bSizer9.Add( bSizer27, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDelete = wx.Button( self.m_panel51, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnDelete.Enable( False )
		
		bSizer26.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		self.btnCancel = wx.Button( self.m_panel51, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.btnCancel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.btnAdd = wx.Button( self.m_panel51, wx.ID_ANY, u"Add grade", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.btnAdd, 0, wx.ALL, 5 )
		
		bSizer9.Add( bSizer26, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_panel51.SetSizer( bSizer9 )
		self.m_panel51.Layout()
		bSizer9.Fit( self.m_panel51 )
		bSizer42.Add( self.m_panel51, 1, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.mainMenu = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.menuFile, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.menuFile, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.menuFile, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.AppendItem( self.m_menuItem3 )
		
		self.mainMenu.Append( self.menuFile, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menu2.AppendSeparator()
		
		self.mainMenu.Append( self.m_menu2, u"MyMenu" ) 
		
		self.m_menu3 = wx.Menu()
		self.mainMenu.Append( self.m_menu3, u"MyMenu" ) 
		
		self.SetMenuBar( self.mainMenu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listGradesFirst.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.ListGradesFirst_OnListItemDeselected )
		self.listGradesFirst.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ListGradesFirst_OnListItemSelected )
		self.listGradesFirst1.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.ListGradesFirst_OnListItemDeselected )
		self.listGradesFirst1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ListGradesFirst_OnListItemSelected )
		self.listGradesFirst2.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.ListGradesFirst_OnListItemDeselected )
		self.listGradesFirst2.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ListGradesFirst_OnListItemSelected )
		self.listGradesFirst3.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.ListGradesFirst_OnListItemDeselected )
		self.listGradesFirst3.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ListGradesFirst_OnListItemSelected )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDelete_OnButtonClick )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.btnCancel_OnButtonClick )
		self.btnAdd.Bind( wx.EVT_BUTTON, self.btnAdd_OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ListGradesFirst_OnListItemDeselected( self, event ):
		event.Skip()
	
	def ListGradesFirst_OnListItemSelected( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	def btnDelete_OnButtonClick( self, event ):
		event.Skip()
	
	def btnCancel_OnButtonClick( self, event ):
		event.Skip()
	
	def btnAdd_OnButtonClick( self, event ):
		event.Skip()
	

