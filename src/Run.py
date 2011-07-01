'''
Created on Jun 28, 2011

@author: drakChe
'''
from GUI_V2 import MainFrame
import wx

from wx._misc import DateTime

class Exam(object):    
    def __init__(self, subject='', grade=0, date=DateTime.Now()):
        self.Subject = subject
        self.Grade = grade
        self.Date = date
        
    def __repr__(self, *args, **kwargs):
        return '{0} - {1} ({2})'.format(self.Subject,str(self.Grade),self.Date.Format('%d-%m-%Y'))
        
class GUIOverride(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        
        self.list = [[],[],[],[]]
        
    def UnselectList(self):
        self.listGradesFirst.Select(-1, None)
        self.listGradesSecond.Select(-1, None)
        self.listGradesThird.Select(-1, None)
        self.listGradesFourth.Select(-1, None)
    
    def btnCancel_OnButtonClick(self, event):
        self.txtSubject.Value = ''
        self.datDatum.Value = DateTime.Now()
        self.spinGrade.Value = 0
        self.UnselectList()
        
    def tabNotebookOnNotebookPageChanged(self, event):
        self.UnselectList()
        event.Skip()
    
    def btnAdd_OnButtonClick(self, event):        
        ex = Exam()
        ex.Subject = self.txtSubject.Value
        ex.Grade = self.spinGrade.Value
        ex.Date = self.datDatum.Value
        
        activeYear = self.tabNotebook.GetSelection()       
        self.list[activeYear].append(ex)             
        self.tabNotebook.GetPage(activeYear).GetChildren()[0].Append(self.list[activeYear])
        self.UnselectList()
        
    def ListGradesFirst_OnListItemSelected(self, event):
        id = event.GetSelection()
        activeYear = self.tabNotebook.GetSelection()
        item = self.list[activeYear][id]
        self.txtSubject.Value = item.Subject
        self.spinGrade.Value = item.Grade
        self.datDatum.Value = item.Date        

if __name__ == '__main__':
    a = wx.App()
    GUIOverride(None).Show()
    a.MainLoop()
