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
        
        
        
        self.activeYear = self.tabNotebook.GetSelection()
        self.selectedItem = -1
        self.list = [[],[],[],[]]
        
    def UnselectList(self):
        self.listGradesFirst.Select(-1)
        self.listGradesSecond.Select(-1)
        self.listGradesThird.Select(-1)
        self.listGradesFourth.Select(-1)
    
    def btnCancel_OnButtonClick(self, event):
        
        self.ClearFields()
        
    def ClearFields(self):
        self.txtSubject.Value = ''
        self.datDatum.Value = DateTime.Now()
        self.spinGrade.Value = 0
        self.UnselectList()
        self.btnDelete.Disable()
        
    def tabNotebookOnNotebookPageChanged(self, event):
        self.activeYear = self.tabNotebook.GetSelection()
        self.UnselectList()
        event.Skip()
    
    def btnAdd_OnButtonClick(self, event):        
        ex = Exam()
        ex.Subject = self.txtSubject.Value
        ex.Grade = self.spinGrade.Value
        ex.Date = self.datDatum.Value
        
        
        
        exist = False
        
        for e in self.list[self.activeYear]:
            if not exist:
                if e.Subject == ex.Subject:
                    exist = True
         
        if not exist:
            self.list[self.activeYear].append(ex)            
            self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Append(str(ex),ex)
            
        else:
            wx.MessageBox('Uneseni ispit posoji, molimo ispravite','Info')                                
        
        self.ClearFields()
        
        
    def ListGradesFirst_OnListItemSelected(self, event):
        self.selectedItem = event.GetSelection()
        
        item = self.list[self.activeYear][self.selectedItem]
        self.txtSubject.Value = item.Subject
        self.spinGrade.Value = item.Grade
        self.datDatum.Value = item.Date 
        self.btnDelete.Enable()
        
    def btnDelete_OnButtonClick(self, event):
        self.list[self.activeYear].pop(self.selectedItem)
        self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Delete(self.selectedItem)
        self.ClearFields()
        
        
if __name__ == '__main__':
    a = wx.App()
    GUIOverride(None).Show()
    a.MainLoop()
