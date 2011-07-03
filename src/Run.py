'''
Created on Jun 28, 2011

@author: drakChe
'''
from GUI_V2 import MainFrame
import wx
from DTO import Exam
from DBBroker import Insert,GetAll,Update,Delete

class GUIOverride(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)
            
        self.Updating = False        
        self.activeYear = self.tabNotebook.GetSelection()
        self.selectedItem = -1
        self.list = GetAll()
        for i in range(0,4):
            for item in self.list[i]:                            
                self.tabNotebook.GetPage(i).GetChildren()[0].Append(str(item),item)
        self.RecalculateAverage()
        
    def UnselectList(self):
        self.listGradesFirst.Select(-1)
        self.listGradesSecond.Select(-1)
        self.listGradesThird.Select(-1)
        self.listGradesFourth.Select(-1)
    
    def btnCancel_OnButtonClick(self, event): 
        self.Updating = False       
        self.ClearFields()
        
    def mItemExit_OnMenuSelection(self, event):
        self.Destroy()
        
    def ClearFields(self):
        self.txtSubject.Value = ''
        self.spinESBP.Value = 0
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
        ex.ESBP = self.spinESBP.Value        
        ex.Year = self.activeYear + 1
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
                Insert([(ex.Subject,ex.Grade,ex.ESBP,ex.Year)])
            else:
                wx.MessageBox('Ispit vec postoji')
        self.ClearFields()
        self.RecalculateAverage()
        
    def toolExitOnToolClicked(self, event):
        res = wx.MessageDialog(None,'Da li zelite da izadjete',
                  'Info',   
                  wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION).ShowModal()
        if res == wx.ID_YES:
            self.Destroy()
    
    def MainFrameOnClose(self, event):
        res = wx.MessageDialog(None,'Da li zelite da izadjete',
                  'Info',   
                  wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION).ShowModal()
        if res == wx.ID_YES:
            self.Destroy()
    
    def toolCalculateOnToolClicked(self, event): 
        t = self.CalculateAll()     
        wx.MessageBox("""
            Vas ukupan prosek iznosi: %(avg).2f
            A ukupni ESBP: %(esbp)d
        """ % {'avg':t[0],'esbp':t[1]}, 'Info')
        
        
    def ListGradesFirst_OnListItemSelected(self, event):
        self.selectedItem = event.GetSelection()
        
        item = self.list[self.activeYear][self.selectedItem]
        self.txtSubject.Value = item.Subject
        self.spinGrade.Value = item.Grade
        self.spinESBP.Value = item.ESBP
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
        self.Updating = False
        self.RecalculateAverage()
        
    def RecalculateAverage(self):
        if len([item for sublist in self.list for item in sublist]) > 0:
            avg = []
            for i in range(0,4):
                gradeSum = []
                esbpSum = []
                angByYear = float(0)
                for it in self.list[i]:
                    gradeSum.append(it.Grade)
                    esbpSum.append(it.ESBP)
                if len(gradeSum) > 0:
                    angByYear = float(sum(gradeSum))/len(gradeSum)
                avg.append((angByYear,sum(esbpSum)))
            for c in range(0,4):
                self.tabNotebook.GetPage(c).GetChildren()[3].SetLabel('%.2f (%d)' % avg[c])            
            
    def CalculateAll(self):
        flatList = [item for sublist in self.list for item in sublist]
        x ,y = 0 ,0
        if len(flatList)>0:
            flatGrade = [i.Grade for i in flatList]
            flatESBP = [i.ESBP for i in flatList]
            x = float(sum(flatGrade))/len(flatGrade)
            y = sum(flatESBP)
        return x, y
if __name__ == '__main__':
    a = wx.App()
    g = GUIOverride(None)
#    g.Maximize()
    g.Show()
    a.MainLoop()
