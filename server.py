# render template allows us to send html files to webpage
from flask import Flask, render_template, url_for, request, redirect
import csv

# frameworks give us a higher level of abstraction
# ginja is a templating language for Flask that allows us to dynamically update our pages

app = Flask(__name__)

# server waiting for route request

# variable rules allow us to be dynamic. we can use <>

@app.route("/<string:page_name>")
def my_home(page_name):
    # when using render_template, flask automatically looks for a folder called templates. You need to create this.
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



# new route for submitting form on contact page
# GET means broswer wants to send info. POST means browser wants to save info.
# We never call this on the front end. Works in conjunction with contact.html
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to database"
    else:
        return "Something went wrong. Try again"
"""
Below is an example of how we would hard code our html pages

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')
"""

