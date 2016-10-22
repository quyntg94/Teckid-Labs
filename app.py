from flask import *
from mlab import *
from mongoengine import *

app = Flask(__name__)
mlab_connect()

class Post(Document):
    title = StringField()
    content = StringField()
    def to_json(self):
        return {"title": self.title, "content": self.content}

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return jsonify([post.to_json() for post in Post.objects])
    elif request.method == "POST":
        form = request.form
        title_value = form["title"]
        content_value = form["content"]

        p = Post(title = title_value, content = content_value)
        p.save()

        return jsonify({"code": 1, "message": "OK"})

if __name__ == '__main__':
    app.run()