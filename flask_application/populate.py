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

from flask_application import user_datastore, app
from flask_application.models import db


def create_users():
    db.create_all()
    user_datastore.create_user(email='fra@marella.net', password='qwerty')
    db.session.commit()

def populate_data():
    create_users()