# -*- coding: utf-8 -*-
"""This file is part of the Daliegest project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
__author__ = 'Francesco Marella <francesco.marella@anche.no>'
__copyright__ = 'Copyright © 2014 Francesco Marella'

class Config(object):
    SECRET_KEY = '{SECRET_KEY}'
    SITE_NAME = 'DalieGest'
    SUBTITLE = 'Software gestionale'
    SITE_ROOT_URL = 'http://example.com'
    MEMCACHED_SERVERS = ['localhost:11211']
    SYS_ADMINS = ['foo@example.com']

    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    #DB_HOST = 'localhost'
    #DB_PORT = 27017

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
    

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
    
    DB = 'production'

class TestConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = False
    TESTING = True

class DevelopmentConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    '''Use "if app.debug" anywhere in your code, that code will run in development code.'''
    DEBUG = True
    TESTING = True

