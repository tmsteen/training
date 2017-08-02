#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_flask` -- serving up REST
=========================================

LAB_FLASK Learning Objective: Learn to serve RESTful APIs using the Flask library
::

 a. Using Flask create a simple server that serves the following string for the root route ('/'):
  "<h1>Welcome to my server</h1>"

 b. Add a route for "/now" that returns the current date and time in string format.

 c. Add a route that converts Fahrenheit to Centigrade and accepts the value to convert
    in the url.  For instance, /fahrenheit/32.0 should return "0.0"

 d. Add a route that converts Centigrade to Fahrenheit and accepts the value to convert
    in the url.  For instance, /centigrade/0.0 should return "32.0"

"""
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to my server</h1>'

@app.route('/now')
def show_time():
    return str(time.asctime())

@app.route('/farenheit/<float:temp>')
@app.route('/farenheit/<int:temp>')
def farenheit(temp=None):
    return '{} *F converted to Centigrade is {} *C'.format(temp,
                                                        (temp - 32) * 5 / 9 )

@app.route('/centigrade/<float:temp>')
@app.route('/centigrade/<int:temp>')
def centigrade(temp=None):
    return '{} *C converted to Farenheit is {} *F'.format(temp,
                                                        temp * 9 / 5 + 32 )

if __name__ == '__main__':
    app.run(debug=True)
