from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Capgemini(v2.0) ,friends how are you all doing!!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)