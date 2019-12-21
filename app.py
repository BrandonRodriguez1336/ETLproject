from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)


db = client.gender_gap
collection = db["2016"]

@app.route('/')
def index():              
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        x= request.form['Occupation']
        gender = collection.find({"Occupational_Category": x})
    
    return render_template('index.html',gender=gender)



if __name__ == "__main__":
    app.run(debug=True)