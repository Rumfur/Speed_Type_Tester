import os
import certifi
import pymongo
from random_word import RandomWords
from configparser import ConfigParser

print("Configuration file test")

# Testing if configuration file exists on disk in the current working directory
print("----------")
print("Checking if config file exists -->")
assert os.path.isfile("config.txt") == True
print("OK")
print("----------")

# Opening the configuration file
config = ConfigParser()
config.read('config.txt')

# Checking if all NEWS API  related config options are present in the config file
print("Checking if config has NEWS API related options -->")
assert config.has_option('MONGODB', 'username') == True
assert config.has_option('MONGODB', 'password') == True
assert config.has_option('MONGODB', 'cluster') == True
assert config.has_option('MONGODB', 'database') == True
print("OK")
print("----------")

# Checking if programm receaves words from RandomWords API
print("Checking if programm receaves words from RandomWords API -->")
r = RandomWords()
words = r.get_random_words(hasDictionaryDef="true", limit=5)
assert (len(words) > 0) == True
print("OK")
print("----------")

# Checking if possible to connect to MongoDb with the existing config options
print("Checking if it is possible to connect to MongoDb with the given config options -->")
ca = certifi.where()
mongodb_user = config.get('MONGODB', 'user')
mongodb_password = config.get('MONGODB', 'password')
mongodb_cluster = config.get('MONGODB', 'password')
mongodb_database = config.get('MONGODB', 'dataBase')
connection = pymongo.MongoClient(
    f'mongodb+srv://{mongodb_user}:{mongodb_password}@{mongodb_database}.ray5r.mongodb.net/{mongodb_database.capitalize()}?retryWrites=true&w=majority', tlsCAFile=ca)
serverData = connection.admin.command('ismaster')

assert serverData["ismaster"] == True

print("OK")
print("----------")

# Checking if log file exist
print("Checking if DB migration component log config file exists log_migrate_db.yaml -->")
assert os.path.isfile("logfile.log") == True
print("OK")
print("----------")

print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")