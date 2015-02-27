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
