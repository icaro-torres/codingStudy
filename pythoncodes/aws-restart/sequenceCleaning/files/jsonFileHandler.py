""" 
basically i did this code all wrong, so i will try to fix it

import json

def readJsonFile(fileName):
    data=""
    # problematic line
    with open('sequenceCleaning/insulin.json') as json_file:
        data = json.load(json_file)
    return data

import json

def readJsonFile(fileName):
    data = ""
    try:
        # another problematic line (this was just for a try/except line, i didn't need to do it)
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file: " + fileName)
    return data
"""
# above code is not needed, so i will just write a simple function to read the json file

import json

def readJsonFile(fileName):
    data = ""
    try:
        # here you will use the argument fileName to read the json file
        # this means the function 'readJsonFile' will try to open and read the file
        # what is passed as fileName
        with open(fileName, 'r') as json_file: # added 'r' mode for clarity
            # if the file is opened successfully, it will load the json data
            data = json.load(json_file)
    except IOError:
        # added the fileName to the error message to debug easier
        print("Could not read file: " + fileName)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {fileName}. Check file content.")
    return data