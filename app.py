from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello world')
    return 'Hello world'

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)