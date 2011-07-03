'''
Created on Jun 28, 2011

@author: drakChe
'''
from GUI_V2 import MainFrame
import wx
from DTO import Exam
from DBBroker import Insert,GetAll,Update,Delete
from wx._misc import DateTime


 

        
class GUIOverride(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)
            
        self.Updating = False        
        self.activeYear = self.tabNotebook.GetSelection()
        self.selectedItem = -1
        self.list = GetAll()
        for i in range(0,3):
            for item in self.list[i]:                            
                self.tabNotebook.GetPage(i).GetChildren()[0].Append(str(item),item)
        
        
    def UnselectList(self):
        self.listGradesFirst.Select(-1)
        self.listGradesSecond.Select(-1)
        self.listGradesThird.Select(-1)
        self.listGradesFourth.Select(-1)
    
    def btnCancel_OnButtonClick(self, event):
        
        self.ClearFields()
        
    def mItemExit_OnMenuSelection(self, event):
        self.Destroy()
        
    def ClearFields(self):
        self.txtSubject.Value = ''
        self.datDatum.Value = DateTime.Now()
        self.spinGrade.Value = 0
        self.UnselectList()
        self.btnDelete.Disable()
        
    def tabNotebookOnNotebookPageChanged(self, event):
        self.activeYear = event.GetSelection()
        self.UnselectList()
        event.Skip()
    
        
    
    def btnAdd_OnButtonClick(self, event):        
        ex = Exam()
        ex.Subject = self.txtSubject.Value
        ex.Grade = self.spinGrade.Value
        ex.ESBP = 0
        
        
        
        exist = False
        
        for e in self.list[self.activeYear]:
            if not exist:
                if e.Subject == ex.Subject:
                    exist = True
        if self.Updating:
            self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Delete(self.selectedItem)
            self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Append(str(ex),ex)
            exOld = self.list[self.activeYear].pop(self.selectedItem)
            ex.ExamId = exOld.ExamId
            self.list[self.activeYear].append(ex)
            Update((ex.ExamId,ex.Subject,ex.Grade,ex.ESBP,ex.Year))
            self.Updating = False
        else:
            if not exist:                
                self.list[self.activeYear].append(ex)            
                self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Append(str(ex),ex)
                Insert([(ex.Subject,ex.Grade,ex.ESBP,self.activeYear+1)])
            else:
                wx.MessageBox('Ispit vec postoji')
            
            
                                            
        
        self.ClearFields()
        
        
    def ListGradesFirst_OnListItemSelected(self, event):
        self.selectedItem = event.GetSelection()
        
        item = self.list[self.activeYear][self.selectedItem]
        self.txtSubject.Value = item.Subject
        self.spinGrade.Value = item.Grade
        #TODO: insert esbp here
        self.Updating = True
        self.btnDelete.Enable()
        
    def btnDelete_OnButtonClick(self, event):
        res = wx.MessageDialog(None,'Da li zelite da obrisete ispit?',
                  'Info',   
                  wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION).ShowModal()
        if res == wx.ID_YES:
            it = self.list[self.activeYear].pop(self.selectedItem)
            self.tabNotebook.GetPage(self.activeYear).GetChildren()[0].Delete(self.selectedItem)
            Delete(it.ExamId)
            self.ClearFields()
        
        
        
if __name__ == '__main__':
    a = wx.App()
    GUIOverride(None).Show()
    a.MainLoop()
