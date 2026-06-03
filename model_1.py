from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")

def home():
    return "hello! this page <h1>hello11</h1>"
@app.route("/<name>")
def user(name):
    return f"hello {name}"
@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin !")) 
if __name__ == "__main__":
    app.run()