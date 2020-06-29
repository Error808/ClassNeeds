"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)


"""
The flask application package.
"""

from datetime import datetime
from flask import render_template,  request, redirect, url_for
from ClassNeeds import app

import ClassNeeds.config

import psycopg2




@app.route('/')
@app.route('/home')
def classNeeds():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/Classes', methods = ['GET', 'POST'])
def Classes():

    if request.method == 'POST':
        
        data = request.form['classChoose']

        if data == "CSE 101":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 102":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 103":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 104":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 120":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 130":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 180":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 181":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 183":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 140":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 144":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 150":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 160":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 111":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 112":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
        elif data == "CSE 115":
            print(data)
            return render_template(
                'classDetails.html',
                message = data,
                title = "title"
            )
       

 

        

    elif request.method == 'GET':
        return render_template(
            'classes.html',
            title='Classes',
            year=datetime.now().year,
            message='classes should show here'
        )
    print(data)


@app.route('/Ratings')
def Ratings():
    """Renders the contact page."""
    return render_template(
        'ratings.html',
        title='Ratings',
        year=datetime.now().year,
        message='ratings of the classes should show here'
    )

@app.route('/About')
def About():
    """Renders the contact page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='about us'
    )

@app.route('/ClassInfo')
def ClassInfo():
    return render_template(
        'classDetails.html',
        message = data,
        title = "title"
        
        )







#connecting to the database

try:
    connection = psycopg2.connect(user = config.user1,
                                  password = config.pass1,
                                  host = config.host1,
                                  port =  config.port1 ,
                                  database = config.database1)

    cursor = connection.cursor()
    # print postgresql connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # print postgresql version
    cursor.execute("select version();")
    record = cursor.fetchone()
    print("you are connected to - ", record,"\n")

except (exception, psycopg2.error) as error :
    print ("error while connecting to postgresql", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("postgresql connection is closed")