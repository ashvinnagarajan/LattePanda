#this file works completely perfectly
#do not mess up this file

import pyrebase

config = {
    "apiKey": "AIzaSyAnFTWZTgWEugKOSUM6WY_NkxrPzRzn6dU",
    "authDomain": "bruin-racing.firebaseapp.com",
    "databaseURL": "https://bruin-racing.firebaseio.com",
    "projectId": "bruin-racing",
    "storageBucket": "bucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


db.child("speed").update({"1": 234234234234})

db.child("speed").update({"0": 23,
                          "1": 12,
                          "2": 1000,
                          "3": 2000})

