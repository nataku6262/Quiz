#Test of generating a question whilst drawing from the pickled file.

# 1.1 version
# Attempting to put in random number generator that will form the base of quiz

# 1.2 Version
# Replace random number generator with randomly selecting file name a generated by
# questList Function

# 1.3 Version
# If Else function to select questions based on Grade

# 1.4 Version
# Fleshing out the elif statement for grade selection.

# 1.5 Version
# Introducing a for loop to determine possible answer placement. 

import pickle
import random
import os

def questList(fileName):
    quiz = []
    for file in os.listdir ('\\Quiz Questions'):
        if file.startswith (fileName):
            quiz.append(file)
    return quiz

# Libraries using questList for all the colour belt ranks,
# extends each new list with previous lists contents.

whiteBelt = questList('wb')

yellowTab = questList ('yt')
yellowTab.extend (whiteBelt)

yellowBelt = questList ('yb')
yellowBelt.extend (yellowTab)


# Function to determine the selection of questions to be used.

def rank():
    belt = input ('What grade are you? ')
    belt = belt.lower()

    if belt == '10' or belt == '10th kup' or belt =='white' or belt == 'white belt'\
       or belt == '10th' or belt == 'tenth' or  belt == 'tenth kup':
        return whiteBelt
    elif belt == '9' or belt == '9th kup' or belt =='yellow tab' \
       or belt == '9th' or belt == 'ninth' or  belt == 'ninth kup':
        return yellowTab
    elif belt == '8' or belt == '8th kup' or belt =='yellow belt' \
       or belt == '8th' or belt == 'eight' or  belt == 'eight kup':
        return yellowBelt
    else:
        print ('You need to actually select your rank! Try again!')
        rank()

# Quiz application 

def Quiz():

    userGrade = rank()
    score = 0
    numberQuestions = 3

    questList =[]
    
    while numberQuestions > 0:
        randUserGrade = random.choice(userGrade)

# If question file is not in the list ask question Else pick another question.
        if randUserGrade in questList:
            randUserGrade

        else:
            
            questList.append(randUserGrade)
            numberQuestions -=1
    
            quizQuest = pickle.load(open('\\Quiz Questions\\' + str(randUserGrade), 'rb'))
            questionLib = quizQuest

            question = questionLib[0]

        # Randomly assigns the order of the answers.
            v = random.sample (range (1,5),4)
            answer1 = questionLib[v[0]]
            answer2 = questionLib[v[1]]
            answer3 = questionLib[v[2]]
            answer4 = questionLib[v[3]]

            correct = questionLib[5]

            explanation = questionLib[6]


            print (question)

            print ('\t', answer1, '\n\t', answer2, '\n\t', answer3, '\n\t', answer4)

            response = input()

            if response == correct:
                print ('Correct')
                score += 1

            else:
                print ('That is incorrect:\n', explanation)

# Prints Users score out of number of questions asked.
    print ('Your final score is:', score, '/', (len(questList)))

Quiz()
