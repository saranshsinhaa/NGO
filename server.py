import csv
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index.html")
def home2():
    return render_template('index.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/volunteers.html")
def volunteers():
    return render_template('volunteers.html')

@app.route("/gallery.html")
def gallery():
    return render_template('gallery.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/form", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()
        database(data)
        return render_template("/form_submit.html")
        
        
    else:
        return "Something went wrong"

def database(data):
    with open("database.csv",newline='', mode="a") as database:
        name= data["name"]
        email= data["email"]
        message= data["message"]
        writer= csv.writer(database, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name,email,message])
