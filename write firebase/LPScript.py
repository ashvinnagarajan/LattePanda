import pyrebase
import time
import serial
from datetime import datetime

config = { #firebase authentification
    "apiKey": "AIzaSyAnFTWZTgWEugKOSUM6WY_NkxrPzRzn6dU",
    "authDomain": "bruin-racing.firebaseapp.com",
    "databaseURL": "https://bruin-racing.firebaseio.com",
    "projectId": "bruin-racing",
    "storageBucket": "bucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

trialName = db.child("Latest Trial").get() #trial name naming
trialName = trialName.val().split()
num = int(trialName[1]) + 1
trialName = trialName[0] + " " + (str(num))

newCurrent = -1 #default values
newVolt = -1
newLat = -1
newLong = -1
newSpeed = -1
newRPM = -1
newAltitude = -1
newTemp = -1
newGyroX = -1
newGyroY = -1
newGyroZ = -1
newAcX = -1
newAcY = -1
newAcZ = -1
newMagX = -1
newMagY = -1
newMagZ = -1
newPitch = -1
newRoll = -1
newHeading = -1

joulemeterStatements = 2 #number of statements from joulemeter
otherNanoStatements = 18 #number of statements from everything else

while (True):
  joulemeter = serial.Serial('/dev/oliver', baudrate = 9600, timeout = 1) #joulemeter Arduino
  otherNano = serial.Serial('/dev/lexi', baudrate = 9600, timeout = 1) #everything else Arduino

  now = datetime.now() #set time
  current_time = now.strftime("%H:%M:%S") #set current time
  timeName = current_time 

  lapNumber = db.child("Lap").get() #fetch lap number
  lapNumber = lapNumber.val()
  lapRunning = db.child("Running").get() #fetch running state
  lapRunning = lapRunning.val()

  for x in range (0, joulemeterStatements): #read joulemeter statements
  	  joulemeterInput = joulemeter.readline().decode('ascii')
  	  joulemeterInputPrefix = joulemeterInput[0:3]
  	  if (joulemeterInputPrefix == "Cur"):
  	  	newCurrent = float(joulemeterInput[5:-2])
  	  if (joulemeterInputPrefix == "Vlt"):
		newVolt = float(joulemeterInput[5:-2])

  newPower = newCurrent*newVolt

#  joulemeterInput = joulemeter.readline().decode('ascii')
#  if (joulemeterInput[0:3] == "Cur"):
#      newCurrent = float(joulemeterInput[5:10])
#  joulemeterInput = joulemeter.readline().decode('ascii')
#  if (joulemeterInput[0:3] == "Vlt"):
#      newVolt = float(joulemeterInput[5:10])

  for x in range (0, otherNanoStatements): #read otherNano statements
  	  otherNanoInput = otherNano.readline().decode('ascii')  
  	  otherNanoPrefix = otherNanoInput[0:3]
	  if (joulemeterInputPrefix == "Vlt"):
		newVolt = float(joulemeterInput[5:-2])
	  if (joulemeterInputPrefix == "Spd"):
  	  	newSpeed = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Lng"):
  	  	newLong = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Lat"):
  	  	newLat = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Alt"):
  	  	newAltitude = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Tem"):
  	  	newTemp = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "GyX"):
  	  	newGyroX = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "GyY"):
  	  	newGyroY = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "GyZ"):
  	  	newGyroZ = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "AcX"):
  	  	newAcX = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "AcY"):
  	  	newAcY = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "AcZ"):
  	  	newAcZ = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "MaX"):
  	  	newMagX = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "MaY"):
  	  	newMagY = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "MaZ"):
  	  	newMagZ = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Pit"):
  	  	newPitch = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Rol"):
  	  	newRoll = float(otherNanoInput[5:-2])
  	  if (joulemeterInputPrefix == "Hea"):
  	  	newHeading = float(otherNanoInput[5:-2])

#  otherNanoInput = otherNano.readline().decode('ascii')  
#  if (otherNanoInput[0:3] == "Rpm"):
#      newRPM = (otherNanoInput[5:10])
#  otherNanoInput = otherNano.readline().decode('ascii')
#  if (otherNanoInput[0:3] == "Spd"):
#      newSpeed = float(teensyInput[5:10])
#  otherNanoInput = otherNano.readline().decode('ascii')
#  if (otherNanoInput[0:3] == "Lng"):
#      newLong = float(otherNanoInput[5:10])
#  otherNanoInput = otherNano.readline().decode('ascii')
#  if (otherNanoInput[0:3] == "Lat"):
#      newLat = float(otherNanoInput[5:10])

  db.update(
        {"Latest Trial": trialName,
        "Latest Time": timeName})

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
        "volt": newVolt,
        "GyX": newGyroX,
        "GyY": newGyroY,
        "GyZ": newGyroZ,
        "Altitude": newAltitude})

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
        {"acceleration x": newAcX,
        "acceleration y": newAcY,
        "acceleration z": newAcZ,
        "avg": 0,
        "rpm": newRPM,
        "speed": newSpeed,
        "throttle": 0})

  db.child(trialName).child(timeName).child("track").update(
        {"name": "Parking Garage",
        "trial": 1,
        "temp": newTemp})

  db.child(trialName).child(timeName).child("IMU").update(
  		{"MagX": newMagX,
  		"MagY": newMagY,
  		"MagZ": newMagZ,
  		"Pitch": newPitch,
  	  	"Roll": newRoll,
  	  	"Heading": newHeading})