import pickle
import os

fileList = ['wbQuestion.txt','ytQuestion.txt', 'ybQuestion.txt']
       
def whiteSpace(listNam, val):
    return [value for value in listNam if value != val]

def vinegar():
    question = []
    
    for file in fileList:
        n=1
        quizFile = open ('\\Question Files\\' + file, 'r')
        for line in quizFile.readlines():
            for i in line.split('\n'):
                i.rstrip('\n')
                question.append(i)
                

        question = whiteSpace(question, '')
        
        while len(question) >0:
            tempList = question[0:7]
            questFile = open('\\Quiz Questions\\'+ file +str(n)+'.p', 'wb')
            pickle.dump(tempList, questFile)
            questFile.close()
            del question[0:7]
            n+=1

vinegar()
