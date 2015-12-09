#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-07 21:32:44
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-09 00:20:36


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
from models.models import *

########################################################
## FLASK APP
########################################################
app = Flask("careerhack", static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mjejkxwhhvmwop:o-nMAMf3-Z-XRgGSuhMm6i9yUE@ec2-54-204-8-224.compute-1.amazonaws.com:5432/d9iv7in7po4q9k'

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
    with app.app_context():
        companies = [company.Name for company in Company.query.all()]
        topics = [topic.TopicName for topic in Topic.query.all()]
        jobtypes = [job.JobPosition for job in JobType.query.all()]


    return render_template(
        'index.html',
        number_of_companies=len(companies),
        companies_list=companies,
        topic_list = topics,
        job_list = jobtypes,
        url=request.base_url
        )

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<company_name>')
def company(company_name):
    """
    [Company] - Fills a company HTML 
    """
    with app.app_context():
        query = db.engine.execute(
            'select * from "Companies" inner join (select * from "Interviewers" inner join (select * from "Questions" left outer join (select * from "Answers") as joinC using ("QuestionID")) as joinB using ("InterviewerID")) AS joinA using ("CompanyID") WHERE "Name"=\'%s\';' % company_name
            )

        metadata = [item for item in query]

        print metadata

    return render_template(
        'company.html',
        name=company_name,
        metadata=metadata
        )

@app.route('/Topics/<topic_name>')
def topics(topic_name):
    print topic_name
    """
    [Topics] - Fills Topics HTML 
    """
    with app.app_context():
        query = db.engine.execute(
            'select * from "Companies" inner join (select * from "Interviewers" inner join (select * from "Topics" inner join(select * from "Questions" left outer join (select * from "Answers") AS joinB using ("QuestionID")) AS joinA using ("TopicID")) as joinC using ("InterviewerID")) AS joinD using ("CompanyID") where "TopicName" =\'%s\';' % topic_name
            )

        metadata = [item for item in query]

        print metadata

    return render_template(
        'topic.html',
        name=topic_name, 
        metadata=metadata
        )


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