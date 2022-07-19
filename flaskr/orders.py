from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('orders', __name__)


@bp.route('/orders')
@login_required
def orders_page():
    if g.user.type == "customer":
        return db.execute('SELECT * FROM Orders WHERE customerId == "?" ORDER BY creationDate DESC',(user.id)).fetchall()
    else:
        db = get_db()
        orders = db.execute('SELECT * FROM Orders ORDER BY creationDate DESC').fetchall()
        return orders