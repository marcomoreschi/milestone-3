import os
if os.path.exists('env.py'):
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
    recipes=mongo.db.cook_recipe.find().limit(3)
    return render_template("index.html", recipes=recipes)

#////////////////////////////////////////////////# Add Thanks page 
@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


#////////////////////////////////////////////////# Add recipe page
@app.route('/add_recipe')
def add_recipe():
    title = mongo.db.recipe_title.find()
    cuisines = mongo.db.cuisine_recipe.find()
    type_cuisines = mongo.db.type_recipe.find()
    return render_template("addrecipe.html",
    cuisines= cuisines, type_cuisines=type_cuisines, title=title)

    
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
    search = request.form.get('search_recipe_title').lower()
    print(search)
    recipe_title_search = mongo.db.cook_recipe.find({"recipe_title": {"$regex": f'.*{search}.*'}})
    return render_template("search_recipe_title.html", recipes=recipe_title_search)


@app.route('/the_recipes/<recipe_id>')
def the_recipes(recipe_id):
    the_recipes = mongo.db.cook_recipe.find({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.find({'_id': ObjectId(recipe_id)})
    return render_template("the_recipes.html", recipe=the_recipes)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)