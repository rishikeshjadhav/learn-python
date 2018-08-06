from flask import Flask
app = Flask(__name__)

@app.route("/")
def hey():
    return 'Hey there'

@app.route("/hello")
def hello():
    return 'hello there'

if __name__ == "__main__":
    app.run()