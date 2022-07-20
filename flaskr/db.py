import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def parse_json(results: list) -> str:
    result_list = []
    for row in results:
        entry = {}
        for key in row.keys():
            entry[key] = row[key]
        
        result_list.append(entry)
    
    return result_list

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('queries\schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('add-db-mock-data')
@with_appcontext
def add_db_mock_data_command():
    """Adds Mock data to based on 'queries\\add-products' sql query."""
    
    db = get_db()

    click.echo('Adding products mock data...')
    with current_app.open_resource('queries\\add-products.sql') as f:
        db.executescript(f.read().decode('utf8'))
        

    click.echo('Adding users mock data...')
    db.execute("INSERT INTO Users (username,password,displayName) VALUES (?,?,?)",('customer1',generate_password_hash('Aa123456'),'customer 1'))
    db.execute("INSERT INTO Users (username,password,displayName,type) VALUES (?,?,?,?)",('employee1',generate_password_hash('Aa123456'),'employee 1','Employee'))
    db.execute("INSERT INTO Users (username,password,displayName,type) VALUES (?,?,?,?)",('admin',generate_password_hash('Aa123456'),'admin 1','Admin'))
    db.commit()

    click.echo('Adding orders mock data...')
    with current_app.open_resource('queries\\add-orders.sql') as f:
        db.executescript(f.read().decode('utf8'))

    click.echo('Added mock data successfully.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_db_mock_data_command)

