# CareerHack

People who are interviewing for tech companies generally rely on Glassdoor to know what questions they could be asked. Glassdoor allows anonymous users to post their application experience. People write about what the interviews were like, the difficulty of the interviews, and any questions they were asked. While this is a great resource, there a few flaws. People cannot see what specific person at the company asked the question, and their role. Many times, the interview questions depend heavily on who is conducting the interview. Another flaw is that answers cannot be posted. Users are unable to post their solutions to the questions. Our aim with this project was to solve this problem. 

CareerHack is a resource for people who are interviewing in tech companies. This website allows job hunters to find what questions they could be asked when they are interviewing. They can not only see the questions that have been asked before but also see by what company they were asked by, what specific person asked them the question, the role of that person at the company, possible answers to the question they asked, and when the question was asked. They can figure out the question they might be asked selecting the company name, or topic, or job type. 

Furthermore, CareerHack allows people to anonymously post questions they have been asked. After specifying the necessary details, it becomes part of the CareerHack database. The anonymity encourages users to questions without fear of prosecution.

Currently, CareerHack is running on Heroku via:

[http://careerhack.herokuapp.com](http://careerhack.herokuapp.com/)

Installing
=======

CareerHack requires Python 2.7.x and the following pip modules:

And the following modules (found in [requirements.txt](https://github.com/g12mcgov/CareerHack/blob/master/requirements.txt)):

    Flask==0.10.1
	Flask-SQLAlchemy==2.1
	Jinja2==2.8
	MarkupSafe==0.23
	SQLAlchemy==1.0.9
	Werkzeug==0.11.2
	gunicorn==19.4.1
	itsdangerous==0.24
	psycopg2==2.6.1
	wsgiref==0.1.2

Setup
=======

I suggest first creating a virtual environment via [virtualenv](https://virtualenv.pypa.io/en/latest/) before installing the below requirements. Otherwise, they'll be installed globally. 

Anyways, to install the pip modules run:

```bash
$ sudo python setup.py install
```
This will also create a build package.

Then, to run the app on port 5000 (default), type:

```bash
$ python app.py
```

You can also make this an exectuable via:

```bash 
$ chmod +x app.py
```

And run it via:

```bash 
./app.py
```
