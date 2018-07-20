# Add a page with a form for CREATING new donations
    # create a template for this page, inside of the templates directory. inherit from base.jinja2.
    # The page should have a form, with a field for
        # the donor name and
        # the amount of the donation
        # The method of the form should be POST

# If the handler receives a GET request, then it should render the template for the donation creation page.
# If the handler receives a POST request (a form submission), then it should attempt to retrieve the name of the donor and the amount of the donation from the form submission.
    # It should retrieve the donor from the database with the indicated name, and create a new donation with the indicated donor and donation amount. Then it should redirect the visitor to the home page.

# Add navigation elements in base.jinja2 to the top of both pages. The navigation elements should include links to both the home page and your new donation-creation page.

# Publish your work to Heroku.
    # If you publish your work to Heroku and then make changes to your application, you will need to publish those changes by commiting your work to your git repository and then executing git push heroku master.
    # Make sure that you also git push origin master to push your changes to GitHub.

# Edit the top of this README file, replacing my Heroku link (http://afternoon-reef-51666.herokuapp.com/donations/) with your own Heroku link.
    # If you're unable to get your application running on Heroku, just write a couple of sentences about where you got hung up.


import os

from flask import Flask, render_template, request, redirect, url_for, session
import base64

from model import SavedDonation

app = Flask(__name__)
#app.secret_key = b'\x07Gj\x84ihq\x1f+\xf3\xc7\xae\xf6\xc2\x9c\xbeaXm\x1e*\x98\xebH'
app.secret_key= ox.environ.get('SECRET_KEY').encode()
#must first enter this into terminal: export SECRET_KEY = CWKUUPGIYFG62

# Create a route and a handler function inside of main.py. Accept both GET requests and POST requests.
@app.route('/create', methods=["GET", "POST"])
def create_donation():
    # session['donor']

    # What is 'total'? Should this be 'donor'?
    if 'd' not in donor:
        session['donor'] = ""
        session['donation'] = 0

    if request.method == "POST":
        donor = request.form['donor']
        session['donor'] = donor

        donation = int(request.form['donation'])
        session['donation'] = donation

    return render_template('create.jinja2', donation=donation)


@app.route('/save', methods=["POST"])
def save():
    donation = session.get('total', 0)
    code = base64.b32encode(oc..urandom(8)).decode().strip('=')

    saved_donation = SavedDonation(value=total, code=code)
    saved_total.save()

    return render_template('save.jinja2', donation=donation)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)