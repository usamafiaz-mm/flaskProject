import time

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# db =  SQLAlchemy(app)


@app.route('/getrecord', methods=["GET"])
def get_demo():
    name = request.args.get('name')
    return {'message': f"Hello {name}"}


@app.route('/postrecord', methods=["POST", "GET"])
def post_demo():
    # name = request.args.get('name')
    # email = request.args.get('email')
    # password = request.args.get('password')
    # print("POST METHOD WAS CALLED")
    # return {"name": name, 'email': email, 'company': "MicroMerger"}

    print(request.form)
    print("name", request.form.get("name"))
    print("email", request.form.get("email"))
    print("password", request.form.get("password"))
    return {"name": request.form.get("name"), "email": request.form.get("email"), "company": "MicroMerger MM"}


@app.route("/")
def hello():
    return "Hello"


@app.route("/oncreate", methods=["GET"])
def on_create():
    print("on Create Method was called")
    return {"message": "API MESSAGE : Activity Started"}


@app.route("/onback", methods=["GET"])
def on_back():
    print("on Back Method was called")
    return {"message": "API MESSAGE : Activity Resumed"}


@app.route("/login", methods=["GET"])
def login():
    if request.method == "GET":
        email = request.args.get("email")
        password = request.args.get("password")
        name = email.split('@')[0]
        name = ''.join(i for i in name if not i.isdigit())
        print("LOGIN METHOD WAS CALLED BY ", name)
        print(request.remote_addr)

        return {"name": name, "email": email}


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=3000)
