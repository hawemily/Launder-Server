import os, json, random, datetime

from flask import Flask, url_for, redirect, request, render_template, request, jsonify
from random import seed, randint

app = Flask(__name__)
#set of events, each one is a dict
entries = {"eventid" : ["load", "color", "gender", 90, 234]}
lss = [["eventId", "load", "color", "gender", 90, 234]]

ls = [[90, "load", "color", "gender", 90, 234]]
userIdToName = {"userId" : "username"}

@app.route('/create_match', methods=['POST'])
def create_match():
    req_data = request.get_json()
    
    username = req_data['username']
    userStartTime = req_data['startTime']
    userEndTime = req_data['endTime']
    userLoadSize = req_data['loadSize']
    userColor = req_data['color']
    userGender = req_data['gender']
    
    # currentDT = datetime.datetime.now()
    # seed(currentDT)
    # r = randint(1,21)
    # x = True

    # while x:
    #     if r in userIdToName:
    #         r = randint(1, 21)
    #     else:
    #         x = False
        
    # newEntry = [r, userLoadSize, userColor, userGender, userStartTime, userEndTime]
    # userIdToName.update({r : username})
    # ls.append(newEntry)
    return jsonify({})
    

@app.route('/match_success/<eventId>')
def match_success(eventId):
    # username = userIdToName[eventId] 
    # for entry in ls:
    #     entry.pop(5)
    #     entry.pop(4)
    #     entry.pop(0)
    # for entry in ls:
    #     ls.append(username)
    return jsonify({"success" : True})
    #how the fuck do i change the app to another damn page

@app.route('/match_failure')
def match_failure():
    # for entry in ls:
    #     entry.pop(5)
    #     entry.pop(4)
    #     entry.pop(0)
    return json.dumps({"success" : False})

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
    userLoadSize = None
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
    id = "dont"
    for i in range(len(ls)):
        startTime = ls[i][4]
        endTime = ls[i][5]
        id = ls[i][0]
        maxStartTime = max(startTime, userStartTime)
        minEndTime = min(endTime, userEndTime)
        if maxStartTime < minEndTime:
            load = ls[i][1]
            color = ls[i][2]
            gender = ls[i][3]
            if load == userLoad and color == userColor and gender == userGender:
                ls.pop(i)
                userIdToName.pop(id)
                return redirect(url_for('match_success', eventId=id))
    
    return redirect(url_for('match_success', eventId=id))
    #return redirect()

if __name__ == "__main__":
    app.run(debug=True)

