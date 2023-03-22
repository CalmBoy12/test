from flask import Blueprint, Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import bcrypt
from datetime import datetime


load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('users', __name__)

mongo = PyMongo(app, retryWrites=False)


@blueprint.route("/")
def articleGetAll():
    users = mongo.db.user
    users_data = users.find({})
    data = []
    for x in users_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    print('usersssssssss', data)

    return jsonify({'success': True, "data": data})


@blueprint.route("/signin", methods=["POST"])
def signin():
    add = mongo.db.user
    data = request.get_json(force=True)
    data['email'] = data['email']
    existUser = add.find_one({'email': data['email']})
    print('dataaaaa', existUser)
    if(existUser):
        passwordCheck = bcrypt.checkpw(
            data['password'].encode('utf8'), existUser['password'])
        if(passwordCheck):
            return jsonify({'success': True, 'message': 'User Find!!!', 'email': data['email'], 'name': existUser['name'], 'uid': str(existUser['_id'])})
        else:
            return jsonify({'success': False, 'message': 'Invalid Email Or Password!!!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid Email Or Password!!!'})


@blueprint.route("/signup", methods=["POST"])
def registerUser():
    add = mongo.db.user
    data = request.json
    existUser = add.find_one({'email': data['email']})
    if(existUser):
        return jsonify({'success': False, 'message': 'User Already Exist!!!'})
    else:
        hashed_password = bcrypt.hashpw(
            data['password'].encode('utf8'), bcrypt.gensalt(12))
        add_data = add.insert_one({
            'name': data['name'],
            'email': data['email'],
            'password': hashed_password})
        return jsonify({'success': True, 'message': 'Successfully Registered', 'email': data['email'], 'name': data['name'], 'uid': str(add_data.inserted_id)})


@blueprint.route("/social-login", methods=["POST"])
def socialLogin():
    add = mongo.db.user
    data = request.get_json(force=True)
    existUser = add.find_one({'email': data['email'], 'uid': data['uid']})


    if(existUser):
        return jsonify({'success': True, 'message': 'User Login Sucessfully!!!', 'data': {'email': existUser['email'], 'fullName': existUser['fullName'], 'uid': existUser['uid'], '_id': str(existUser['_id'])}})
    else:
        add_data = add.insert_one({
            'fullName': data['fullName'],
            'email': data['email'],
            'uid': data['uid'],
            'created_at': datetime.now()
        })
        add_data
        # print('add_data', add_data)
        return jsonify({'success': True, 'message': 'User Signin Sucessfully!', 'data': {'email': data['email'], 'fullName': data['fullName'], 'uid': data['uid'], '_id': str(add_data.inserted_id)}})
