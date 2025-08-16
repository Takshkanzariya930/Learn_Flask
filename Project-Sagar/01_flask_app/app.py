from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__,template_folder="templates")
app.secret_key = "123321"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "111":
            session['user'] = username
            return redirect(url_for("welcome"))
        
        else:
            return "Invalid - Username and Password"
        
    else:
        return render_template("index.html")

@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html",user=session['user'])
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)