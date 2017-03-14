Project Name: {{cookiecutter.project_name}}
Project Domain: {{cookiecutter.domain_name}}
Project Version: {{cookiecutter.version}}
Django Version: {{cookiecutter.django_version}}
PostGIS Version: {{cookiecutter.postgis_version}}
PostgreSQL Version: {{cookiecutter.postgresql_version}}
Anaconda3 Distribution: {{cookiecutter.anaconda3_python_version}}
Conda Environment: {{cookiecutter.conda_env_name}}
Author/s: {{cookiecutter.author_name}}
Author email: {{cookiecutter.email}}
Date: {% now 'utc', '%x' %}
Timezone: {{cookiecutter.timezone}}


SETUP INSTRUCTIONS
===================

If you're reading this, you have successfully generated a Geodjango project from a Conda environment, and you have ran the 'cookiecutter' command against my github repo at 'https:github.com/justinmnoor/geodjangotemplate'. You have also created a PostgreSQL/PostGIS database on your local machine, and an S3 bucket in your AWS account. Your database and bucket have the names that you specified when you ran cookiecutter against my github repo. If you have not completed these steps, see the 'README.rst' document at 'https://github.com/justinmnoor/geodjangotemplate', and complete them.


First Steps for Your New GeoDjango Project:
============================================

1) Activate your conda env.

2) CD into the root directory of your Django project (where 'manage.py' lives).

3) Make sure you've added your aws keys and S3 bucket name your 'aws_config.json' file.

	$ python manage.py collectstatic
	
4) Login to AWS and veryify that your static files were collected into your S3 bucket.

5) 	$ python manage.py migrate

6)  $ gunicorn {{cookiecutter.project_slug}}.wsgi
	
      * Click on the link to the running server.

      * Your landing page should show a jumbotron, a basic slippy-map, and a navbar with a couple of links.

      * See notes on settings files below at the 'Important Notes' section.

7) Exit the server:
    
    'Ctrl C'

8) Add db_config, dj_config, and aws_config to .gitignore.

9) Create a git repository in the root directory of your Django project:
	
	$ git init

	$ git add .
	
	$ git commit -m "first commit"
	
	$ git remote add origin git@github.com:yourname/yourprojectrepo.git (or wherever your repo is)
	
	$ git push -u origin master

10) Optional (highly recommended!):

	  * Setup AWS Cloudfront and update your aws_config.json file accordingly.

	  * Setup Route 53.

11) Now you can start serving and analyzing geospatial data!

12) My 'geodjangoapps' template might help you.
	
    https://github.com/justinmnoor/geodjangoapps

14) Be sure to take my tutorials on GeoDjango as well (coming soon).

15) Get to work.

16) Accomplish big things and be a disruptor.


Important Notes
================

Do not run 'django-admin startproject'!! Cookie-Cutter took care of that for you. Your project is already generated :).

Json files are used for storing secret keys and secret stuff because it is lightweight and works amazingly well with Python. Json config files will also work with Apache if needed.

There are three config files: 1) db_config, 2) dj_config, and 3) aws_config, located in the {{cookiecutter.project_slug}}/config directory. Variables are set when you generate your Django project. See the code in your 'base.py' settings file at the 'ENVIRONMENT CONFIGURATION' section. You can also refer to 'hooks.py' in the github repo. 

Config files stay out of version control so add them to '.gitignore' ASAP.

Regarding step 6, this project separates settings files as a best practices approach. Running Django's development server will default to 'local.py' settings. Running Gunicorn will default to 'production.py' settings. All settings import from 'base.py'. If you've collected your static files into your S3 bucket, your static content will be served when running Gunicorn.

