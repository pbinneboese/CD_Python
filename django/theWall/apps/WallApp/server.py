from flask import Flask, redirect, request, session, render_template, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  =   re.compile(r'^[a-zA-Z]')

app = Flask(__name__)
app.secret_key = 'mykey'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_reg')

# ---------------------------- login/ regisration -----------------------------
@app.route('/')
def index():
    check_user()
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    check_user()
    print request.form
    errors = []
    # Validate all form data
    # first_name last_name lengths
    if len(request.form['first_name']) < 2:
        errors.append('First name is too short!')
    if len(request.form['last_name']) < 2:
        errors.append('Last name is too short!')
    # first_name, last_name letters only
    if not NAME_REGEX.match(request.form['first_name']):
        errors.append('First name must be letters only!')
    if not NAME_REGEX.match(request.form['last_name']):
        errors.append('Last name must be letters only!')
    # Email - Valid Email format, and that it was submitted
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Please enter a valid email!')
    # check for email in DB
    query = "SELECT * FROM users where email = :email"
    data = {
        'email': request.form['email'],
    }
    user = mysql.query_db(query, data)
    if user:
        errors.append('Email already exists!')

    # Password - at least 8 characters, and that it was submitted
    if len(request.form['password']) < 8:
        errors.append('Password must be at least 8 characters long!')
    # Passwords match
    if not request.form['password'] == request.form['password_confirmation']:
        errors.append('Passwords must match!')

    print errors

    # If we fail the validations
    if errors:
        # send validation messages to client
        for error in errors:
            print type(error)
            flash(error)
        # redirect back to index
        return redirect('/')

    # If we pass validations
    else:
        # encrypt password
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        print hashed_pw
        # create our user
        query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOw(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }

        # save user info (id) in session
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        # send success message/ redirect to success page
        return redirect('/success')


    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    check_user()
    # check for user
    query = "SELECT * FROM users where email = :email"
    data = {
        'email': request.form['email'],
    }
    user = mysql.query_db(query, data)
    print user
    print ('-')*80
    print user[0]

    # if user exists
    if user:
        # check for password match
        if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        # if password check is True
            # save the user_id in session
            session['user_id'] = user[0]['id']
            # redirect to success
            return redirect('/success')
        # if not password match
        else:
            # send meassage to client
            flash('Invalid email/password combination!')
            # redirect to index
            return redirect('/')

    # if not user
    else:
        # send message to client
        flash('Please enter a valid email, or register!')
        # redirect to index
        return redirect('/')

@app.route('/success')
def success():
    check_user()
    # verify that session is set

    if not 'user_id' in session:
        flash('Must be logged in to use our page!')
        return redirect('/')

    # get all messages and join users table to messages table
    query = "SELECT messages.user_id, messages.id, messages.content, messages.created_at, DATE_FORMAT(messages.created_at, '%b %D, %Y %h:%i:%s') AS formated_date, CONCAT(users.first_name, ' ', users.last_name) AS full_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY formated_date DESC"

    # get all messages
    messages = mysql.query_db(query)
    # get the current_time by import the datetime module
    current_time = datetime.datetime.now()
    for message in messages:
        # get the difference between the current time and the time the message was created and save to the db
        difference = current_time - message['created_at']
        # convert the difference to a string in order to do the comparsion,  both datetime.now() and the NOW() has a data type of datetime, can not perform comparsion without a conversion first
        difference = str(difference)
        # if the difference is under 30 mins:
        if difference < '0:30:00':
            # add true to the query object
            message['can_delete'] = True
        else:
            # else add false
            message['can_delete'] = False
    # print messages
    # get all comments and join users table to comments table
    query = "SELECT comments.message_id, comments.content, DATE_FORMAT(comments.created_at, '%b %D, %Y %h:%m') AS formated_date, CONCAT(users.first_name, ' ', users.last_name) AS full_name FROM comments JOIN users ON comments.user_id = users.id"
    comments = mysql.query_db(query)
    # print comments


    return render_template('success.html', messages = messages, comments=comments, current_time=current_time)

@app.route('/logout', methods=['POST'])
def logout():
    check_user()
    session.clear()
    return redirect('/')

def check_user():
    if 'user_id' in session:
        print 'True'
    else:
        print 'False'

# ------------------------------ wall routes -----------------------------------
@app.route('/create_message', methods=['POST'])
def add_message():
    query = "INSERT into messages (content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/create_comment/<message_id>', methods=['POST'])
def add_comment(message_id):
    query = "INSERT into comments (content, message_id, user_id, created_at, updated_at) VALUES (:content, :message_id, :user_id, NOW(), NOW())"
    data = {
        'content': request.form['content'],
        'user_id': session['user_id'],
        'message_id': message_id
    }
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/delete_message/<message_id>', methods=['POST'])
def delete_message(message_id):
    query = "DELETE FROM messages WHERE id = :message_id"
    data = {
        'message_id':message_id
    }
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug = True)
