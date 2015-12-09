#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-07 23:16:56
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-08 21:32:41

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
	"""
	Company Model
	"""
	__tablename__ = 'Companies'
	CompanyID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(60))
	Industry = db.Column(db.String(60))
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, Name, Industry):
		self.Name = Name
		self.Industry = Industry
		self.Updated = datetime.datetime.now()

class Interviewer(db.Model):
	"""
	Interviewer Model
	"""
	__tablename__ = 'Interviewers'
	InterviewerID = db.Column(db.Integer, primary_key=True)
	Interviewer = db.Column(db.String(60))
	Position = db.Column(db.String(60))
	CompanyID = db.Column(db.Integer, db.ForeignKey('Companies.CompanyID'))

	def __init__(self, Interviewer, Position):
		self.Interviewer = Interviewer
		self.Position = Position

class Question(db.Model):
	"""
	Question Model
	"""
	__tablename__ = 'Questions'
	QuestionID = db.Column(db.Integer, primary_key=True)
	Question = db.Column(db.Text)
	JobID = db.Column(db.Integer, db.ForeignKey('JobTypes.JobID'))
	TopicID = db.Column(db.Integer, db.ForeignKey('Topics.TopicID'))
	InterviewerID = db.Column(db.Integer, db.ForeignKey('Interviewers.InterviewerID'))
	Created = db.Column(db.DateTime, default=datetime.datetime.now())
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, Question, Created, Updated):
		self.QuestionID = QuestionID
		self.Question = Question
		self.Created = Created
		self.Updated = Updated

class Answer(db.Model):
	"""
	Answer Model
	"""
	__tablename__ = 'Answers'
	AnswerID = db.Column(db.Integer, primary_key=True)
	Answer = db.Column(db.Text)
	QuestionID = db.Column(db.Integer, db.ForeignKey('Questions.QuestionID'))
	Created = db.Column(db.DateTime, default=datetime.datetime.now())
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, Answer, Created, Updated):
		self.AnswerID = AnswerID
		self.Answer = Answer
		self.Created = Created
		self.Updated = Updated

class JobType(db.Model):
	"""
	JobType Model
	"""
	__tablename__ = 'JobTypes'
	JobID = db.Column(db.Integer, primary_key=True)
	JobPosition = db.Column(db.String(60), unique=True)
	NewGrad = db.Column(db.Boolean, default=False)

	def __init__(self, JobPosition, NewGrad):
		self.JobPosition = JobPosition
		self.NewGrad = NewGrad

class Topic(db.Model):
	"""
	Topic Model
	"""
	__tablename__ = 'Topics'
	TopicID = db.Column(db.Integer, primary_key=True)
	TopicName = db.Column(db.String(60), unique=True)

	def __init__(self, TopicName):
		self.TopicName = TopicName