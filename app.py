import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] ='marco_cook'
app.config["MONGO_URI"] =  os.getenv("MONGO_URI")

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

#////////////////////////////////////////////////# Add saltimbocca 
@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


#////////////////////////////////////////////////# Add recipe page
@app.route('/add_recipe')
def add_recipe():
    cuisines = mongo.db.cuisine_recipe.find()
    type_cuisines = mongo.db.type_recipe.find()
    return render_template("addrecipe.html",
    cuisines= cuisines, type_cuisines=type_cuisines)

    
#////////////////////////////////////////////////# Button Add Recipe and send them to mongoDb
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.cook_recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('thanks')) 

#////////////////////////////////////////////////# Find Recipe 
@app.route('/search_recipe')
def search_recipe():
    recipes=mongo.db.recipes
    return render_template("search_recipe.html", recipes=recipes)


@app.route('/search_recipe_title', methods=['POST'])
def search_recipe_title():
    search = request.form.get('search_recipe_title')
    print(search)
    recipe_title_search = mongo.db.cook_recipe.find({"recipe_title": {"$regex": f'.*{search}.*'}})
    return render_template("search_recipe_title.html", recipes=recipe_title_search)


@app.route('/recipes')
def recipes():
    return render_template("recipes.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)