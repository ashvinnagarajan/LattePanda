import pyrebase
import time
import serial
from datetime import datetime

config = {
    "apiKey": "AIzaSyAnFTWZTgWEugKOSUM6WY_NkxrPzRzn6dU",
    "authDomain": "bruin-racing.firebaseapp.com",
    "databaseURL": "https://bruin-racing.firebaseio.com",
    "projectId": "bruin-racing",
    "storageBucket": "bucket.appspot.com"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

trialName = db.child("Latest Trial").get()
trialName = trialName.val().split()
num = int(trialName[1]) + 1
trialName = trialName[0] + " " + (str(num))
timeName = ""

newCurrent = 99
newVolt = 99
newLat = 99
newLong = 99
newSpeed = 99
newRPM = 99

while (True):
  teensy = serial.Serial('/dev/lexi', baudrate = 9600, timeout = 1)
  nano = serial.Serial('/dev/oliver', baudrate = 9600, timeout = 1)
  
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  previousTime = timeName
  timeName = current_time
  lapNumber = db.child("Lap").get()
  lapNumber = lapNumber.val()
  lapRunning = db.child("Running").get()
  lapRunning = lapRunning.val()
  
  teensyInput = teensy.readline().decode('ascii')
  if (teensyInput[0:3] == "Rpm"):
      newRPM = (teensyInput[5:10])
  teensyInput = teensy.readline().decode('ascii')
  if (teensyInput[0:3] == "Spd"):
      newSpeed = float(teensyInput[5:10])
  teensyInput = teensy.readline().decode('ascii')
  if (teensyInput[0:3] == "Lng"):
      newLong = float(teensyInput[5:10])
  teensyInput = teensy.readline().decode('ascii')
  if (teensyInput[0:3] == "Lat"):
      newLat = float(teensyInput[5:10])

   # res = teensy.readline().decode('ascii')
   # newLat = res
   # res = teensy.readline().decode('ascii')
   # newLong = res
   # res = teensy.readline().decode('ascii')
   # newSpeed = res
   # res = teensy.readline().decode('ascii')
   # newRPM = res
   
  nanoInput = nano.readline().decode('ascii')
  if (nanoInput[0:3] == "Cur"):
      newCurrent = float(nanoInput[5:10])

  nanoInput = nano.readline().decode('ascii')
  
  if (nanoInput[0:3] == "Vlt"):
      newVolt = float(nanoInput[5:10])
   # res = nano.readline().decode('ascii')
   # newVolt = res
   # res = nano.readline().decode('ascii')
   # newCurrent = res

  newPower = newCurrent*newVolt
  
    # newLat = 6
    # newLong = 5
    # newSpeed = 4
    # newRPM = 3
    # newVolt = 1
    # newCurrent = 1.1
    # newPower = newVolt*newCurrent

  db.update(
        {"Latest Trial": trialName,
        "Latest Time": timeName,
         "Previous Time": previousTime})
  
  db.child(trialName).child(timeName).child("battery").update(
        {"amp": 0,
        "remaining": 0,
        "temp": 0,
        "volt": 0})
  
  db.child(trialName).child(timeName).child("driver").update(
        {"image": "./images/Caroline.jpg",
        "message": "I Believe In You!!!",
        "name": "Caroline",
        "phone": "999-999-999",
        "social": "@CarolineDriver"})

  db.child(trialName).child(timeName).child("gps").update(
        {"lat": newLat,
        "long": newLong})
  
  db.child(trialName).child(timeName).child("joulemeter").update(
        {"amp": newCurrent,
        "avg": 0,
        "instant": newPower,
        "peak": 0,
        "volt": newVolt})

  db.child(trialName).child(timeName).child("lap").update(
        {"current": lapNumber,
        "fastest": 0,
        "number": 0,
        "remaining": 0,
        "slowest": 0,
        "total": 0,
        "running": lapRunning})
  
  db.child(trialName).child(timeName).child("motor").update(
        {"bhp": 0,
        "temp": 0,
        "volt": 0})

  db.child(trialName).child(timeName).child("speed").update(
        {"acceleration": 0,
        "avg": 0,
        "rpm": newRPM,
        "speed": newSpeed,
        "throttle": 0})
  
  db.child(trialName).child(timeName).child("track").update(
        {"name": "Parking Garage",
        "trial": 1,})
  
