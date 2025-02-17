# from flask import Flask ,redirect, url_for, render_templates, request

# app=Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route('/admin')
# def admin():
#     return redirect(url_for('home'))

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method=="POST":
#         user=request.form["nm"]
#         return redirect(url_for("user",usr=user))
#     else:
#         return render_template("login.html")

# @app.route("/<usr>")
# def user(usr):
#     return f"Hello, {usr}!"

# if __name__ == "_main_":
#     app.run(debug=True)

# #jhinjha2

from flask import Flask, render_template, redirect, request,url_for
# creating a instance of class flask
app=Flask(__name__)#app is an object
@app.route("/")
def home():
    #rendering index.html
    return render_template("index.html")

#login page mthds allowed: post, get
@app.route('/login', methods=["POST", "GET"])
def login():
    #request lib handles all the req. of our webpage
    #if mthd is post send user to his local page
    if request.method=="POST":
        #form is a dictionary and we are retrieving the user name from key 'nm' declared in html form tag
        user = request.form["nm"]# retrieve data from form
        #after submission of form redirect to user page & passing user as attribute
        return redirect(url_for("user",usr=user))# redirecting to user page
    else:
        #if no submit event is generated send user to login page and ask to login
        return render_template("login.html")

#<usr> is used to send variable to our mthd
@app.route('/<usr>')
def user(usr):
    #rendering a inline html to show user name
    return f"Hello, {usr}!"#display msg

#entry point of our webpage
if __name__=="__main__":
    app.run(debug=True)
