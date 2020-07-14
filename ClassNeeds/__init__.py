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
from sqlalchemy import func

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

# table for reviews
class Ratings1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(300), unique=True)
    rating = db.Column(db.Integer)
    userIDsUp = db.Column(db.ARRAY(db.Integer))
    userIDsDown = db.Column(db.ARRAY(db.Integer))

# table for comments
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    className = db.Column(db.String(300))
    comment = db.Column(db.String(500))

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

        classes = getClasses() # helper function below
        
        if data in classes:
            items = File().query.filter(File.className == data)
            comments = Comments().query.filter(Comments.className == data)
            notes = []
            syllabuses = []
            pExams = []
            pHomeworks = []
            commentList = []

            for item in items:
                if item.wfile == "Notes":
                    notes.append(item)
                elif item.wfile == "Syllabus":
                    syllabuses.append(item)
                elif item.wfile == "Practice Exams":
                    pExams.append(item)
                elif item.wfile == "Previous Homeworks":
                    pHomeworks.append(item)
            
            for comment in comments:
                commentList.append(comment)

            return render_template(
                'classDetails.html',
                message = data,
                title = data,
                notes = notes,
                syllabuses = syllabuses,
                pExams = pExams,
                pHomeworks = pHomeworks,
                commentList = commentList
            )
        # else:
            # TODO: if the class doesn't exist, maybe display another page?
            # although at the moment we control what classes can be passed in as 'data'
 
    elif request.method == 'GET':
        return render_template(
            'classes.html',
            title='Classes',
            year=datetime.now().year,
            message='classes should show here'
        )

@app.route('/Ratings', methods = ['GET', 'POST'])
def Ratings():
    if current_user.is_anonymous:
        flash('Please sign in or sign up first :)')
        return redirect (url_for('ClassNeeds'))
    """Renders the Ratings page."""

    if current_user.is_anonymous:
        flash('Please sign in or sign up first :)')
        return redirect (url_for('ClassNeeds'))

    if request.method == 'POST':
        className = request.form['classChoose']
        direction = request.form['direction']

        query = Ratings1.query.filter_by(className = className).first()

        # users who have already voted up or down
        userIDsUp = query.userIDsUp
        userIDsDown = query.userIDsDown

        # alter the rating 
        if(direction == "up"):

            if current_user.id in userIDsUp:      # user voted up already, so subtract 1
                query.rating = Ratings1.rating - 1
                # remove id from userIDsUp
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsUp: func.array_remove( Ratings1.userIDsUp, current_user.id ) 
                    }, synchronize_session=False)

            elif current_user.id in userIDsDown:  # user had voted down, so add 2
                query.rating = Ratings1.rating + 2
                # add to userIDsUp and remove id from userIDsDown
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsUp: func.array_append( Ratings1.userIDsUp, current_user.id ),
                        Ratings1.userIDsDown: func.array_remove( Ratings1.userIDsDown, current_user.id )
                    }, synchronize_session=False)

            else:                                 # user has not voted, so add 1
                query.rating = Ratings1.rating + 1
                # add id to userIDsUp
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsUp: func.array_append( Ratings1.userIDsUp, current_user.id )
                    }, synchronize_session=False)

        else: # direction == down

            if current_user.id in userIDsDown:    # user voted down already, so add 1
                query.rating = Ratings1.rating + 1
                # remove id from userIDsDown
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsDown: func.array_remove( Ratings1.userIDsDown, current_user.id ) 
                    }, synchronize_session=False)

            elif current_user.id in userIDsUp:    # user had voted up, so subtract 2
                query.rating = Ratings1.rating - 2
                # add id to userIDsDown and remove from userIDsUp
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsDown: func.array_append( Ratings1.userIDsDown, current_user.id ),
                        Ratings1.userIDsUp: func.array_remove( Ratings1.userIDsUp, current_user.id )
                    }, synchronize_session=False)

            else:                                 # user has not voted, so subtract 1
                query.rating = Ratings1.rating - 1
                # add id to userIDsDown
                db.session.query(Ratings1).filter( Ratings1.className==className ).update( {
                        Ratings1.userIDsDown: func.array_append( Ratings1.userIDsDown, current_user.id )
                    }, synchronize_session=False)

        db.session.commit()

    # load in the  ratings page -----------------------------
    
    # query the database for each class' rating
    classes = getClasses()
    ratings = []
    for c in classes:
        ratings.append(Ratings1.query.filter_by(className = c).first().rating)

    # determine classes already voted for
    classesUp = []
    classesDown = []
    for c in classes:
        upvotes = Ratings1.query.filter_by(className = c).first().userIDsUp
        downvotes = Ratings1.query.filter_by(className = c).first().userIDsDown
        if current_user.id in upvotes:
            classesUp.append(c)
        elif current_user.id in downvotes:
            classesDown.append(c)

    # sort the classes based on rating
    classesAndRatings = []
    for i in range(0, len(classes)):
        classesAndRatings.append( {'class': classes[i], 'rating': ratings[i]} )
    classesAndRatings.sort(key=ratingsSortHelper)

    # grab the 5 highest and lowest classes
    sortedClasses = []
    for dictionary in classesAndRatings:
        sortedClasses.insert(0,dictionary['class']) # prepend
    highestRatedClasses = sortedClasses[0:5]
    lowestRatedClasses = sortedClasses[-5:]

    # currently assumes strings are being passed in for classes
    return render_template(
        'ratings.html',
        title='Ratings',
        zippedMsg=zip(classes, ratings),
        classesUp=classesUp,
        classesDown=classesDown,
        highestRatedClasses=highestRatedClasses,
        lowestRatedClasses=lowestRatedClasses,
        year=datetime.now().year
    )

def ratingsSortHelper(element):
    '''
    helper function for Ratings()
    '''
    return element['rating']

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

@app.route('/UploadComment', methods = ['POST'])
def UploadComment():
    comment = request.form['inputComment']
    className = request.form['className']

    newComment = Comments( className = className, comment = comment)
    db.session.add(newComment)
    db.session.commit()
    
    return render_template(
            'classes.html',
            year=datetime.now().year,
            message='classes should show here'
        )


def getClasses():
    '''
    Acts as a helper function for Classes() and Ratings().
    Looks to ClassNeeds/classes.txt to find the list of classes.
    returns: a String[] of the classes separated on \n
    ''' 
    classes = open("ClassNeeds/classes.txt", "r") # reads in from specific txt
    return classes.read().split("\n")             # splits the data by \n

def updateRatingsTableClasses():
    '''
    Reads in classes from classes.txt and verifies they're in the database.
    '''
    classesToAdd = getClasses()
    
    for classToAdd in classesToAdd:
        classExists = Ratings1.query.filter_by(className = classToAdd).first()

        if not classExists: # class already exists
            newRating = Ratings1( rating=1, className=classToAdd, userIDsUp=[], userIDsDown=[] )
            db.session.add(newRating)
            print("updateRatingsTableClasses: added {} to ratings table".format(classToAdd))
        
    db.session.commit()

updateRatingsTableClasses()
