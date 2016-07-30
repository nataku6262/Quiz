import pickle
import os

# List of Question files based on TKD rank to generate question binary files to be called in Quiz App

fileList = ['wbQuestion.txt','ytQuestion.txt', 'ybQuestion.txt']
       
# Strips out white space that leaks in to list when iterating through txt file.   
def whiteSpace(listNam, val):
    return [value for value in listNam if value != val]

# Function to read lines of Question files and pass into a list. 
def vinegar():
    question = []
    
    for file in fileList:
        n=1
        quizFile = open ('\\Question Files\\' + file, 'r')
        for line in quizFile.readlines():
            for i in line.split('\n'):
                i.rstrip('\n')
                question.append(i)
                
    # Call of whitespace function explained above.
        question = whiteSpace(question, '')
        
    # Iterates through the list in blocks of 7 passing them to a temporary list
    # pickles the list and the deletes first 7 items in the list, loops and repeats
    # until list is exhausted.
	
        while len(question) >0:
            tempList = question[0:7]
            questFile = open('\\Quiz Questions\\'+ file +str(n)+'.p', 'wb')
            pickle.dump(tempList, questFile)
            questFile.close()
            del question[0:7]
            n+=1

vinegar()
