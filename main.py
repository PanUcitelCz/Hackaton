from flask import Flask, send_from_directory, request, Response
from flask_cors import CORS

from pymongo import MongoClient
from types import SimpleNamespace
import requests
import json
from hashlib import sha512 
from uuid import uuid4

CONNECTION_STRING = "mongodb://98.71.99.77:27017/foodapp"
mongo = MongoClient(CONNECTION_STRING)

db = mongo.foodapp

app = Flask(__name__)
CORS(app)

# Leuze latlong: 49.7432394,13.4106877

@app.route("/add-review", methods=["POST", "GET"])
def add_review():
    review = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))
    
    if(db.locations.find_one({"location_id": review.location_id}) is None):
        db.locations.insert_one({"location_id": review.location_id, "zumpy": 0, "visit-count": 0 })

    db.reviews.insert_one({"user_id": review.user_id, "rating": review.rating})

    return Response("Review added", status=201)


@app.route("/authenticate-user", methods=["POST", "GET"])
def authenticate_user():
    user = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    db_user = db.users.find_one({"name": user.name})
    if db_user == None:
        return Response("User not found", status=404)


    print(f"{db_user.get('hash')} got {sha512(user.password.encode('utf-8')).digest()}")

    if db_user.get("hash") == sha512(user.password.encode('utf-8')).digest():
        response = Response(json.dumps({"session_id": uuid4().hex}), status=200)
        response.headers["Content-Type"] = "application/json"
        return response 

    else:
        return Response("Wrong password", status=401)
    



@app.route("/register", methods=["POST", "GET"])
def register():
    user = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    if(db.users.find_one({"name": user.name}) is not None):
        return Response("User already exists!", status=400)
    
    db.users.insert_one({"name": user.name, "hash": sha512(user.password.encode('utf-8')).digest()})

    response = Response(json.dumps({"session_id": uuid4().hex}), status=201)
    response.headers["Content-Type"] = "application/json"
    return response 


@app.route("/find-voted", methods=["POST"])
def find_voted():
    data = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    all_votes = db.votes.find({})



@app.route("/remove-vote", methods=["POST"])
def remove_vote():
    vote = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    db.votes.delete_one({"user_id": vote.user_id, "location_id": vote.location_id})
    return Response(status=200)

@app.route("/add-vote", methods=["POST"])
def add_vote():
    
    print(request.get_data())
    vote = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))

    if db.votes.find_one({"location_id": vote.location_id, "user_id": vote.username}):
        return Response(status=401)

    if(db.locations.find_one({"location_id": vote.location_id}) == None):
        db.locations.insert_one({"location_id": vote.location_id, "zumpy": 0, "visit-count": 0 })
        
    db.votes.insert_one({"location_id": vote.location_id, "user_id": vote.username, "vote_time": vote.time})

    print("added vote!!!!!!!!!!!!!!!")
    return Response(status=200)

@app.route("/find-closest", methods=["GET"])
def find_closest():
    Headers={"Referer":"https://foodapp.com/","accept":"application/json"}
    x=requests.get('https://api.content.tripadvisor.com/api/v1/location/nearby_search?latLong=49.7432394%2C13.4106877&key=06071D2668FF4DE3B82432788FF07AE8&language=en',headers=Headers);
    found_locations = x.json().get("data")
    print(found_locations)

    for i, location in enumerate(found_locations):
        db_location = db.locations.find_one({"location_id": location.get("location_id")})

        if db_location:
            average = 0
            count = 0
            vote_count = 0

            for vote in db.votes.find({"location_id": location.get("location_id")}):
                vote_count += 1

            for review in db.reviews.find({}):
                if location.get("location_id") == review.get("location_id"):
                    average += review.get("rating")
                    count += 1

            if count > 0:
                average = average/count
            else:
                average = 0

            found_locations[i]["zumpy"] = db_location.get("zumpy")
            found_locations[i]["kadiboudy"] = db_location.get("kadiboudy")
            found_locations[i]["visit_count"] = db_location.get("visit_count")
            found_locations[i]["vote_count"] = vote_count
            found_locations[i]["average"] = average

        else:
            found_locations[i]["zumpy"] = 0
            found_locations[i]["kadiboudy"] = 0
            found_locations[i]["visit_count"] = 0
            found_locations[i]["average"] = 0
            found_locations[i]["vote_count"] = 0
            found_locations[i]["average"] = 0

        #print(location)
        #print(db_location)

    #data = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))
    #print(x.json())
    
    msg = Response(json.dumps(found_locations), status=200)
    msg.headers["Content-Type"] = "application/json"

    print(json.dumps(found_locations))
    return msg

if __name__ == "__main__":
    app.run(debug=True)

