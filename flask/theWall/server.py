from flask import Flask, redirect, request, session, render_template, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'mykey'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'users_db')


def check_user():
    if 'user_id' in session:
        print 'True'
    else:
        print 'False'

# login/ registration
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
        query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }

        # save user info (id) in session
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        # send success message/ redirect to wall page
        return redirect('/wall')


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
    # print user
    # print ('-')*80
    # print user[0]

    # if user exists
    if user:
        # check for password match
        if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        # if password check is True
            # save the user_id in session
            session['user_id'] = user[0]['id']
            # redirect to wall
            return redirect('/wall')
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

@app.route('/logout', methods=['POST'])
def logout():
    check_user()
    session.clear()
    return redirect('/')

# START WALL HERE
@app.route('/wall')
def wall():
    check_user()
    # verify that session is set
    if not 'user_id' in session:
        flash('Must be logged in to use our page!')
        return redirect('/')
    # For all messages, show message posts by date and user
    query = "SELECT messages.id, DATE_FORMAT(messages.created_at,'%b %D %Y') AS date, messages.message, users.first_name, users.last_name FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC"
    # print "QUERY=", query
    message_list = mysql.query_db(query)
    print "MESSAGES=", message_list

    # Now do the comment posts for each message
    query = "SELECT comments.id, comments.user_id, comments.message_id, DATE_FORMAT(comments.created_at,'%b %D %Y') AS date, comments.comment FROM comments JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_at ASC"
    # print "QUERY=", query
    comment_list = mysql.query_db(query)
    print "COMMENTS=", comment_list

    # # Now do the comment posts by user
    # query = "SELECT comments.id, DATE_FORMAT(comments.created_at,'%b %D %Y') AS date, comments.comment, users.first_name, users.last_name FROM comments JOIN users ON users.id = comments.user_id ORDER BY comments.created_at ASC"
    # # print "QUERY=", query
    # comment_list = mysql.query_db(query)
    # # print "COMMENTS=", comment_list

    return render_template('wall.html', messages=message_list, comments=comment_list)

@app.route('/post_message', methods=['POST'])
def post_message():
    # Add this post to the wall
    new_message = request.form['message']
    if len(new_message) < 1:
        flash('Cannot post an empty message')
        return redirect('/wall')
    query = "INSERT into messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        'user_id': session['user_id'],
        'message': new_message
    }
    # print "QUERY=", query
    print "DATA=", data
    this_message_id = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/post_comment/<this_message_id>', methods=['POST'])
def post_comment(this_message_id):
    # Add this post to the wall
    new_comment = request.form['comment']
    if len(new_comment) < 1:
        flash('Cannot post an empty comment')
        return redirect('/wall')
    query = "INSERT into comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
        'message_id': this_message_id,
        'user_id': session['user_id'],
        'comment': new_comment
    }
    # print "QUERY=", query
    print "DATA=", data
    this_comment_id = mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug = True)
