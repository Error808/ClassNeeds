"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.secret_key = "super secret key"

"""
The flask application package.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import render_template,  request, redirect, url_for, send_file, flash
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from flask_login import LoginManager, UserMixin, login_user,login_required, logout_user, current_user

#from ClassNeeds import app

import ClassNeeds.config



#location of the database
app.config['SQLALCHEMY_DATABASE_URI'] =  "postgres://vmnwaguqhuxhiy:9a7a8ca0bf1cff4890d9f56a298ae099d1a22a0fe8b6d423d3895e0902ec97af@ec2-54-175-117-212.compute-1.amazonaws.com:5432/dff5amlfes2k69"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

#table in the database
class File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    className = db.Column(db.String(300))
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    wfile = db.Column(db.String(300))

# table for sign up 
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))


#creates the table
db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/SignUp' , methods = ['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        email = request.form.get('user')
        password = request.form.get('passW')
        user = Users.query.filter_by(email = email).first()

        if user:
            flash('This email address already exists!')
            return redirect(url_for('SignUp'))
        new_user = Users(email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Signed up successfully, please sign in.')
        return redirect(url_for('SignIn'))

    else:
        return render_template(
        'signUp.html',
        title='SignUp',
        year=datetime.now().year
    )

@app.route('/SignIn' , methods = ['GET', 'POST'])
def SignIn():
    if current_user.is_authenticated:
        flash('You are already signed in!')
        return redirect (url_for('ClassNeeds'))
    if request.method == 'POST':
        user = request.form['user']
        passW = request.form['passW']
        remember = True if request.form.get('remember') else False

        user = Users.query.filter_by(email=user).first()

        if not user or not check_password_hash(user.password, passW):
            flash('Email address or password is incorrect.')
            return redirect(url_for('SignIn')) 

        # return redirect(url_for('profile'))
        login_user(user)
        flash('Signed in successfully.')
        return redirect(url_for('ClassNeeds'))

    else:
        return render_template(
        'signIn.html',
        title='SignIn',
        year=datetime.now().year
    )

@app.route('/SignOut')
def SignOut():
    if current_user.is_anonymous:
        flash('You are not signed in!')
        return redirect (url_for('SignUp'))
    logout_user()
    flash('You signed out successfully.')
    return redirect(url_for('ClassNeeds'))




@app.route('/')
@app.route('/ClassNeeds')
def ClassNeeds():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )



@app.route('/Download/<int:id>', methods=['GET'])
def Download(id):
    item = File().query.filter_by(id=id).first()
    return send_file(BytesIO(item.data), as_attachment = True, attachment_filename = item.name)

@app.route('/Classes', methods = ['GET', 'POST'])
def Classes():

    if current_user.is_anonymous:
        flash('Please sign in or sign up first :)')
        return redirect (url_for('ClassNeeds'))

    if request.method == 'POST':
        
        data = request.form['classChoose']

        if data == "CSE 101":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "101",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 102":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "102",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 103":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "103",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 104":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "104",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 120":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "120",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 130":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "130",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 180":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "180",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 181":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "181",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 183":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "183",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 140":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "140",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 144":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "144",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 150":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "150",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 160":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "160",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 111":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "111",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 112":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "112",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
        elif data == "CSE 115":
            items = File().query.filter(File.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            return render_template(
                'classDetails.html',
                message = data,
                title = "115",
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks
            )
       

 
    elif request.method == 'GET':
        return render_template(
            'classes.html',
            title='Classes',
            year=datetime.now().year,
            message='classes should show here'
        )



@app.route('/Ratings')
def Ratings():
    if current_user.is_anonymous:
        flash('Please sign in or sign up first :)')
        return redirect (url_for('ClassNeeds'))
    """Renders the Ratings page."""
    # TODO: replace this with querying the database for every class
    classes = ["CSE 101", "CSE 102", "CSE 103", "CSE 104"]
    # TODO: replace this with actuallying finding out the lowest rated and highest rated classes
    mid = (int)(len(classes)/2)
    highest_rated_classes = classes[0:mid]
    lowest_rated_classes = classes[mid:]

    # currently assumes strings are being passed in for classes
    return render_template(
        'ratings.html',
        title='Ratings',
        highest_rated_classes=highest_rated_classes,
        lowest_rated_classes=lowest_rated_classes,
        year=datetime.now().year
    )

@app.route('/About')
def About():
    """Renders the About page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year
    )

@app.route('/Upload', methods = ['POST'])
def Upload():
    file = request.files['inputFile']
    className = request.form['className']
    wfile = request.form['inlineRadioOptions']

  
    newFile = File( wfile = wfile, className = className, name = file.filename, data = file.read())
    db.session.add(newFile)
    db.session.commit()

    return render_template(
            'classes.html',
            year=datetime.now().year,
            message='classes should show here'
        )


