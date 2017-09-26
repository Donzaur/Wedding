"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request, redirect, url_for
from Donzaur_Flask import app

@app.route('/')
@app.route('/landing')
def home():
    """Renders the home page."""
    return render_template(
        'landing.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/Groomsmen')
def groomsmen():
    return render_template('groomsmen.html',title = 'Nick\'s Groomsmen')
    
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',title = 'Our Story')

@app.route('/venue')
def venue():
    return render_template('venue.html',title = 'Venue')

@app.route('/accomodations')
def accomodations():
    return render_template('accomodations.html',title = 'Accomodations')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/landing')
def landing():
    """Renders the about page."""
    return render_template(
        'landing.html',
        title='Nick and Hannah\'s wedding',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.errorhandler(404)
def page_not_found(e):
    pageName =  request.url
    pageName = str(pageName)
    pageName = pageName.upper()
    print(pageName)
    if "GROOMSMEN" in pageName:
        print("Success")
        return redirect(url_for('groomsmen'))
    else:
        return render_template("404.html")

