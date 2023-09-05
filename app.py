from flask import Flask
from controller.order_controller import order_blueprint

app = Flask(__name__)
app.register_blueprint(order_blueprint)