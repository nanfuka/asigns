# from flask import Flask, jsonify, request, json, render_template
from flask import Flask, render_template, redirect, url_for, request, jsonify
from app.db import DatabaseConnection
# from urllib.request import urlopen
from PIL import Image
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import json

UPLOAD_FOLDER = "/Users/Emmanuel/asigns/app/views/static/images"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)

dbase = DatabaseConnection()


@app.route('/')
def index():
    """index url"""
    return render_template('home.html')


@app.route('/login',  methods=['POST', 'GET'])
def login():
    """index url"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'The username and password you have entered are invalid.'
        else:
            return redirect(url_for('signup'))
    return render_template('login.html', error=error)


@app.route('/profile',  methods=['POST', 'GET'])
def profile():
    return render_template('profile.html')


def validate_signup(firstname, lastname, username, gender, dateofbirth, maritalstatus):
    if not firstname or firstname.strip() == "":
        return "Enter firstname"
    if not firstname.isalpha():
        return "firstname should be composed of only letters"
    if not lastname or lastname.strip() == "":
        return "Enter lastname"
    if not lastname.isalpha():
        return "lastname should be composed of only letters"
    if not username or username.strip() == "":
        return "Enter username"
    if dbase.get_details_for_particularuser(username):
        return "please choose a different username, this one is already taken"
    if not username.isalpha():
        return "username should be composed of only letters"
    if not gender or gender.strip() == "":
        return "Enter gender"
    if not gender.isalpha():
        return "firstname should be composed of only letters"
    if not dateofbirth:
        return "Enter dateofbirth"
    if not maritalstatus or maritalstatus.strip() == "":
        return "Enter maritalstatus"
    if not maritalstatus.isalpha():
        return "maritalstatus should be composed of only letters"


@app.route('/signups',  methods=['POST', 'GET'])
def signup():
    """index url"""
    er = None
    if request.method == 'POST':
        # image = request.form['image']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        gender = request.form['gender']
        dateofbirth = request.form['dateofbirth']
        maritalstatus = request.form['maritalstatus']

        churchfamily = request.form['churchfamily']
        fellowshipgroup = request.form['fellowshipgroup']
        leadershiprole = request.form['leadershiprole']
        highestlevelofeducation = request.form['highestlevelofeducation']
        profession = request.form['profession']
        occupation = request.form['occupation']
        placeofwork = request.form['placeofwork']


        placeofresidence = request.form['placeofresidence']
        phonecontact = request.form['phonecontact']
        emailaddress = request.form['emailaddress']
        highestlevelofeducation = request.form['highestlevelofeducation']
        profession = request.form['profession']
        occupation = request.form['occupation']

        dateofbaptism = request.form['dateofbaptism']
        placeofbaptism = request.form['placeofbaptism']
        nameofpastorwhobaptised= request.form['nameofpastorwhobaptised']
        formerreligion = request.form['formerreligion']
        profession = request.form['profession']
        occupation = request.form['occupation']
        er = validate_signup(firstname, lastname, username,
                             gender, dateofbirth, maritalstatus)


        if er:
            er = er
        else:
            dbase.create_member(firstname, lastname, username, gender, dateofbirth, maritalstatus,churchfamily, fellowshipgroup, leadershiprole, highestlevelofeducation, profession, occupation, placeofwork, placeofresidence, phonecontact, emailaddress, dateofbaptism, placeofbaptism, nameofpastorwhobaptised,formerreligion)
            return redirect(url_for('upload_file'))
    return render_template('memb_reg.html', error=er)


@app.route('/fetch_user',  methods=['GET'])
def view_member():

    data = dbase.get_members()
    return jsonify(data)


@app.route('/member_table',  methods=['GET'])
def member_table():
    # username = request.form['username']

    data = dbase.get_members()
    return render_template('membership.html', data=data)


@app.route('/view_profile',  methods=['GET'])
def view_profile():
    # username = request.form['username']

    data = dbase.get_members()
    return render_template('profile.html')


def validate_search(username):
    if not dbase.get_details_for_particularuser(username):
        # if not username or not isalpha(username):
        return "Enter a valid username in the input box"


@app.route('/fetch_them',  methods=['GET', 'POST'])
def view():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        error = validate_search(username)
        if error:
            error = error

        data = dbase.get_details_for_particularuser(username)
        return render_template('profile.html', username=data['username'],
                               lastname=data['lastname'],
                               firstname=data['firstname'],
                               gender=data['gender'],
                               dateofbirth=data['dateofbirth'],
                               maritalstatus=data['maritalstatus'],
                                churchfamily=data['churchfamily'],
                                fellowshipgroup=data['fellowshipgroup'],
                                leadershiprole=data['leadershiprole'],
                               highestlevelofeducation=data['highestlevelofeducation'],
                                profession=data['profession'],
                               occupation=data['occupation'],
                               placeofwork=data['placeofwork'],
                               placeofresidence=data['placeofresidence'],
                               phonecontact=data['phonecontact'],
                               emailaddress=data['emailaddress'],
                               dateofbaptism=data['dateofbaptism'],
                               placeofbaptism=data['placeofbaptism'],
                               nameofpastorwhobaptised=data['nameofpastorwhobaptised'],
                               formerreligion=data['formerreligion']
                               )
    all_users = dbase.get_members()
    return render_template('view_members.html', error=error, all_users=all_users)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    data = None
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No file part'
            return render_template('im.html', error=error)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data = 'your photo has been successfully uploaded'
            file.save(os.path.join(
                '/Users/Emmanuel/asigns/app/views/static/images', filename))
            return redirect(url_for('signup',
                                    filename=filename, data=data))
    return render_template('im.html', data=data)


# @app.route('/im', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             error ='No file part'
#             return render_template('im.html', error = error)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(
#                 '/Users/Emmanuel/asigns/app/views/static/images', filename))
#             return redirect(url_for('signup'))
#     return render_template('memb_reg.html')
