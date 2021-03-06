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

        textq = "What is the longest river in wales?"

        print(textq)

        Number = Number - 1

time.sleep(1)

#Gets Option 1

grabOption1 = (31, 288, 509, 346)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im1 = numpy.asarray(sct.grab(grabOption1))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text1 = "River Nile"

        Number = Number - 1

#Gets Option 2

grabOption2 = (33, 346, 512, 402)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im2 = numpy.asarray(sct.grab(grabOption2))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text2 = "River Severn"

        Number = Number - 1

#Gets Option 3

grabOption3 = (32, 402, 511, 462)

Number = 1

with mss.mss() as sct:
    while Number > 0:
        im3 = numpy.asarray(sct.grab(grabOption3))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text3 = "River Wye"

        Number = Number - 1

q1point = 0
q2point = 0
q3point = 0


#Searches the question

Questions = wikipedia.page(textq)

Question1 = Questions.links

#Count how many times each come up in the Question

links1 = [text1]
test=[]
for link in links1:
    try:
        #try to load the wikipedia page
        page=wikipedia.page(link, auto_suggest=False)
        test.append(page)
    except wikipedia.exceptions.PageError:
        #if a "PageError" was raised, ignore it and continue to next link
        continue

####

links2 = [text2]
test=[]
for link in links2:
    try:
        #try to load the wikipedia page
        page=wikipedia.page(link, auto_suggest=False)
        test.append(page)
    except wikipedia.exceptions.PageError:
        #if a "PageError" was raised, ignore it and continue to next link
        continue

###

links3 = [text3]
test=[]
for link in links3:
    try:
        #try to load the wikipedia page
        page=wikipedia.page(link, auto_suggest=False)
        test.append(page)
    except wikipedia.exceptions.PageError:
        #if a "PageError" was raised, ignore it and continue to next link
        continue

for w in Question1:
    q1point += links1.count(w)
    q2point += links2.count(w)
    q3point += links3.count(w)

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




