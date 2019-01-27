import os, json, random, datetime, copy

from flask import Flask, url_for, redirect, request, render_template, request, jsonify
from random import seed, randint
from copy import deepcopy

app = Flask(__name__)
#set of events, each one is a dict
entries = {'1' : ["1/2", "dgaf", "female", 5000, 16920], '2' : ["1/4", "white", "male", 20000, 86372], 
           '3' : ["3/4", "color", "male", 100, 4782]}

# ls = [[90, "load", "color", "gender", 90, 234]]
entryIdToName = {'0' : "JASON is a genius", '1' : "Stephen King's It", '3' : "adopted children"}
ids = {"username" : "success"}

@app.route('/create_match', methods=['POST'])
def create_match():
    req_data = request.get_json()
    
    username = req_data['username']
    userStartTime = req_data['startTime']
    userEndTime = req_data['endTime']
    userLoad = req_data['load']
    userColor = req_data['color']
    userGender = req_data['gender']
    
    currentDT = datetime.datetime.now()
    seed(currentDT)
    r = randint(1,21)
    x = True

    while x:
        if r in entryIdToName:
            r = randint(1, 21)
        else:
            x = False
        
    # newEntry = [userLoad, userColor, userGender, userStartTime, userEndTime]
    # entryIdToName.update({r : username})
    # ls.update({r : newEntry})
    return jsonify({})
    

@app.route('/match_success/<eventId>')
def match_success(eventId):
    entryId = int(eventId)
    username = entryIdToName[entryId]
    chosenOne = entries[entryId]
    return json.dumps({"success" : True, username : chosenOne})
    #how the fuck do i change the app to another damn page

@app.route('/match_failure')
def match_failure():
    arrayEntries = []
    for key, value in entries.items():
        valueCopy = []
        valueCopy.append(key)
        for i in range(len(value)):
            valueCopy.append(value[i])
        arrayEntries.append(valueCopy)
    return json.dumps({"success" : False, "foreversingle" : arrayEntries})

@app.route('/')
def default():
    return "Welcome"

@app.route('/match', methods=['POST'])
def match():
    req_data = request.get_json()

    from pprint import pprint
    pprint(req_data)

    userStartTime = None
    userEndTime = None
    userColor = None
    userLoad = None
    userGender = None

    if 'startTime' in req_data:
        userStartTime = req_data['startTime']
    if 'endTime' in req_data:
        userEndTime = req_data['endTime']
    if 'color' in req_data:
        userColor = req_data['color']
    if 'load' in req_data:
        userLoad = req_data['load']
    if 'gender' in req_data:
        userGender = req_data['gender']
    
    for entry, args in entries.items():
        startTime = args[3]
        endTime = args[4]
        maxStartTime = max(startTime, userStartTime)
        minEndTime = min(endTime, userEndTime)
        if maxStartTime < minEndTime:
            load = args[0]
            color = args[1]
            gender = args[2]
            if load == userLoad and color == userColor and gender == userGender:
                intEntry = int(entry)
                entries.pop(intEntry)
                entryIdToName.pop(intEntry)
                return redirect(url_for('match_success', eventId=intEntry))
    
    return redirect(url_for('match_failure'))
    #return redirect(url_for('match_success', eventId=id))

if __name__ == "__main__":
    app.run(debug=True)

