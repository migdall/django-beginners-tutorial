Django Beginners Tutorial
=========================

##### Purpose

To help those who will learn Django in the future and as a resource for what I think is most important when starting a new Django project.

##### Start

Django 1.6 Overview: https://docs.djangoproject.com/en/1.6/intro/overview/

Have Python 2.7+ installed on your computer.

Basic Installation
------------------

##### Install virtualenv locally
* mkdir ~/src
* wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-12.0.7.tar.gz#md5=e08796f79d112f3bfa6653cc10840114 --no-check-certificate
* tar -zxvf virtualenv-12.0.7.tar.gz
* cd virtualenv-12.0.7/
* python setup.py install

##### Install pip
* http://pip.readthedocs.org/en/latest/installing.html

##### Install pip locally
* cd ~/src, use mkdir ~/src if you do not have the ~/src directory
* wget https://pypi.python.org/packages/source/p/pip/pip-6.0.8.tar.gz#md5=2332e6f97e75ded3bddde0ced01dbda3 --no-check-certificate
* tar -zxvf pip-6.0.8.tar.gz
* cd pip-6.0.8/
* python setup.py intall

Installing virtualenv and pip locally is good if you do not have sudo access, want to try different versions of the software, and for other reasons. This installation is also helpful when you want to try another version of Python. The steps listed for installing virtualenv and pip locally are very similar to the steps you might take in installing a local version of Python.

The foundation for the local installation steps of virtualenv and pip can be found in this StackOverflow answer located at this address http://stackoverflow.com/questions/5506110/is-it-possible-to-install-another-version-of-python-to-virtualenv.

Clone this repository
-----------------------------------------------------

* git clone https://github.com/migdall/django-beginners-tutorial.git

Create a virtual environment
-----------------------------------------------------

* cd django-beginners-tutorial/
* virtualenv env
* source env/bin/activate
* pip install Django==1.6.10

Create the initial tables for the database (sqlite)
-----------------------------------------------------

* cd django-beginners-tutorial/myproject/
* python manage.py syncdb

Run the local server
-----------------------------------------------------

* cd django-beginners-tutorial/myproject/
* python manage.py runserver
* Visit 127.0.0.1:8000 in a browser window
