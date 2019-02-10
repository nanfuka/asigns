# from flask import Flask, jsonify, request, json, render_template
from flask import Flask, render_template, redirect, url_for, request
from app.db import DatabaseConnection

app = Flask(__name__)

dbase = DatabaseConnection()



@app.route('/')
def index():
    """index url"""
    return render_template('rep.html')
# @app.route('/login')
# def signup_url():
#     """index url"""
#     return render_template('register.html')

@app.route('/login',  methods=['POST', 'GET'])
def login():
    """index url"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'The username and password you have entered are invalid.'
        else:
            return redirect(url_for('signup'))
    return render_template('register.html', error=error)

@app.route('/signup',  methods=['POST', 'GET'])
def signup():
    """index url"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        new = dbase.create_member(username, password)
        # return jsonify({"status": 201, "data": [{"user": new,"message": "you have successfully signedup in as a user"}]})
    return render_template('memb_reg.html')

@app.route('/fetch_users',  methods=['POST', 'GET'])
def view_members():
    members = dbase.get_members()
    return render_template(members=members)


        # # error = None

        #     if request.form['username'] != 'admin' or request.form['password'] != 'secret':
        #         error = 'The username and password you have entered are invalid.'
        #     else:
        #         return redirect(url_for(''))
        # return render_template('memb_reg.html', error=error)

