django-beginners-tutorial
=========================

To help others who will go before me. Specifically, making a Django project easier to get started with.

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

##### Use pip to install Django
* pip install Django==1.6.10 (use sudo to install globally)

Start a new Django project (or clone this repository)
-----------------------------------------------------

* mkdir begin_django
* cd begin_django
* django-admin.py startproject myproject

Run the local server
--------------------

* cd begin_django/myproject
* python manage.py runserver
* Go to 127.0.0.1:8000 in a browser window

Create the initial tables for the database (sqlite)
---------------------------------------------------

* cd begin_django/myproject
* python manage.py syncdb
