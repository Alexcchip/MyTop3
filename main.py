from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash # got security hashing for pin
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
        # print to confirm we got the data 
        print(pin, username, email, band1, band2, band3)
        # check if the email and username and in the database
        eM = User.query.filter_by(email=email).first()
        US = User.query.filter_by(username=username).first()
        if US:
            flash('Username is already in use', category='error')
        elif eM:
            flash('Email is already in use', category='error')
        elif len(email) < 4:
            flash("Email is too short", category='error')
        elif (len(pin) != 4): # changed to elif to fix integrity error issues
            flash("Pin is not 4 numbers long", category='error')
        else:
            flash('You signed in!', category='success')
            # generate_password_hash will hash the password with the sha256 method
            new_user = User(pin=generate_password_hash(pin, method = "sha256"),username=username, email=email, band1=band1, band2=band2, band3=band3)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('list'))

        
    return render_template('index.html')




@app.route('/list')
def list():
    users = User.query.all() # query all the users in the database to retrieve in the future
    return render_template('list.html', users=users)

# UPDATE THE DATABASE
# Note for alex: Create a new page on the website, the user would need to upload the correct pin, usernmae and email and then it will be updated
@app.route('/update', methods=['GET', 'POST'])
def update():
    # create a post method to get everything
    if request.method == 'POST':
        username = request.form.get('userr')
        pin = request.form.get('pin')
        update_band1 = request.form.get('b1') # not mandatory for the user to fill these out
        update_band2 = request.form.get('b2')
        update_band3 = request.form.get('b3')
       # print(username, pin, update_band1, update_band2, update_band3), used for testing 
        #print(len(update_band1), len(update_band2), len(update_band3)) 
        US = User.query.filter_by(username=username).first()
        
        # Note for Alex: I am going to delete the email, as long as we have the username and pin were good 
        # check if the username and email is in the database, note to alex: did not need to verify the pin 
        if US: 
            # check if both match, the pin that the user gave to the original
            if check_password_hash(US.pin, pin):
                # get the dataset from the specific user, filter by the username the person has given
                update_user = User.query.filter_by(username=username).first()
                if len(update_band1) != 0: # if the user has inputed something for band 1
                    update_user.band1 = update_band1
                    db.session.commit()
                    flash('Band 1 has been updated!', category='success')

                if len(update_band2) != 0: # if the user has inputed something for band2 
                    update_user.band2 = update_band2
                    db.session.commit()
                    flash('Band 2 has been updated!', category='success')

                if len(update_band3) != 0: # if the user has inputed something for band3
                    update_user.band3 = update_band3 # change to the band the user has given
                    db.session.commit()
                    flash('Band 3 has been updated!', category='success') 

                else:
                    flash('No update neccessary as input fields are blank', category='success')

        else: # if username is not in database
            flash('Username not in database, please make an account"', category='error')

    return render_template('update.html')

            

'''note for dip: I am having trouble with verifying that the user info exists (). It says that it does even if it doesn't
. I am also having trouble with updating the user info'''
# I guess the syntax is not correct with the if US and eM and pIn. Also we dont need to very pin and we shoudnt do db.session.commit() because we did not add anything beforehand. 
        #if US and eM and pIN:
         #   db.session.commit()
        #    print(update_band1, update_band2, type(update_band3))
         #   return redirect(url_for('list'))
       # else:
       #     flash("User info is incorrect", category='error')
   # return render_template('update.html')""

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    