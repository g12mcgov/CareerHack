#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-07 23:16:56
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-08 00:30:38

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
	"""
	Company Model
	"""
	__tablename__ = 'Companies'
	CompanyID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(60), unique=True)
	Industry = db.Column(db.String(60), unique=True)
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, CompanyID, Name, Industry, Updated):
		self.CompanyID = CompanyID
		self.Name = Name
		self.Industry = Industry
		self.Updated = Updated

class Interviewer(db.Model):
	"""
	Interviewer Model
	"""
	__tablename__ = 'Interviewers'
	InterviewerID = db.Column(db.Integer, primary_key=True)
	Interviewer = db.Column(db.String(60), unique=True)
	Position = db.Column(db.String(60), unique=True)
	CompanyID = db.Column(db.Integer, db.ForeignKey('Company.CompanyID'))

	def __init__(self, InterviewerID, Interviewer, Position):
		self.InterviewerID = InterviewerID
		self.Interviewer = Interviewer
		self.Position = Position

class Question(db.Model):
	"""
	Question Model
	"""
	__tablename__ = 'Questions'
	QuestionID = db.Column(db.Integer, primary_key=True)
	Question = db.Column(db.Text)
	JobID = db.Column(db.Integer, db.ForeignKey('JobType.JobID'))
	TopicID = db.Column(db.Integer, db.ForeignKey('Topic.TopicID'))
	InterviewerID = db.Column(db.Integer, db.ForeignKey('Interviewer.InterviewerID'))
	Created = db.Column(db.DateTime, default=datetime.datetime.now())
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, QuestionID, Question, Created, Updated):
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
	QuestionID = db.Column(db.Integer, db.ForeignKey('Question.QuestionID'))
	Created = db.Column(db.DateTime, default=datetime.datetime.now())
	Updated = db.Column(db.DateTime, default=datetime.datetime.now())

	def __init__(self, AnswerID, Answer, Created, Updated):
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

	def __init__(self, JobID, JobPosition):
		self.JobID = JobID
		self.JobPosition = JobPosition

class Topic(db.Model):
	"""
	Topic Model
	"""
	__tablename__ = 'Topics'
	TopicID = db.Column(db.Integer, primary_key=True)
	TopicName = db.Column(db.String(60), unique=True)

	def __init__(self, TopicID, TopicName):
		self.TopicID = TopicID
		self.TopicName = TopicName