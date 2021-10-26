from os import write
from os.path import exists
#from speedTypeTester import *
import logging
import sqlite3
import certifi
import pymongo
from time import perf_counter
import random

def addDBvalues():
    conn = sqlite3.connect('speedTypeDB.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS results')

    cur.execute('CREATE TABLE results (NR INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, username TEXT NOT NULL UNIQUE, typeSpeed INTEGER)')
    cur.execute('INSERT INTO results (NR, username, typeSpeed) VALUES (?, ?, ?)', (1, 'Vasja', 60))
    conn.close()

ca = certifi.where()
myclient = pymongo.MongoClient('mongodb+srv://Pukitis:<Student007>@speedtypecluster.jk8qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
mydb = myclient["SpeedTypeCluster"]
mycol = mydb["SpeedTypeCluster"]

addDBvalues()

logger = logging.getLogger(logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))

def writeConfig(): # Writes config file lines
    file = open("config.txt", "a")
    file.write("Testing writing!\n")
    file.write("I wonder what i'll write here.")
    file.close()

def checkConfig():
    if not(exists("config.txt")):
        file = open("config.txt","x") # Makes config file, if doesn't exist
        writeConfig()

def readConfig():
    file = open("config.txt", "r") # Reads config file
    return file.read()

checkConfig()
logger.info(readConfig())

#ACTUAL PROJECT STARTS HERE


confDict = {}
confDict[0] = "banana"
confDict[1] = "nonana"
confDict[2] = "house"
confDict[3] = "crayon"
print(len(confDict))

choice= ""
while choice != "Start":
    print("Write \"Start\" to start test.")
    choice = input()

print("The test has started")

count = 0
inputWord = ""
timerStart = perf_counter()

x = random.sample(range(0,len(confDict)),1)
print(x)
while count != 10:
    word = confDict[random.sample(range(0,len(confDict)),1)[0]]
    while inputWord != word:
        print("Write "+word+"!")
        inputWord = input()
        count += 1


timerStop = perf_counter()
print("Time is : ",(timerStop-timerStart))