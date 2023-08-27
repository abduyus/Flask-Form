from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

@app.route('/', methods=["GET", 'POST'])
def index():
    """index method"""
    
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]
        
    return render_template("index.html")


app.run(debug=True, port=1406)
