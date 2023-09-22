from flask import Flask, send_from_directory

from pymongo import MongoClient

import random

CONNECTION_STRING = "mongodb://localhost:27017"

def get_database():
   pass 


app = Flask(__name__)

# Leuze latlong: 49.7432394,13.4106877

@app.route("/register", methods=["POST", "GET"])
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)

