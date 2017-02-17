from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re   # RegEx module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "KeyForTodayIsWhizKid"
mysql = MySQLConnector(app,'usersdb')

# session variables
user_id = 0;

# Initial page - prompt user for login/registration
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Login existing user - form submittal
@app.route('/login', methods=['POST'])
def login():
    print "Got user login"
    valid = True    # assume valid till proven otherwise
    user_email = request.form['user_email']
    user_password = request.form['user_password']
    # validate email address
    if len(user_email) < 1:
        valid = False
    elif len(user_email) > 80:
        valid = False
    elif not EMAIL_REGEX.match(user_email):
        valid = False
    if valid == False:  # flash the error
        flash("Invalid email address")
        return redirect('/')
    # validate password
    if len(user_password) < 8:
        valid = False
    if valid == False:  # flash the error
        flash("Invalid password")
        return redirect('/')
    print user_email, user_password
    # verify this user is in the database
    query = "SELECT * FROM user_table WHERE email = :user_email"
    data = {'user_email': user_email}
    this_user = mysql.query_db(query, data)
    print this_user
    if len(this_user) < 1:
        valid = False
        flash("User {} not found".format(user_email))
    elif this_user.password != user_password:
        valid = False
        flash("Password incorrect")
    if valid == False:
        return redirect('/')
    else:   # user is valid, proceed with login
        user_id = this_user.id
        flash("Logging {} in...".format(user_email))
        return redirect('/success')

# Create a new user entry - form submittal
@app.route('/create_user', methods=['POST'])
def create():
    print "Got new registration"
    errors = []
    user_first_name = request.form['user_first_name']
    user_last_name = request.form['user_last_name']
    user_email = request.form['user_email']
    user_password = request.form['user_password']
    user_password2 = request.form['user_password2']
    # validate first and last names
    if not ((len(user_first_name) >= 2) and NAME_REGEX.match(user_first_name)):
        errors.append("First name must contain only alpha characters")
    if not ((len(user_last_name) >= 2) and NAME_REGEX.match(user_last_name)):
        errors.append("Last name must contain only alpha characters")

    elif len(user_email) > 80:
        valid = False

    # validate email address
    if len(user_email) < 1:
        valid = False
    elif len(user_email) > 80:
        valid = False
    elif not EMAIL_REGEX.match(user_email):
        valid = False
    if valid == False:  # flash the error
        flash("Invalid email address")
        return redirect('/')
    # validate password
    if len(user_password) < 8:
        valid = False
    if valid == False:  # flash the error
        flash("Invalid password")
        return redirect('/')
    print user_email, user_password
    # verify this user is in the database
    query = "SELECT * FROM user_table WHERE email = :user_email"
    data = {'user_email': user_email}
    this_user = mysql.query_db(query, data)
    print this_user
    if len(this_user) < 1:
        valid = False
        flash("User {} not found".format(user_email))
    elif this_user.password != user_password:
        valid = False
        flash("Password incorrect")
    if valid == False:
        return redirect('/')
    else:   # user is valid, proceed with login
        user_id = this_user.id
        flash("Logging {} in...".format(user_email))
        return redirect('/success')

    # We'll then create a dictionary of data from the POST data received.
    query = "INSERT INTO user_table (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {'email': user_email}
    print query;
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/success')

# Show login success page
@app.route('/success')
def show():
    query = "SELECT * FROM user_table"  # define your query
    users = mysql.query_db(query)  # run query with query_db()
    return render_template('success.html', all_users=users) # pass data to our template

# Process logout form
@app.route('/logout')
def logout():
    session.clear()
    flash("User logged out.")
    return redirect('/'

app.run(debug=True)
