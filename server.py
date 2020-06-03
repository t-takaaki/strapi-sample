from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/posts')
def posts():
    res = requests.get('http://localhost:1337/posts')
    posts = json.loads(res.content)
    return render_template('posts.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
