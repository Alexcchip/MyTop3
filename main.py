from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form.get('userr')
        email = request.form.get('em')
        band1 = request.form.get('b1')
        band2 = request.form.get('b2')
        band3 = request.form.get('b3')
        print(username, email, band1, band2, band3)

        new_user = User(username=username, email=email, band1=band1, band2=band2, band3=band3)
        db.session.add(new_user)
        db.session.commit()
    return render_template('index.html')

@app.route('/list')
def list():

    return render_template('list.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    