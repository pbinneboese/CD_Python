from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

# our index route will display the initial webpage
@app.route('/')
def index():
    # set the answer's value
    if 'answer' not in session:
        session['answer'] = random.randrange(0,101)
        session['guess'] = 0
        session['compare'] = 'none'
        print "Answer is", session['answer']
    return render_template("index.html")

# this route will handle our form submission
@app.route('/attempt', methods=['POST'])
def getAttempt():
    # here we check which button was pressed
    session['guess'] = int(request.form['guess'])
    # if session['guess'] < 1:
    #     session['guess'] = 0
    print "Guess is", session['guess'], "Answer is", session['answer']
    if session['guess'] < session['answer']:
        session['compare'] = 'low'
    elif session['guess'] > session['answer']:
        session['compare'] = 'high'
    else:  #got it right
        session['compare'] = 'match'
        # session.pop('answer')  # create a new random answer
    return redirect('/')

# this route handles the game restart
@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')

app.run(debug=True) # run our server
