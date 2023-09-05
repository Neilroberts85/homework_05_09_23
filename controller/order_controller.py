from flask import Blueprint
from flask import render_template
from models.order_list import orders

order_blueprint = Blueprint("orders",__name__)

@order_blueprint.route("/orders")
def index():
    return render_template('index.jinja', title="My Order List", orders=orders)

@order_blueprint.route("/orders/one_order")
def order1(one_order):
    return render_template('order.html', title="one order", orders=orders)