from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# this index route renders our starting page - the form
@app.route('/')
def index():
    return render_template("index.html")

# this result route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name=name, location=location, language=language, comment=comment)
# the "result.html" form redirects back to our index route

app.run(debug=True) # run our server
