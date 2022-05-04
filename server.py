from flask import Flask,render_template

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