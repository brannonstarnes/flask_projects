from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World from Flask. This route is '/' </p>"

@app.route("/night")
def goodnight():
    return "<p>Goodnight, World! From route '/night' </p>"

# using variable rules in Flask Routes
# These need to be escaped to prevent HTML injection attacks
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"


# Using url_for 
@app.route('/login')
def login():
    return 'login'

@app.route("/new-user/<new_user>")
def new_user(new_user):
    return f"{new_user}'s profile"

with app.test_request_context():  ## tells Flask to act like it is handling a request even while in a shell env. CONTEXT LOCAL, useful for testing
    print(url_for('hello_world'))
    print(url_for('login'))
    print(url_for('new_user', new_user="Sally")) ## Here you can see reversed URL creation, where url is built based on input
    print(url_for('goodnight'))

