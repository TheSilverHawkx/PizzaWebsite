from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db,parse_json

bp = Blueprint('orders', __name__)


@bp.route('/orders')
@login_required
def orders_page():
    if g.user["type"] == "Customer":
        query = F'SELECT * FROM Orders WHERE customerId == "{g.user["id"]}"'
    else:
        query = F'SELECT * FROM Orders'

    order_id = request.args.get("id")
    if order_id is not None:
        if g.user["type"] == "Customer":
            query += F' AND id == {order_id}'
        else:
            query += F' WHERE id == {order_id}'

    query += ' ORDER BY creationDate DESC'
    db = get_db()
    results = db.execute(query).fetchall()

    return render_template('orders/list_orders.html',orders=parse_json(results))