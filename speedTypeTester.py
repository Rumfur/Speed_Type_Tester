from importInstaller import *
from os import write
from os.path import exists
from configMaker import *
from databaseMaker import *
from time import perf_counter
from random_word import RandomWords

installImports()

createLocalDBTables()

r = RandomWords()
words = r.get_random_words(hasDictionaryDef="true", limit=5)

choice = ""
while choice != "Start":
    print("\nThis is a speed typing test. You will have to write the words that are printed out in the console.\nWrite \"Start\" to start test.")
    choice = input()

count = -1
inputWord = ""
characterCount = 0
timerStart = perf_counter()
mistakes = 0

for word in words: #Goes through the words and asks the user to input them
    attempts = 0
    while inputWord != word:
        if attempts > 0:
            mistakes += 1
        attempts += 1
        print("Write \""+word+"\"!")
        inputWord = input()
    characterCount += len(word)

timerStop = perf_counter()
time = timerStop-timerStart
speed = characterCount / time

print("Time is : ", time, "!")
print("You write at a speed of ", speed, " haracters per second!")
print("You made ", mistakes, " mistakes!")

username = ""
while len(username)<3:
    print("Please insert your username!\n Username must be atleast 3 characters long and cannot contain \"@\" symbol!")
    username = input()
    if "@" in username:
        username = ""

addDataPymongo(username, speed, mistakes)
MigrateData()
#closeConnection