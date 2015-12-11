#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-07 21:32:44
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-11 01:02:47


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
            'SELECT * FROM "Companies" INNER JOIN \
            	(SELECT * FROM "Interviewers" INNER JOIN \
            		(SELECT * FROM "Questions" left OUTER JOIN \
            			(SELECT * FROM "Answers") AS joinC \
            			USING ("QuestionID")) AS joinB \
        				USING ("InterviewerID")) AS joinA \
        				USING ("CompanyID") \
    				WHERE "Name"=\'%s\';' % company_name
            )

        metadata = [item for item in query]
        exists = True if metadata else False

    return render_template(
        'company.html',
        name=company_name,
        metadata=metadata,
    	exists=exists
        )

@app.route('/Topics/<topic_name>')
def topics(topic_name):
    print topic_name
    """
    [Topics] - Fills Topics HTML 
    """
    with app.app_context():
        query = db.engine.execute(
            'SELECT * FROM "Companies" INNER JOIN \
            	(SELECT * FROM "Interviewers" INNER JOIN \
            		(SELECT * FROM "Topics" INNER JOIN \
            			(SELECT * FROM "Questions" LEFT OUTER JOIN \
            				(SELECT * FROM "Answers") AS joinB \
            				USING ("QuestionID")) AS joinA \
        					USING ("TopicID")) AS joinC \
        					USING ("InterviewerID")) AS joinD \
        					USING ("CompanyID") \
    					WHERE "TopicName"=\'%s\';' % topic_name
            )

        metadata = [item for item in query]

    return render_template(
        'topic.html',
        name=topic_name, 
        metadata=metadata
        )

@app.route('/Jobs/<job_name>')
def jobs(job_name):
    print job_name
    """
    [Jobs] - Fills Jobs HTML 
    """
    with app.app_context():
        query = db.engine.execute(
            'SELECT * FROM "Companies" INNER JOIN \
            	(SELECT * FROM "Interviewers" INNER JOIN \
            		(SELECT * FROM "Topics" INNER JOIN \
            			(SELECT * FROM "JobTypes" INNER JOIN \
            				(SELECT * FROM "Questions" LEFT OUTER JOIN \
            					(SELECT * FROM "Answers") AS joinC \
            					USING ("QuestionID")) AS joinA \
        						USING ("JobID")) AS joinB \
        						USING ("TopicID")) AS joinD \
        						USING ("InterviewerID")) AS joinE \
        						USING ("CompanyID") \
    						WHERE "JobPosition" =\'%s\';' % job_name.replace("%20", " ")
            )

        metadata = [item for item in query]

    return render_template(
        'job.html',
        name=job_name, 
        metadata=metadata
        )

@app.route('/insert-question/<company_name>', methods=['POST'])
def insert_question_by_company(company_name):
	data = json.loads(request.get_data())
	if data:
		# First get company ID
		company_id = db.engine.execute(
			'SELECT "CompanyID" FROM "Companies" WHERE "Name"=\'%s\';' % company_name
		).first()[0]

		# Insert Interviewer
		insert_interviewer_query = db.engine.execute(
			'INSERT INTO "Interviewers" ("Interviewer", "Position", "CompanyID") VALUES (\'{}\', \'{}\', \'{}\');'
			.format(
				data['interviewer_input'], 
				data['position_input'],
				company_id)
			)

	return Response(mimetype="application/json")

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