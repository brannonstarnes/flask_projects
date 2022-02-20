from flask import Flask
from markupsafe import escape

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


