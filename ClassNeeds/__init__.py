"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)


"""
The flask application package.
"""

from datetime import datetime
from flask import render_template,  request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO

#from ClassNeeds import app

import ClassNeeds.config



#location of the database
app.config['SQLALCHEMY_DATABASE_URI'] =  "postgres://vmnwaguqhuxhiy:9a7a8ca0bf1cff4890d9f56a298ae099d1a22a0fe8b6d423d3895e0902ec97af@ec2-54-175-117-212.compute-1.amazonaws.com:5432/dff5amlfes2k69"

db = SQLAlchemy(app)

#table in the database
class File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    className = db.Column(db.String(300))
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    wfile = db.Column(db.String(300))


#creates the table
db.create_all()




@app.route('/')
@app.route('/home')
def classNeeds():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )



@app.route('/download/<int:id>', methods=['GET'])
def download(id):
    item = File().query.filter_by(id=id).first()
    return send_file(BytesIO(item.data), as_attachment = True, attachment_filename = item.name)

@app.route('/Classes', methods = ['GET', 'POST'])
def Classes():

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
            year=datetime.now().year,
            message='classes should show here'
        )



@app.route('/Ratings')
def Ratings():
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
        highest_rated_classes=highest_rated_classes,
        lowest_rated_classes=lowest_rated_classes,
        year=datetime.now().year
    )

@app.route('/About')
def About():
    """Renders the About page."""
    return render_template(
        'about.html',
        year=datetime.now().year
    )


@app.route('/SignIn')
def SignIn():
    """Renders the About page."""
    return render_template(
        'signIn.html',
        title='signIn',
        #message='about us',
        year=datetime.now().year
    )

    
@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['inputFile']
    className = request.form['className']
    wfile = request.form['inlineRadioOptions']

  
    newFile = File( wfile = wfile, className = className, name = file.filename, data = file.read())
    db.session.add(newFile)
    db.session.commit();

    return render_template(
            'classes.html',
            year=datetime.now().year,
            message='classes should show here'
        )


