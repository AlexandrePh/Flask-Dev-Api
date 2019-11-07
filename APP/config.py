from flask import  Flask


from APP.routes import base_routes
#APP CONFIG
app = Flask(__name__, template_folder='templates')
app.register_blueprint(base_routes)
#BLUEPRINTS CONFIG


@app.route('/')
def hello_world():
    return "hello"