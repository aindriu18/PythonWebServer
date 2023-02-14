# render template allows us to send html files to webpage
from flask import Flask, render_template

# frameworks give us a higher level of abstraction
# ginja is a templating language for Flask that allows us to dynamically update our pages

app = Flask(__name__)

# server waiting for route request

# variable rules allow us to be dynamic. we can use <>

@app.route("/<string:page_name>")
def my_home(page_name):
    # when using render_template, flask automatically looks for a folder called templates. You need to create this.
    return render_template(page_name)


"""
Below is an example of how we would hard code our html pages

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')
"""

