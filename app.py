from flask import Flask

app = Flask(__name__)

#http://IP주소:5000/
@app.route("/")
def index():
    return "Hello World"

#http://IP주소:5000/abc
@app.route("/abc")
def hello_abc():
    return "Hello abc"

if __name__ == '__main__':
    app.run('0.0.0.0')