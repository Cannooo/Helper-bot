import time
import cv2
import mss
import numpy
import pytesseract
import sys
import wikipedia

#Gets Question 

grabQuestion = (29, 158, 516, 275)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        imq = numpy.asarray(sct.grab(grabQuestion))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        textqDirty = pytesseract.image_to_string(imq)
        stopwords = ["who", "what", "when", "of", "and", "that", "have", "the", "why", "the", "on", "with", "as", "this", "by", "from", "they", "a", "an", "and", "my", "are", "in", "to", "these", "is", "does", "which", "his", "her", "also", "have", "it", "not", "we", "means", "you", "comes", "came", "come", "about", "if", "by", "from", "go", "?", ",", "!", "'", "has",]
        Dirtywords = textqDirty.split()

        resultwords = [word for word in Dirtywords if word.lower() not in stopwords]
        textq = ' '.join(resultwords) 
        print(textqDirty)

        Number = Number - 1

time.sleep(1)

#Gets Option 1

grabOption1 = (31, 288, 509, 346)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im1 = numpy.asarray(sct.grab(grabOption1))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text1 = pytesseract.image_to_string(im1)

        Number = Number - 1

#Gets Option 2

grabOption2 = (33, 346, 512, 402)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im2 = numpy.asarray(sct.grab(grabOption2))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text2 = pytesseract.image_to_string(im2)

        Number = Number - 1

#Gets Option 3

grabOption3 = (32, 402, 511, 462)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im3 = numpy.asarray(sct.grab(grabOption3))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text3 = pytesseract.image_to_string(im3)

        Number = Number - 1

q1point = 0
q2point = 0
q3point = 0


#Searches the question

Questions = wikipedia.page(textq)

Question1 = Questions.links

#Count how many times each come up in the Question

OptionOne = wikipedia.page(text1)

OptionOne1 = OptionOne.links

####

OptionTwo = wikipedia.page(text2)

OptionTwo2 = OptionTwo.links

###

OptionThree = wikipedia.page(text3)

OptionThree3 = OptionThree.links

for w in Question1:
    q1point += OptionOne1.count(w)
    q2point += OptionTwo2.count(w)
    q3point += OptionThree3.count(w)

#Count how many time Option 1 shows up in the text

for word in Question1:
    if word == text1:
        q1point += 1
        
#Count how many times Option 2 shows up in the text

for word in Question1:
    if word == text2:
        q2point += 1
        

#Count how many times Option 3 shows up in the text

for word in Question1:
    if word == text3:
        q3point += 1

#Prints the points

print("The question is: \n", textq)
print(" ")
print(text1, "gets", (q1point), "Points")
print(" ")
print(text2, "gets", (q2point), "Points")
print(" ")
print(text3, "gets", (q3point), "Points")




