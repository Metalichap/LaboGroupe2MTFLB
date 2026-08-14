from flask import render_template

from app import app
from app.framework.decorators.inject import inject

@app.route('/sites', methods=['GET'])
@inject
def get_sites():
    pass