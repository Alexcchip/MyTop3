from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "12wwqewq3"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    band1 = db.Column(db.String(50), nullable=False)
    band2 = db.Column(db.String(50), nullable=False)
    band3 = db.Column(db.String(50), nullable=False)


@app.route('/')
def home():
    return render_template('index.html', value="sd")

@app.route('/list')
def list():
    return render_template('list.html')

if __name__ == 'main':
    db.create_all()
    app.run(debug=True)
    