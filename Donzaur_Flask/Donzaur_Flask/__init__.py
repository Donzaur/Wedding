"""
The flask application package.
"""

from flask import Flask, request
app = Flask(__name__)

import Donzaur_Flask.views
