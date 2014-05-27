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

from flask import Blueprint, render_template
from flask.ext.security import (login_required, roles_required, roles_accepted)
from flask_application.models import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/admin')
@roles_required('admin')
def admin_page():
    return render_template('security/index.html', content='Admin Page')

@admin.route('/admin_or_editor')
@roles_accepted('admin', 'editor')
def admin_or_editor():
    return render_template('security/index.html', content='Admin or Editor Page')