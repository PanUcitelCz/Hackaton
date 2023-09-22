from flask import Flask, send_from_directory, request, Response

from pymongo import MongoClient
from types import SimpleNamespace
import json

import random

CONNECTION_STRING = "mongodb://98.71.99.77:27017/foodapp"
mongo = MongoClient(CONNECTION_STRING)

db = mongo.foodapp

def get_database():
   pass 


app = Flask(__name__)

# Leuze latlong: 49.7432394,13.4106877

@app.route("/add-review")
def add_review():
    reveiw = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))


@app.route("/register", methods=["POST", "GET"])
def register():
    user = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    if(db.users.find_one({"name": user.name}) is not None):
        return Response("User already exists!", status=400)
    

    db.users.insert_one({"name": user.name, "hash": user.hash})

    return Response("User created", status=201)


if __name__ == "__main__":
    app.run(debug=True)

