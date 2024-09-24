from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this!

jwt = JWTManager(app)

users = []

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = {
        'username': data['username'],
        'password': data['password']
    }
    users.append(new_user)
    return jsonify({"msg": "User created"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            access_token = create_access_token(identity=user['username'])
            return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
