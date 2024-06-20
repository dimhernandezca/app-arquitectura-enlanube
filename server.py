from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register_page")
def register_page():
    return render_template("register.html")

if __name__ =="__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port)