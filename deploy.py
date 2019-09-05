from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def read_users():
    with open('users.json', 'r') as infile:
        data = json.load(infile)
    return dict(data)

def write_users(data):
    with open('users.json', 'w') as outfile:
        json.dump(data, outfile)


def read_drivers():
    with open('drivers.json', 'r') as infile:
        data = json.load(infile)
    return dict(data)

def write_drivers(data):
    with open('drivers.json', 'w') as outfile:
        json.dump(data, outfile)


@app.route("/")
def test():
        return '<h1>Deployed on Heroku !</h1><h3>SE Project</h3>'


@app.route("/test")
def test_v1():
        return jsonify( {"users.json" : read_users(), "drivers.json" : read_drivers() })



@app.route("/deleteuser", methods=['POST'])
def deleteUser():
        if(request.method == 'POST'):
                data = read_users()
                phone = request.get_json()['phone_no']
                if(phone in data['users'].keys()):
                        user = data['users'][phone]
                        del data['users'][phone]
                        write_users(data)
                        return jsonify({"error": False, "message" : "User deleted", phone : user}), 200
                else:
                        return jsonify({"error": True, "message" : "User does not exist", "phone_no" : phone}), 400  

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405

@app.route("/getusers", methods=['GET'])
def getusers():
        if(request.method == 'GET'):
                data = read_users()
                users = data["users"]
                if(len(users) == 0):
                        return jsonify({"error": True, "message" : "Users list empty"}), 204

                return jsonify({"error": False, "users": users}), 200

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405
        

@app.route("/getuser", methods=['POST'])
def getuser():
        if(request.method == 'POST'):
                data = read_users()
                users = data['users']

                phone = request.get_json()['phone_no']
                if(phone not in users.keys()):
                        return jsonify({"error": True, "message" : "User does not exist"}), 400

                return jsonify({"error": False, "user" : { phone : users[phone]} }), 200

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405


@app.route("/adddriver", methods=['POST'])
def addDriver():
        if(request.method == 'POST'):
                name = request.get_json()['name']
                status = request.get_json()['status']
                phone_no = request.get_json()['phone_no']
                rating = request.get_json()['rating']
                lat = request.get_json()['latitude']
                lng = request.get_json()['longitude']

                data = read_drivers()

                if(name in data['drivers'].keys()):
                        return jsonify({"status" : "error", "message" : "Driver already exists"}), 400

                data['drivers'][name] = {"latitude" : lat, "longitude" : lng, "phone_no" : phone_no, "status" : status, "rating" : rating}
                write_drivers(data)
                return jsonify({"name": name, "message" : "Created driver"}), 201

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405


@app.route("/deletedriver", methods=['POST'])
def deleteDriver():
        if(request.method == 'POST'):
                data = read_drivers()
                name = request.get_json()['name']
                if(name in data['drivers'].keys()):
                        del data['drivers'][name]
                        write_drivers(data)
                        return jsonify({ name : "Deleted"}), 200

                return jsonify({}), 400  

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405


# Signup
@app.route("/adduser", methods=['POST'])
def addUser():
        if(request.method == 'POST'):
                pwd = request.get_json()['password']
                phone_no = request.get_json()['phone_no']
                data = read_users()

                if(phone_no in data['users'].keys()):
                        return jsonify({"error" : True, "message" : "User already exists"}), 400

                data['users'][phone_no] = {"password" : pwd}
                write_users(data)
                return jsonify({"error" : False, "message" : "User created successfully", phone_no : data["users"][phone_no]}), 201

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405


# Login
@app.route("/login", methods=['POST'])
def loginUser():
        if(request.method == 'POST'):
                
                data = read_users()
                phone = request.get_json()['phone_no']
                pwd = request.get_json()['password']
                
                if(phone not in data['users'].keys()):
                        return jsonify({"error" : True, "message" : "No such user"}), 400
                
                if(pwd != data['users'][phone]["password"]):
                        return jsonify({"error" : True, "message" : "Password is wrong"}), 400
                
                return jsonify({"error" : False, "message" : "Login successful", phone : data["users"][phone]}), 200

        else:
                return jsonify({"error" : True, "message" : "Bad method"}), 405




#For testing only
#if __name__ == "__main__":
#    app.run(host="127.0.0.1", port=5000, debug=True)
