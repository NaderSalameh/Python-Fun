import os,re

#importing my the txt file
txt_path = os.path.join('Resources','Pinocchio_Paragraph.txt')
with open(txt_path, 'r', encoding='utf-8') as file:

    #initializing the variables
    pinocchio = file.read()
    sentenceList = re.split("(?<=[.!?]) +", pinocchio)
    sentenceCount = len(sentenceList)
    totWords = len(pinocchio.split())

    #creating my lists 
    wordCount = []
    letterCount = []

    # cleaning out the paragraphs of all punctuation in order to get correct letter counts 
    pinocchio_clean = pinocchio.replace('.','')
    pinocchio_clean = pinocchio_clean.replace(',','')
    pinocchio_clean = pinocchio_clean.replace('"','')
    pinocchio_clean = pinocchio_clean.replace("'",'')
    pinocchio_clean = pinocchio_clean.replace(')','')
    pinocchio_clean = pinocchio_clean.replace('(','')

    # creating a couple of for loops to gather some word and letter counts and append my results to my lists above
    for i in (sentenceList):
        wordCount.append(len(i.split()))
        
    for l in pinocchio.split():
        letterCount.append(len(l))

#Creating an output text file 
output_path = os.path.join('Analysis', "Paragraph_Analysis.txt")
with open(output_path, 'w', newline='') as textfile:
    
    
    textfile.write(pinocchio)
    textfile.write("\n \n \n")
    textfile.write('Paragraph Analysis\n')
    textfile.write('--.----------.----------.----\n')
    textfile.write(f"Approximate Word Count: {totWords}\n")
    textfile.write(f"Approximate Sentence Count: {sentenceCount}\n")
    textfile.write(f"Average Letter Count: {round(sum(letterCount)/len(letterCount),2)}\n")
    textfile.write(f"Average Sentence Length: {round(sum(wordCount)/len(wordCount),2)} ")
