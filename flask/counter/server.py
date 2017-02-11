from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

# our index route will display the counter webpage
@app.route('/')
def index():
    # initialize and increment counter upon each refresh
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

# this route will handle our form submission
@app.route('/count', methods=['POST'])
def countThis():
    print "Got Post Info"
    # here we check which button was pressed
    if request.form['btn'] == 'increment':
        session['counter'] += 1
    elif request.form['btn'] == 'reset':
        session['counter'] = 0
    return redirect('/')

app.run(debug=True) # run our server
