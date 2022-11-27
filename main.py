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
    pin = db.Column(db.Integer(), nullable=False)
    band1 = db.Column(db.String(50), nullable=False)
    band2 = db.Column(db.String(50), nullable=False)
    band3 = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form.get('userr')
        email = request.form.get('em')
        pin = request.form.get('pin')
        band1 = request.form.get('b1')
        band2 = request.form.get('b2')
        band3 = request.form.get('b3')
        print(pin, username, email, band1, band2, band3)
        US = User.query.filter_by(email=email).first()
        eM = User.query.filter_by(username=username).first()
        if US:
            flash('Username is already in use', category='error')
        if eM:
            flash('Email is already in use', category='error')
        elif len(email) < 4:
            flash("Email is too short", category='error')
        if (len(pin) != 4):
            flash("Pin is not 4 numbers long", category='error')
        else:
            flash('You signed in!', category='success')
            new_user = User(pin=pin,username=username, email=email, band1=band1, band2=band2, band3=band3)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('list'))

        
    return render_template('index.html')




@app.route('/list')
def list():
    users = User.query.all()
    return render_template('list.html', users=users)

# UPDATE THE DATABASE
# Note for alex: Create a new page on the website, the user would need to upload the correct pin, usernmae and email and then it will be updated
@app.route('/update', methods=['GET', 'POST'])
def update():
    # create a post method to get everything
    if request.method == 'POST':
        username = request.form.get('userr')
        email = request.form.get('em')
        pin = request.form.get('pin')
        update_band1 = request.form.get('b1')
        update_band2 = request.form.get('b2')
        update_band3 = request.form.get('b3')
        print(username, email, pin, update_band1, update_band2, update_band3)
        US = User.query.filter_by(username=username).first()
        eM = User.query.filter_by(email=email).first()
        pIN = User.query.filter_by(pin=pin).first()

'''note for dip: I am having trouble with verifying that the user info exists (). It says that it does even if it doesn't
. I am also having trouble with updating the user info'''
        if US and eM and pIN:
            db.session.commit()
            print(update_band1, update_band2, type(update_band3))
            return redirect(url_for('list'))
        else:
            flash("User info is incorrect", category='error')
    return render_template('update.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    