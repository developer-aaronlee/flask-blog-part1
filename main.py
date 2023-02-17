from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
all_posts = []
for x in data:
    post = Post(x["id"], x["title"], x["subtitle"], x["body"])
    all_posts.append(post)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    current_post = None
    for x in all_posts:
        if x.id == post_id:
            current_post = x
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
