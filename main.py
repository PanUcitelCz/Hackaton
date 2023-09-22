from flask import Flask, send_from_directory, request, Response


from pymongo import MongoClient
from types import SimpleNamespace

import json
from hashlib import sha512 

CONNECTION_STRING = "mongodb://98.71.99.77:27017/foodapp"
mongo = MongoClient(CONNECTION_STRING)

db = mongo.foodapp

def get_database():
   pass 


app = Flask(__name__)

# Leuze latlong: 49.7432394,13.4106877

@app.route("/add-review", methods=["POST", "GET"])
def add_review():
    review = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))
    db.reviews.insert_one({"user_id": review.user_id, "rating": review.rating})

    return Response("User created", status=201)


@app.route("/authenticate-user", methods=["POST", "GET"])
def authenticate_user():
    user = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    db.users.find_one({})
    



@app.route("/register", methods=["POST", "GET"])
def register():
    user = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    if(db.users.find_one({"name": user.name}) is not None):
        return Response("User already exists!", status=400)
    
    db.users.insert_one({"name": user.name, "hash": sha512(user.password)})

    return Response("User created", status=201)


if __name__ == "__main__":
    app.run(debug=True)

