import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import re

# take environment variables from .env.
load_dotenv()

app = Flask(__name__)

mail = Mail(app)  # instantiate the mail class

# email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['SECRET_KEY'] = os.getenv('FLASH_SECRET_KEY')


@app.route("/", methods=('GET', 'POST'))
def hello():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name:
            flash('Name is required!', category='error')
        elif not email:
            flash('Email is required!', category='error')
        elif not message:
            flash('Message is required!', category='error')
        else:
            # email validation
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash('Please provide a valid email address!', category='error')
                return redirect('/')

            # sending email
            sender = os.getenv('MAIL_USERNAME')

            msg = Message(
                'My Portfolio Users',
                sender=sender,
                recipients=[email]
            )

            message_body = 'Name: {}, Message: {}'.format(name, message)
            msg.body = message_body

            try:
                mail.send(msg)
                flash('Message submitted successfully', category='info')
            except:
                error_message = 'An error occurred while sending email. PLease try ahain later'
                flash(error_message, category='error')

            return redirect('/')

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
