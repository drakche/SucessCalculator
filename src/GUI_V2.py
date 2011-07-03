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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Kalkulator Uspeha", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.tabNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PanelFirstYear = wx.Panel( self.tabNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"FirstYear" )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		listGradesFirstChoices = []
		self.listGradesFirst = wx.ListBox( self.PanelFirstYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listGradesFirstChoices, 0 )
		bSizer3.Add( self.listGradesFirst, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self.PanelFirstYear, wx.ID_ANY, u"Prosek (ESBP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.PanelFirstYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblAvg = wx.StaticText( self.PanelFirstYear, wx.ID_ANY, u"0.00 (0)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblAvg.Wrap( -1 )
		bSizer3.Add( self.lblAvg, 0, wx.ALL, 5 )
		
		self.PanelFirstYear.SetSizer( bSizer3 )
		self.PanelFirstYear.Layout()
		bSizer3.Fit( self.PanelFirstYear )
		self.tabNotebook.AddPage( self.PanelFirstYear, u"Prva", True )
		self.PanelSecondYear = wx.Panel( self.tabNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		listGradesSecondChoices = []
		self.listGradesSecond = wx.ListBox( self.PanelSecondYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listGradesSecondChoices, 0 )
		bSizer31.Add( self.listGradesSecond, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText171 = wx.StaticText( self.PanelSecondYear, wx.ID_ANY, u"Prosek (ESBP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer31.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.PanelSecondYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText181 = wx.StaticText( self.PanelSecondYear, wx.ID_ANY, u"0.00 (0)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		bSizer31.Add( self.m_staticText181, 0, wx.ALL, 5 )
		
		self.PanelSecondYear.SetSizer( bSizer31 )
		self.PanelSecondYear.Layout()
		bSizer31.Fit( self.PanelSecondYear )
		self.tabNotebook.AddPage( self.PanelSecondYear, u"Druga", False )
		self.PanelThirdYear = wx.Panel( self.tabNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		listGradesThirdChoices = []
		self.listGradesThird = wx.ListBox( self.PanelThirdYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listGradesThirdChoices, 0 )
		bSizer32.Add( self.listGradesThird, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText172 = wx.StaticText( self.PanelThirdYear, wx.ID_ANY, u"Prosek (ESBP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )
		bSizer32.Add( self.m_staticText172, 0, wx.ALL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.PanelThirdYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer32.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText182 = wx.StaticText( self.PanelThirdYear, wx.ID_ANY, u"0.00 (0)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )
		bSizer32.Add( self.m_staticText182, 0, wx.ALL, 5 )
		
		self.PanelThirdYear.SetSizer( bSizer32 )
		self.PanelThirdYear.Layout()
		bSizer32.Fit( self.PanelThirdYear )
		self.tabNotebook.AddPage( self.PanelThirdYear, u"Treća", False )
		self.PanelFourthYear = wx.Panel( self.tabNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		listGradesFourthChoices = []
		self.listGradesFourth = wx.ListBox( self.PanelFourthYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listGradesFourthChoices, 0 )
		bSizer33.Add( self.listGradesFourth, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText173 = wx.StaticText( self.PanelFourthYear, wx.ID_ANY, u"Prosek (ESBP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText173.Wrap( -1 )
		bSizer33.Add( self.m_staticText173, 0, wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.PanelFourthYear, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer33.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText183 = wx.StaticText( self.PanelFourthYear, wx.ID_ANY, u"0.00 (0)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText183.Wrap( -1 )
		bSizer33.Add( self.m_staticText183, 0, wx.ALL, 5 )
		
		self.PanelFourthYear.SetSizer( bSizer33 )
		self.PanelFourthYear.Layout()
		bSizer33.Fit( self.PanelFourthYear )
		self.tabNotebook.AddPage( self.PanelFourthYear, u"Četvrta", False )
		
		bSizer41.Add( self.tabNotebook, 1, wx.EXPAND, 5 )
		
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
		
		self.spinGrade = wx.SpinCtrl( self.m_panel51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 5, 10, 5 )
		fgSizer1.Add( self.spinGrade, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"ESBP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.spinESBP = wx.SpinCtrl( self.m_panel51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer1.Add( self.spinESBP, 0, wx.ALL, 5 )
		
		bSizer27.Add( fgSizer1, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel51, wx.ID_ANY, wx.Bitmap( u"Pictures/flowerTransparent.gif", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_bitmap1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 5 )
		
		bSizer9.Add( bSizer27, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDelete = wx.BitmapButton( self.m_panel51, wx.ID_DELETE, wx.Bitmap( u"Icons/trash.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnDelete.SetBitmapDisabled( wx.Bitmap( u"Icons/trash_disable.png", wx.BITMAP_TYPE_ANY ) )
		self.btnDelete.SetBitmapSelected( wx.Bitmap( u"Icons/trash.png", wx.BITMAP_TYPE_ANY ) )
		self.btnDelete.SetBitmapFocus( wx.Bitmap( u"Icons/trash.png", wx.BITMAP_TYPE_ANY ) )
		self.btnDelete.SetBitmapHover( wx.Bitmap( u"Icons/trash.png", wx.BITMAP_TYPE_ANY ) )
		self.btnDelete.Enable( False )
		self.btnDelete.SetToolTipString( u"Obrisi" )
		
		self.btnDelete.Enable( False )
		self.btnDelete.SetToolTipString( u"Obrisi" )
		
		bSizer26.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		self.btnCancel = wx.BitmapButton( self.m_panel51, wx.ID_CANCEL, wx.Bitmap( u"Icons/cancel.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnCancel.SetBitmapDisabled( wx.Bitmap( u"Icons/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCancel.SetBitmapSelected( wx.Bitmap( u"Icons/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCancel.SetBitmapFocus( wx.Bitmap( u"Icons/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCancel.SetBitmapHover( wx.Bitmap( u"Icons/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCancel.SetToolTipString( u"Ponisti" )
		
		self.btnCancel.SetToolTipString( u"Ponisti" )
		
		bSizer26.Add( self.btnCancel, 0, wx.ALL, 5 )
		
		self.btnAdd = wx.BitmapButton( self.m_panel51, wx.ID_ADD, wx.Bitmap( u"Icons/doc_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnAdd.SetBitmapDisabled( wx.Bitmap( u"Icons/doc_plus.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAdd.SetBitmapSelected( wx.Bitmap( u"Icons/doc_plus.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAdd.SetBitmapFocus( wx.Bitmap( u"Icons/doc_plus.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAdd.SetBitmapHover( wx.Bitmap( u"Icons/doc_plus.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAdd.SetToolTipString( u"Usnimi" )
		
		self.btnAdd.SetToolTipString( u"Usnimi" )
		
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
		self.mainToolBar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.mainToolBar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"Icons/doc_lines_stright.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Izracunaj prosek", wx.EmptyString ) 
		self.mainToolBar.AddSeparator()
		self.mainToolBar.AddLabelTool( wx.ID_EXIT, u"tool", wx.Bitmap( u"Icons/on-off.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Izlaz", wx.EmptyString ) 
		self.mainToolBar.Realize()
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MainFrameOnClose )
		self.tabNotebook.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.tabNotebookOnNotebookPageChanged )
		self.listGradesFirst.Bind( wx.EVT_LISTBOX, self.ListGradesFirst_OnListItemSelected )
		self.listGradesSecond.Bind( wx.EVT_LISTBOX, self.ListGradesFirst_OnListItemSelected )
		self.listGradesThird.Bind( wx.EVT_LISTBOX, self.ListGradesFirst_OnListItemSelected )
		self.listGradesFourth.Bind( wx.EVT_LISTBOX, self.ListGradesFirst_OnListItemSelected )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDelete_OnButtonClick )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.btnCancel_OnButtonClick )
		self.btnAdd.Bind( wx.EVT_BUTTON, self.btnAdd_OnButtonClick )
		self.Bind( wx.EVT_TOOL, self.toolCalculateOnToolClicked, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.toolExitOnToolClicked, id = wx.ID_EXIT )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MainFrameOnClose( self, event ):
		event.Skip()
	
	def tabNotebookOnNotebookPageChanged( self, event ):
		event.Skip()
	
	def ListGradesFirst_OnListItemSelected( self, event ):
		event.Skip()
	
	
	
	
	def btnDelete_OnButtonClick( self, event ):
		event.Skip()
	
	def btnCancel_OnButtonClick( self, event ):
		event.Skip()
	
	def btnAdd_OnButtonClick( self, event ):
		event.Skip()
	
	def toolCalculateOnToolClicked( self, event ):
		event.Skip()
	
	def toolExitOnToolClicked( self, event ):
		event.Skip()
	

