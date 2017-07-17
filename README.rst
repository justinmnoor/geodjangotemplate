* This project is being re-examined, and may be discontinued as I am unsure if Django continues to meet my needs. I am working with Javascript and GO these days, and have developed a keen interest in container technologies.
=================================================================================================================================


A SIMPLE GEODJANGO TEMPLATE
============================

Ready to add some geo to your Django? GeoDjango is an amazing GIS framework for web applications. This template will help get you started.


Project Background
===================

This is a simple GeoDjango template that provides just enough configuration to get you going. It includes a landing page that displays a basic slippy map, a blank 'about' page, and some general configuration for conducting geospatial analyses with Django.

This template was generated with audreyr's Cookie-Cutter templating utility. To see how it was made, take the Cookie-Cutter tutorials at:

    https://github.com/audreyr/cookiecutter

This template was highly inspired by pydanny's Cookiecutter-Django project. A few code snippets were borrowed from pydanny's project for the docs generation. This is not a formal fork/pull-request of pydanny's project because it probably would not make a formidable contribution to the pantry of Cookie-Cutters.

This project follows 'Two Scoops Principles', but surely it gets them wrong sometimes. Please send any suggestions on how it can be improved.

Check out audreyr and pydanny's projects:

  * https://github.com/audreyr
  * https://github.com/pydanny
  * https://www.twoscoopspress.com


Project Features
=================

* Built with Anaconda3 Python
* Works with Django 1.10 or later
* For use with Linux and Mac, or very adventurous Windows users
* AWS friendly!
* Setup with Gunicorn but can also be used with Apache
* Compatible with PostgreSQL and PostGIS
* Configured with Twitter Bootstrap v4.0.0-alpha.6
* Equipped with Leaflet JS 1.0.3
* Utilizes environment variables for secret keys and secret stuff
* Includes django-crispy-forms
* Manages static content with django-storages


GeoDjango Background
=====================

GeoDjango is not a separate installation of Django. The term mainly refers to a 'contrib.gis' module that is included with every Django project. For the most part, if you are using the 'contrib.gis' module, you are using GeoDjango.

GeoDjango does however require additional dependencies apart from the usual Django configuration. Namely, it requires a spatial database, and some geospatial libraries from the OsGeo Project. The spatial database chosen for this template is PostGIS (an extension of Postgresql). The geospatial libraries include GDAL, GEOS, Proj4, and more (see https://docs.djangoproject.com/en/1.10/ref/contrib/gis/tutorial).

The geospatial libraries are non-Python packages. For this reason, the Anaconda Python distribution is used for creating a project environment. Anaconda Python includes the conda package manager, which is a cross-platform tool that handles the geosptatial libraries with ease. Anaconda Python, created by Continuum Analytics, has gained much popularity in the Python community, and has a flourishing community of its own. See https://www.continuum.io/blog/developer-blog/python-packages-and-environments-conda.


Usage
======

1) Install the latest version of Anaconda3 Python from:
  
    https://www.continuum.io/downloads

2) Install the geospatial libraries:

  * For Debian/Ubuntu install these packages globally:

	    $ sudo apt-get install binutils libproj-dev gdal-bin

  * For Mac see: https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/#macosx.

  * For Windows see: https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/#windows.

3) Create a conda environment:
  
  * See notes on requirements below at the 'Important Notes' section.

  * Get the requirements file 'base.yml' from:

      https://gist.github.com/justinmnoor/5e7242a9ec48bef20a29b614bb999633

      or clone from:

      git@gist.github.com:5e7242a9ec48bef20a29b614bb999633.git

  * Change the 'name' value accordingly and save the file in your home directory.

  * Careful with yaml spacing! It has to be perfect!

  * At your terminal run:

      $ conda env create -f base.yml python=3

4) Activate your conda environment:
  
    $ source activate yourenv

5) Now CD into the directory of your local machine where you wish to store your Django project.

6) Run 'cookiecutter' against my github repo:

	  $ cookiecutter https://github.com/justinmnoor/geodjangotemplate

7) Answer the prompts with your information or it will use the [defaults]. You will be prompted for your AWS account info, which you can also ignore and fill in later.

8) CD into your Django project and have a look around. Add your project to a text editor.

9) Next install PostgresSQL 9.5 or later, and PostGIS 2.2 or later, on your local machine.

10) Create a PostgreSQL database with the same name that you specified when you ran cookiecutter against my github repo. You do not need to add the PostGIS extension. Geodjango takes care of that for you.

11) Log into your AWS account and create an S3 bucket with the same name that you specified when you ran cookiecutter against my github repo. See the notes on AWS configuration below.

12) To get your project rolling, see the 'install.rst' file located in the 'docs/' directory of your new Django project.

13) Conquer the world and don't look back.

14) It doesn't matter how fast you're going if you're headed in the wrong direction.


Important Notes
================

Regarding step 3, the requirements are installed this way because I haven't figured out how to install 'base.yml' into a pre-existing conda environment. This will need to be worked out. Ideally, there should be a 'local.yml', 'production.yml', and 'test.yml', all of which import from 'base.yml'. Please offer any suggestions. If none of this makes any sense, just complete step 3 and it will sink in later.

Yaml is used for 'base.yml' because the project dependencies are a mixture of conda-forge and pip packages. The conda-forge Django package greatly simplies the installation of the geospatial libraries. A BIG HUGE thank you goes out to the conda-forge community for building this package. If you are installing the geospatial libraries on Windows, may God be with you.

Json files are used for storing secret keys and secret stuff because they are lightweight and work amazingly well with Python. See the 'base.py' settings file at the 'ENVIRONMENT CONFIGURATION' section. These config files allow the user to keep passwords, keys, etc., out of version control by adding them to .gitignore. That said, add them to '.gitignore' now! I am currently exploring methods that utilize systemd or bash scripting for importing environment variables and will implement them ASAP. 


Notes on AWS Configuration
===========================

This project requires the use of an S3 bucket. Your S3 bucket needs to be configured manually before collecting static files.

The Django-Storages package is used to automatically collect static files into an S3 bucket. See: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html for more info on this package. Find the 'django-storages' settings in 'base.py' under 'AWS CONFIGURATION'.

CloudFront and Route 53 are optional but highly recommended, especially when working with geojson. These services need to be setup manually. See the 'Optional Steps for AWS' below. If you prefer not to use AWS, a service like Redis should be used for caching geojson.


Optional Steps for AWS:
------------------------

1) Setup a CloudFront cluster on AWS and update the 'aws_config.json' accordingly under 'aws_custom_domain'.

2) Configure Route 53.

3) Become a cloud guru.


Credits and Inspiration (in alpha order by first name):
========================================================

Audrey and Danny Roy Greenfield,
Jacob Kaplan-Moss,
Jeff Knupp,
Justin Mitchell,
Kenneth Love,
Linus Torvalds,
Revolution Systems (revsys.com),
Richard Stallman,
Twelve Factor App,
Two Scoops Academy

