
This is an experiment with Flask building a ERP for small and medium businesses for the Italian market.

Software components:
- Flask
- AngularJS
- SQLalchemy
- sqlalchemy_utils
- Bower
- VirtualEnv

For a complete list, see requirements.txt

-----

Flask Boilerplate Project
=========================
http://flask.pocoo.org/

This project is meant to be helpful for those who want to quickly jump into a new flask project. Social Media Accounts, UserAccounts, Caching, Mail, User Registration, Roles, Python Script Commands, and Twitter Bootstrap are already configured. 

The Flask Boilerplate Project consists of many projects merged into one to provide the most comprehensive boilerplate for your flask project. It is set up to quickly connect to Google Apps to start sending emails and is fully configurable.

Installation
------------
1. Download via git:

        git clone git://github.com/hansonkd/FlaskBootstrapSecurity.git

2. Change into the cloned directory

        cd FlaskBootstrapSecurity

2. Get VirtualEnv and VirtualEnvWrapper set up. See here for further details: http://www.doughellmann.com/docs/virtualenvwrapper/
	
3. Create a virtualenvironment

        mkvirtualenv environment

4. Install the required python dependancies:

        pip install -r requirements.txt
    
5. As a temporary workaround, run this command to get a version of Flask-Social that works with the current mongoengine

        pip install --upgrade https://github.com/mattupstate/flask-social/tball/develop

6. Edit `flask_application/config.py` to change your mail server and other settings:

        class Config(object):
            SECRET_KEY = '{SECRET_KEY}'
            SITE_NAME = 'Flask Site'
            SITE_ROOT_URL = 'http://example.com'
            MEMCACHED_SERVERS = ['localhost:11211']
            SYS_ADMINS = ['foo@example.com']
    
            # Mongodb support
            MONGODB_DB = 'testing'
            MONGODB_HOST = 'localhost'
            MONGODB_PORT = 27017


            # Configured for GMAIL
            MAIL_SERVER = 'smtp.gmail.com'
            MAIL_PORT = 465
            MAIL_USE_SSL = True
            MAIL_USERNAME = 'username@gmail.com'
            MAIL_PASSWORD = '*********'
            DEFAULT_MAIL_SENDER = 'Admin < username@gmail.com >'
    
            # Flask-Security setup
            SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
            SECURITY_REGISTERABLE = True
            SECURITY_RECOVERABLE = True
            SECURITY_URL_PREFIX = '/auth'
            SECUIRTY_POST_LOGIN = '/'
    
            # Flask-Social setup
            SOCIAL_TWITTER = {
                'consumer_key': '',
                'consumer_secret': ''
            }


7. Run a development server:
        
        python manage.py runserver

Credit
------
####Required Python Projects:

* unittest2
* Flask
* Flask-Assets
* cssmin
* Flask-WTF
* Flask-Script
* Flask-Mail
* Flask-Cache
* python-memcached
* Flask-Security
* Flask-Social
* Flask-MongoEngine

####Non-Python Projects:
* Twitter Bootstrap

####Contributing Projects:
* https://github.com/swaroopch/flask-boilerplate _The project's structure is built from this_
* Flask-Security Example App
* https://github.com/earle/django-bootstrap _uses some template macros_

Usage
-----

##Commands
_Run these commands by using `python manage.py <command>`_


* `reset_db` - Drops all Mongo documents
* `populate_db` - Script to fill the database with new data (either for testing or for initial). You can edit the `populate_data` command in `flask_application/populate.py` (Right now it is set up to add Users.)
* `runserver` - Runs a debug server
* Commands included with Flask-Security can be found here: http://packages.python.org/Flask-Security/#flask-script-commands and by looking in `flask_application/script.py`

##Templates
The base template is based off of Django-bootstrap and is found under: `flask_application/templates/bootstrap/layouts/base_navbar_responsive.html`

##Static Content
This project is designed to use CSSMin and Flask-Assets to manage Assets to save on bandwidth and requests. 

You can find this in the `css_bootstrap` block of the layout template. You can also simply edit `static/css/site.css` as that is included in the base setup. 

##Encoding and Decoding Id's
Sometimes you won't want simple URLs revealing the order of the object ids. For example:
    
    http://example.com/users/view/1/

So you can use `encode_id` and `decode_id` found in `flask_application/helpers.py`

So 

        http://example.com/users/view/1/
        
becomes

        http://example.com/users/view/w3c8/



LICENSE &amp; COPYRIGHT
-----------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
