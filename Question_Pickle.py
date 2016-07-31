import pickle
import os
       
# Strips out white space that leaks in to list when iterating through txt file.   
def whiteSpace(listNam, val):
    return [value for value in listNam if value != val]

# Function to read lines of Question files and pass into a list. 
def questGenerator():
    question = []
    
    for file in fileList:
        
        quizFile = open (directory + quizFolder + file , 'r')
        for line in quizFile.readlines():
            for i in line.split('\n'):
                i.rstrip('\n')
                question.append(i)
                
    # Call of whitespace function explained above.
        question = whiteSpace(question, '')
        
    # Iterates through the list in blocks of 7 passing them to a temporary list
    # pickles the list and the deletes first 7 items in the list, loops and repeats
    # until list is exhausted.

        n = 1
        while len(question) >0:
            tempList = question[0:7]
            questFile = open(directory + '\\Quiz Questions\\'+ file +str(n)+'.p', 'wb')
            pickle.dump(tempList, questFile)
            questFile.close()
            del question[0:7]
            n+=1

#Folder directories, 

quizFolder = '\\Question Files\\'
directory = os.getcwd()
fileList = os.listdir(directory+quizFolder)

quizDirectory = os.listdir (directory)
print (quizDirectory)

print (fileList)

if 'Quiz Questions' not in quizDirectory:
    os.mkdir ('Quiz Questions')
    questGenerator()
else:
    questGenerator()
