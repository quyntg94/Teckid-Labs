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

@app.route('/')
def hello_world():
    return jsonify([post.to_json() for post in Post.objects])

if __name__ == '__main__':
    app.run()