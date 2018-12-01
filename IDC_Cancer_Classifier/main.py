import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from IDC_Cancer_Classifier.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        pass

    return render_template('app/index.html')
