#### import
import main as mm
import importlib as r
# get the sheets
print("*** get the sheet")
sheet = mm.googleDocReadIn()
records_df, wordsStat, words_array, meaning_array, stats_data, stat, help_array = mm.wordsSheet(sheet)
# handle empty cells in meaning and help arrays
meaning_array, help_array= mm.emptyCellsHandler(words_array, meaning_array, help_array)
# get rid of known words
daysInt = 62
words_array, meaning_array, help_array, numbersQuiz = mm.deleteKnownWords(wordsStat, words_array, meaning_array, help_array, days=daysInt)
# user inputs - how many questions, how many possible answers
print(" *** INFO: if you want to quit type 100 into the input field")
print(" How many words? ")

# This part is hard coded now
#numberOfQuestions = mm.userInputValidator(100)
#print(" how many possible answers? ")
#numberWrongAnswers = mm.userInputValidator(100)
#print("*** making the quiz")

numberOfQuestions, numberWrongAnswers = 3, 10
# make quiz
quizQ, possibleWrongAnswers = mm.questions(words_array, meaning_array, help_array, numbersQuiz, length=numberOfQuestions)

def quizF (quizQ, possibleWrongAnswers,numberWrongAnswers):
    for i in quizQ:
        question = i[0]
        goodAnswer = i[1]
        helP = i[2]
        # define x wrong answer
        # print("-------- quizF ", question, goodAnswer)
        mm.random.shuffle(possibleWrongAnswers)
        wrongAnswers = possibleWrongAnswers[0:numberWrongAnswers]
        mapAnswers(question, goodAnswer, helP, wrongAnswers, numberWrongAnswers)
        # print(question, goodAnswer, " ::: wrong ones ::: ", wrongAnswers)
        
def mapAnswers(question, goodAnswer, helP, wrongAnswers, numberWrongAnswers):
    q = [] #variable for all answers
    q.append(goodAnswer)
    dicT = {}
    # print("Q: ", question, " A: ", goodAnswer, " H: ", helP)
    ######## until here it is good
    for i in wrongAnswers:
        q.append(i)
    mm.random.shuffle(q)
    #print("## q is this: ", q)
    n = range(1,numberWrongAnswers+2)
    ######## until here it is good
    for n, a in zip(n, q):
        # n=number, a=corresponding answer
        # print(n, "  ", a)
        dicT[n] = a
    
    answeringF(dicT,goodAnswer, helP, question) ### unlock it after the help is done
    return None


def goodAnswerDictWrite(question, goodAnswer):
    print("Good answer! ")
    print(question, " : ",goodAnswer)
    goodAnswersDict[question] = int(mm.datetime.datetime.now().timestamp())
    return

def goodAnswerChecker(dicT, ans, goodAnswer):
    if dicT[ans] == goodAnswer:
        return True
    else:
        return False
    
def answeringF(dicT, goodAnswer, helP, question):
    print(question)
    # say it
    try:
        mm.speak(question)
    except:
        print("*** INFO: the sound card is used by an another app")
    
    # print(helP)
    # print the answers
    for i in dicT:
        print(i," - ", dicT[i])
    # answer
    ans = mm.userInputValidator(numberWrongAnswers+1)
    if goodAnswerChecker(dicT, ans, goodAnswer): #if the answer is good
        goodAnswerDictWrite(question, goodAnswer)
    else:
        # wrong answer, print help
        print("### Wrong answer, help: ", helP)
        ans = mm.userInputValidator(numberWrongAnswers+1)
        if goodAnswerChecker(dicT, ans, goodAnswer):
            goodAnswerDictWrite(question, goodAnswer)
        if goodAnswerChecker(dicT, ans, goodAnswer) == False:
            wrongAnswersDict[question] = int(mm.datetime.datetime.now().timestamp())
            print("Correct answer: ", goodAnswer)
            mm.webbrowser.open('https://www.collinsdictionary.com/dictionary/english/'+question)
            mm.webbrowser.open('https://docs.google.com/spreadsheets/d/1FLbb3hTuk6CV8IbjYAw1IF8ABTWY6T8ZTfneCiRJ2TM/')
            # print("::: MAPPED GOOD ANSWER IS: ", )
            # print(" ::: DICT :::: ", dicT)
            
# decleare an empty viaraible for the wrong answers

wrongAnswersDict = {}
goodAnswersDict = {}

quizF(quizQ, possibleWrongAnswers, numberWrongAnswers)

print("*** Update statistics sheet")
# append wrong and good answers
for i in wrongAnswersDict:
    wordsStat = wordsStat.append({'Word': i, "NOK":wrongAnswersDict[i], "OK":"" }, ignore_index=True)
for i in goodAnswersDict:
    wordsStat = wordsStat.append({'Word': i, "OK":goodAnswersDict[i], "NOK":"" }, ignore_index=True)

# update the sheet
stat.update([wordsStat.columns.values.tolist()] + wordsStat.values.tolist())
print("*** Bye!")
