from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re   # RegEx module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "KeyForTodayIsWhizKid"
mysql = MySQLConnector(app,'friendsdb')

# Initial page - prompt for a new friend submittal
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Remove page - prompt for a friend removal
@app.route('/remove', methods=['GET'])
def index_remove():
    return render_template('remove.html')

# Create a new friend entry - form submittal
@app.route('/create_friend', methods=['POST'])
def create():
    print "Got new email Post"
    valid = True    # assume valid till proven otherwise
    email_addr = request.form['email_addr']
    if len(email_addr) < 1:
        valid = False
    elif len(email_addr) > 80:
        valid = False
    elif not EMAIL_REGEX.match(email_addr):
        valid = False

    if valid == False:  # flash the error
        flash("Email is not valid!")
        return redirect('/')
    else:   # add to database
        flash("The email address you entered ({}) is a VALID email address! Thank you!".format(email_addr))
    # We'll then create a dictionary of data from the POST data received.
    query = "INSERT INTO email_table (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {'email': email_addr}
    print query;
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/success')

# Remove a friend entry - form submittal
@app.route('/remove_friend', methods=['POST'])
def remove():
    print "Got new email Post"
    valid = True    # assume valid till proven otherwise
    email_addr = request.form['email_addr']
    if len(email_addr) < 1:
        valid = False
    elif len(email_addr) > 80:
        valid = False
    elif not EMAIL_REGEX.match(email_addr):
        valid = False

    if valid == False:  # flash the error
        flash("Email is not valid!")
        return redirect('/remove')
    else:   # add to database
        flash("The email address you entered ({}) is a VALID email address! Thank you!".format(email_addr))
    # We'll then create a dictionary of data from the POST data received.
    query = "DELETE FROM email_table WHERE email = :email"
    data = {'email': email_addr}
    print query;
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/success')

# Show all friend entries
@app.route('/success')
def show():
    query = "SELECT * FROM email_table"  # define your query
    friends = mysql.query_db(query)  # run query with query_db()
    return render_template('success.html', all_friends=friends) # pass data to our template

# # Show a single friend entry
# @app.route('/friends/<friend_id>')
# def show_one(friend_id):
#     # Write query to select specific friend by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])
#
# # Update a friend entry
# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')

# Remove a friend entry
# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)
