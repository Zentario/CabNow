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
    return "<h1>File contents</h1><h4>" + str(read_drivers()) + "</h4>" + "<h4>" + str(read_users()) + "</h4>"


@app.route("/deleteuser", methods=['POST'])
def deleteUser():
        if(request.method == 'POST'):
                data = read_users()
                name = request.get_json()['name']
                if(name in data['users'].keys()):
                        del data['users'][name]
                        write_users(data)
                        return jsonify({ name : "Deleted"}), 200

                return jsonify({}), 400  

        else:
                return jsonify({}), 401


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
                return jsonify({}), 401


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
                return jsonify({}), 401


# Signup
@app.route("/adduser", methods=['POST'])
def addUser():
        if(request.method == 'POST'):
                name = request.get_json()['name']
                pwd = request.get_json()['password']
                phone_no = request.get_json()['phone_no']
                data = read_users()

                if(name in data['users'].keys()):
                        return jsonify({"message" : "User already exists"}), 400

                data['users'][name] = {"password" : pwd, "phone_no" : phone_no}
                write_users(data)
                #return jsonify({"name": name, "password" : pwd, "phone_no" : phone_no}), 201
                return jsonify({"message" : "User created successfully"}), 201

        else:
                return jsonify({"message" : "Bad method"}), 401


# Login
@app.route("/login", methods=['POST'])
def loginUser():
        if(request.method == 'POST'):
                
                data = read_users()
                name = request.get_json()['name']
                pwd = request.get_json()['password']
                
                if(name not in data['users'].keys()):
                        return jsonify({"message" : "No such user"}), 400
                
                if(pwd != data['users'][name]["password"]):
                        return jsonify({"message" : "Password is wrong"}), 400
                
                return jsonify({"message" : "Login successful"}), 200

        else:
                return jsonify({"message" : "Bad method"}), 401




#For testing only
#if __name__ == "__main__":
#    app.run(host="127.0.0.1", port=5000, debug=True)
