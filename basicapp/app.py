from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# "/" stands for home direcotry
@app.route("/")
def home():
    #rendering html file
    return render_template("index.html")
@app.route("/login", methods = ["POST", "GET"])
def login():
    #requests library handles all the requests on the web page
    if request.method == "POST":
    #form is a dictionary and we are returiving user name from key "nm" declared in the html form tag
        user = request.form["nm"]
    #after submit we are redirectoring user to this page and passing user as attribute
        return redirect(url_for("user", usr = user))
    else:
        # if no submit evnet is generated send user to login page and ask user to login
        return render_template("login.html")
@app.route("/usr")
def user(usr):
    # we are rending a inline html to show user name
    return f"<h1>{usr}</h1>"
    #entry point of our web page


if __name__ == "__main__":
    app.run()
