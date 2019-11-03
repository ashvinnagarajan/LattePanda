#this file works completely perfectly
#do not mess up this file

import pyrebase
import time
import serial

config = {
    "apiKey": "AIzaSyAnFTWZTgWEugKOSUM6WY_NkxrPzRzn6dU",
    "authDomain": "bruin-racing.firebaseapp.com",
    "databaseURL": "https://bruin-racing.firebaseio.com",
    "projectId": "bruin-racing",
    "storageBucket": "bucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

trialName = "Trial 2"
timeName = "12:00:00"

while (True):
    s = serial.Serial('COM6', baudrate = 9600, timeout = 1)

    res = s.readline().decode('ascii')
    newLat = res
    res = s.readline().decode('ascii')
    newLong = res
    res = s.readline().decode('ascii')
    newSpeed = res
    res = s.readline().decode('ascii')
    newVolt = res
    res = s.readline().decode('ascii')
    newCurrent = res
    res = s.readline().decode('ascii')
    newPower = res
    res = s.readline().decode('ascii')
    newRPM = res

    db.update(
        {"Latest Trial": trialName,
        "Latest Time": timeName})

    db.child(trialName).child(timeName).child("gps").update(
                            {"lat": newLat,
                            "long": newLong})

    db.child(trialName).child(timeName).child("joulemeter").update(
                            {"amp": newCurrent,
                            "avg": 0,
                            "instant": newPower,
                            "peak": 0,
                            "volt": newVolt})

    db.child(trialName).child(timeName).child("speed").update(
                            {"acceleration": 0,
                            "avg": 0,
                            "brake": 0,
                            "speed": newSpeed,
                            "throttle": 0})
