import json
from flask import Flask

app = Flask(__name__)

post1 = {
    "title" : "Good day",
    "content" : "Today, i met a girl. She has black eyes and loves ice-cream"
}

post2 = {
    "title" : "Bad day",
    "content" : "Today, i met a boy. He has black eyes and loves ice-cream"
}

print(post1["title"])
print(post1["content"])

@app.route('/')
def hello_world():
    return json.dumps(post1)

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)