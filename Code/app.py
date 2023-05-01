from flask import Flask

# create a Flask application:
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Jovian!</p>"


print(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
    # print("i'm inside the if statement")
    


