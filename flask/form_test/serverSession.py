from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

# this route displays the saved session data
@app.route('/show')
def show_user():
  return render_template("user.html")

app.run(debug=True) # run our server
