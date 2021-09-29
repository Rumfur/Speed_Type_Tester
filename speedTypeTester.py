from os.path import exists

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
    print(file.read())

checkConfig()
readConfig()
