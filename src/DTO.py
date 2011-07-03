'''
Created on Jul 2, 2011

@author: drakChe
'''
class Exam(object):    
    def __init__(self,examId=0, subject='', grade=0, esbp=0, year = 0):
        self.ExamId = examId
        self.Subject = subject
        self.Grade = grade
        self.ESBP = esbp
        self.Year = year
        
    def __repr__(self, *args, **kwargs):
        return '{0} - {1} ({2})'.format(self.Subject,str(self.Grade),str(self.ESBP))