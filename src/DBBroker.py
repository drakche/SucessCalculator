'''
Created on Jul 2, 2011

@author: drakChe
'''

import sqlite3
from DTO import *
dbase = 'Calc.db3'


def Insert(tupleList):
    conn = sqlite3.connect(dbase)
    
    c = conn.cursor()
    for tuple in tupleList:
        c.execute('insert into Exam(Name, Grade, ESBP, Year) values(?,?,?,?)',tuple)        
    conn.commit()
    c.close()

def Delete(exId):
    cn = sqlite3.connect(dbase)
    c = cn.cursor()
    c.execute('delete from Exam where ExamId=?',(exId,))
    cn.commit()
    c.close()
    
def Update(t):
    cn = sqlite3.connect(dbase)
    c = cn.cursor()
    c.execute("""
    updATE Exam
    set Name = ?, Grade = ?, ESBP = ?, Year = ?
    where ExamId = ?
    """, (t[1],t[2],t[3],t[4],t[0]))
    cn.commit()
    c.close()
    
def GetAll():
    cn = sqlite3.connect(dbase)
    c = cn.cursor()
    result = []
    c.execute('select ExamId,Name, Grade, ESBP, Year from Exam')
    for r in c:
        result.append(Exam(r[0], r[1], r[2], r[3], r[4] ))
    cn.commit()
    c.close()
    res2 = [[],[],[],[]]
    for ro in result:
        if ro.Year == 1:
            res2[0].append(ro)
        if ro.Year == 2:
            res2[1].append(ro)
        if ro.Year == 3:
            res2[2].append(ro)
        if ro.Year == 4:
            res2[3].append(ro)
    return res2   
        