#!/usr/bin/env python

from flask import Flask, request
from flask_mail import Mail, Message

mail = Mail()

app = Flask(__name__)
mail.init_app(app)

# app.config.update(
#     MAIL_SERVER='TO_COMPLETE',
#     MAIL_PORT='TO_COMPLETE',
#     MAIL_USE_TLS=True,
#     MAIL_USERNAME='TO_COMPLETE',
#     MAIL_PASSWORD='TO_COMPLETE'
# )

@app.route('/test')
def test():
    return "It works"

@app.route('/contact', methods=['POST'])
def contact():

    # msg = Message("Message Codincamp",
    #               sender=request.form['from'],
    #               recipients=[request.form['to']])
    # msg.html = msg.body = request.form['body']
    # mail.send(msg)
    return "%s va recevoir le message suivant de la part de %s : %s" % (request.form['to'], request.form["from"], request.form['body'])

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
