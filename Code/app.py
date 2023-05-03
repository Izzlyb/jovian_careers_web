from flask import Flask, render_template

# create a Flask application:
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
    # print("i'm inside the if statement")
    


