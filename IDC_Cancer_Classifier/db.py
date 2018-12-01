import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Creates a database instance
    :return: database instance
    """

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = dict_factory

    return g.db


# noinspection PyUnusedLocal
def close_db(e=None):
    """
    Close database connection
    :param e: event
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """
    Initializes the database with a schema that corresponds to the station type (cable lock, dome)
    """

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """
    Initializes the application
    :param app: application instance
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def dict_factory(cursor, row):
    """
    Converts a row into a dictionary
    """
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d
