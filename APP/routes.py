from flask import Blueprint,request
import base64
base_routes = Blueprint('base_routes', __name__,
                        template_folder='templates')


users = ['','user']
@base_routes.route('/user/<user>',methods=['GET','POST'])
def userchecker(user):
    if request.method == 'POST':
        if user not in users:
            users.append(user)
            return 'ok'
        else: 
            return 'invalid'
    else:
        if user not in users:
            return 'valid'
        else: 
            return 'invalid'