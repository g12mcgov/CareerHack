#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-07 21:32:44
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-07 23:44:20


import sys
import json
from flask import (
	Flask,
	jsonify,
	request,
	Response,
	render_template,
	send_from_directory
	)

## SQL
from flask_sqlalchemy import SQLAlchemy

## Models
from models.models import db

########################################################
## FLASK APP
########################################################
app = Flask("careerhack", static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://plqahetrqpbetx:z5jiF9_oetqDGNGyzsE7Gicrq0@ec2-54-204-5-56.compute-1.amazonaws.com:5432/d5tdjoc0h355vn'

########################################################
## DATABASE
########################################################
db.init_app(app)

########################################################
## ROUTES
########################################################
@app.route('/')
@app.route('/index.html')
def index():
	"""
	[index.html] - Returns the main index page
	"""
	return render_template('index.html')


########################################################
## STATIC ASSETS
########################################################
@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
	return send_from_directory('static/img', path)

@app.route('/bower_components/<path:path>')
def send_bower_components(path):
	return send_from_directory('static/bower_components', path)

if __name__ == '__main__':
	# Run
	app.run(
    	debug=True,
    	host= '0.0.0.0'
    	)