from src.models.Invoice import *
from src.database import Database
from flask import Flask, render_template, request, session, jsonify
from src.models.user import User
from pusher import Pusher

app = Flask(__name__)
app.secret_key = "lucy"


@app.route('/login')
def login():
    return render_template("log_in.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None  # If the user is not successfully logged in

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])


@app.route('/')
def start_dashboard():
    parent_data = {'dat': [0, 10, 5, 2, 20, 30, 45]}
    parent_time = {'label': ['January', 'February', 'March', 'April', 'May', 'June', 'July']}
    return render_template("dashboard.html", parent_data=parent_data, parent_time=parent_time)


@app.route('/data')
def data():
    return jsonify({'results': [0, 10, 5, 2, 20, 30, 45],
                    'label': ['January', 'February', 'March', 'April', 'May', 'June', 'July']})


if __name__ == '__main__':
    app.run()

# invoice1 = QInvoice(10000000,1,1,1,1,1,1,1,1,1,1,1,1,1,1)


# invoice1.save_to_mongo()

# invoice1.change_late_day("HELLO! I'm changing the late day!")

# user_input = input("What is the record")

# x = list(input("Enter a multiple value: ").split())

# x = list(map(str, input("Enter a multiple value: ").split()))

# for record in x:
# print(record)
