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


# image1 = Image.open('mail.png')
# image1.show()
@app.route('/s')
def index():
    """index url"""
    return "nakupenda"




@app.route('/')
def my_view():
    data = dbase.get_members()
    datas = [1, "foo"]
    return render_template('inde.html', data=json.dumps, data)
#     # members = dbase.get_members()
#     # return render_template('view_members.html', members=members)
# # @app.route('/login')
# # def signup_url():
# #     """index url"""
# #     return render_template('register.html')

# @app.route('/login',  methods=['POST', 'GET'])
# def login():
#     """index url"""
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'secret':
#             error = 'The username and password you have entered are invalid.'
#         else:
#             return redirect(url_for('signup'))
#     return render_template('register.html', error=error)

# @app.route('/signups',  methods=['POST', 'GET'])
# def signup():
#     """index url"""
#     if request.method == 'POST':
#         # image = request.form['image']
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         username = request.form['username']
#         gender = request.form['gender']
#         dateofbirth = request.form['dateofbirth']
#         maritalstatus = request.form['maritalstatus']
#         # file = request.files['file']
#         # if file.filename == '':
#         #     flash('No selected file')
#         # if file and allowed_file(file.filename):
#         #     filename = secure_filename(file.filename)
#         #     file.save(os.path.join('/Users/Emmanuel/asigns/app/views/static/images', filename))   
#         new = dbase.create_member(firstname, lastname, username, gender, dateofbirth, maritalstatus )
#         # # return jsonify({"status": 201, "data": [{"user": new,"message": "you have successfully signedup in as a user"}]})
#     return render_template('memb_reg.html')

# @app.route('/fetch_users',  methods=['GET'])
# def view_members():
#     members = dbase.get_members()
#     user = "my lovely daughter"

#     return render_template('view_members.html', user = user)

@app.route('/fetch_user',  methods=['GET'])
def view_member():
    lis = []
    members = dbase.get_members()
    for dict_item in members:
        lis.append(dict_item)
        # for dic in dict_item:

        # for key, value in dict_item.items():


        return render_template('show_entries.html', entries=['melisa', 'suubi', 'tendo', 'emma'])

# @app.route('/fetch_user',  methods=['GET'])
# def view_members():
#     password = request.form['password']
#     userdetails = dbase.get_all_user_details(password)
#     return render_template('view_members.html', members=userdetails)

# @app.route('/img')
# def serve_img():
#     image1 = Image.open('mail.png')
#     kifaa = image1.show()   
#     # images = dbase.get_images()


#     # img = Image.open(urlopen(images))
#     return render_template('view_members.html', images=kifaa)

# def readImage():
#     try:
#         fin = open("woman.jpg", "rb")
#         img = fin.read()
#         return img



    # pass # look up via id, create response with appropriate mimetype

        # # error = None

        #     if request.form['username'] != 'admin' or request.form['password'] != 'secret':
        #         error = 'The username and password you have entered are invalid.'
        #     else:
        #         return redirect(url_for(''))
        # return render_template('memb_reg.html', error=error)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/im', methods=['GET', 'POST'])
# # def allowed_file(filename):
# #     return '.' in filename and \
# #            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/im', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             file.save(os.path.join('/Users/Emmanuel/asigns/app/views/static/images', filename))
#             return redirect(url_for('upload_file',
#                                     filename=filename))
#     return render_template('im.html')

# @app.route('/im', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             file.save(os.path.join('/Users/Emmanuel/asigns/app/views/static/images', filename))
#             return redirect(url_for('signup'))
#     return render_template('memb_reg.html')
#     # return redirect(url_for('upload_files'))


    
