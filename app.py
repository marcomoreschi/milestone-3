import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] ='marco_cook'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-z4c90.mongodb.net/marco_cook?retryWrites=true&w=majority'

mongo =PyMongo(app)

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)