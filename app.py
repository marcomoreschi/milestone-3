import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] ='marco_cook'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-z4c90.mongodb.net/marco_cook?retryWrites=true&w=majority'

mongo =PyMongo(app)

#////////////////////////////////////////////////# Add Home Page
@app.route('/')
@app.route('/index')
def index():
    recipes=mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


#////////////////////////////////////////////////# Add saltimbocca 
@app.route('/saltimbocca')
def saltimbocca():
    return render_template("saltimbocca.html")


#////////////////////////////////////////////////# Add pasta alla norma
@app.route('/pastaallanorma')
def pastaallanorma():
    return render_template("pastaallanorma.html")


#////////////////////////////////////////////////# Add fish and chips
@app.route('/fishandchips')
def fishandchips():
    return render_template("fishandchips.html")


#////////////////////////////////////////////////# Add recipe page
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    cuisine=mongo.db.cuisine_recipe.type_recipe.find())





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)