from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsASecureForm'
# this index route renders our starting page - the form
@app.route('/')
def index():
    return render_template("index.html")

# this result route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    errorText = ""
    name = request.form['name']
    if len(name) < 1:
        errorText += "Missing Name. "
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(comment) < 1:
        errorText += "Missing Comment. "
    elif len(comment) > 120:
        errorText += "Comment too long (max 120 characters). "

    print errorText
    if len(errorText) > 0:  # flash the error
        flash(errorText)
        return redirect('/')
    else:   # display the form results
        return render_template("result.html", name=name, location=location, language=language, comment=comment)
# the "result.html" form redirects back to our index route

app.run(debug=True) # run our server
