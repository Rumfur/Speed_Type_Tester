from os import write
from os.path import exists
from configMaker import *
from databaseMaker import *
from time import perf_counter
import random

createLocalDBTables()

checkConfig()

wordDict = {}
wordDict[0] = "banana"
wordDict[1] = "telephone"
wordDict[2] = "house"
wordDict[3] = "crayon"
wordDict[4] = "street"
wordDict[5] = "backpack"
wordDict[6] = "hammer"
wordDict[7] = "grapefruit"
wordDict[8] = "ball"
wordDict[9] = "match"

choice = ""
while choice != "Start":
    print("\nThis is a speed typing test. You will have to write the words that are printed out in the console.\nWrite \"Start\" to start test.")
    choice = input()

count = -1
inputWord = ""
characterCount = 0
timerStart = perf_counter()
mistakes = 0

while count < 1:
    word = wordDict[random.sample(range(0, len(wordDict)), 1)[0]]
    attempts = 0
    while inputWord != word:
        if attempts > 0:
            mistakes += 1
        attempts += 1
        print("Write \""+word+"\"!")
        inputWord = input()
    count += 1
    characterCount += len(word)


timerStop = perf_counter()
time = timerStop-timerStart
speed = characterCount / time

print("Time is : ", time, "!")
print("You write at a speed of ", speed, " haracters per second!")
print("You made ", mistakes, " mistakes!")

username = ""
while len(username)<3:
    print("Please insert your username! (Must be atleast 3 characters long)")
    username = input()

addDataPymongo(username, speed)
MigrateData()