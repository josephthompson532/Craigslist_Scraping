# Importing Dependencies
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import scraping

#Create Flask App.
app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/craigsdb"
mongo = PyMongo(app)

@app.route("/")

def index():
    items = mongo.db.items.find_one()
    return render_template("index.html", items=items)

@app.route("/scrape")

def scrape():
    city=request.args.get('city')
    item=request.args.get('item')
    items = mongo.db.items

    craigs_data = scraping.scrape_all(city, item)

    items.update({}, craigs_data, upsert=True)
    return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)
