# start mongo in two anaconda prompts before starting this step (mongod, and mongo); both prompts must remain open

# Import Flask to render template, redirect to another url, and create a url
from flask import Flask, render_template, redirect, url_for
# import PyMongo to interact with Mongo DB
from flask_pymongo import PyMongo
# Import scrapping code that will be converted from jupyter to Python
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the html page


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# add next route and function


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


# tell Flask to run
if __name__ == "__main__":
    app.run()
