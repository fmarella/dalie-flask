#!/usr/bin/env python
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

import datetime

from flask import Blueprint, render_template, jsonify
from flask_application import app
from flask.ext.security import login_required

from flask_application.models import db, Cliente

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template(
                'index.html',
                config=app.config,
                now=datetime.datetime.now,
            )

@frontend.route('/profile')
@login_required
def profile():
    return render_template(
        'profiles/profile.html',
        content='Profile Page',
        twitter_conn=app.social.twitter.get_connection())

@frontend.route('/clienti')
def foo():
    c = Cliente.query.all()
    return jsonify(clienti=c[0].as_dict())