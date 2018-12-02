import functools
import os
import uuid

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

from IDC_Cancer_Classifier.db import get_db

from .classifier.prediction import predict

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        file = request.files['loadImage']
        filename = '{0}.png'.format((str(uuid.uuid4())))
        path = os.path.join(current_app.root_path, 'uploads', filename)

        file.save(path)

        predict(path)

    return render_template('app/index.html')
