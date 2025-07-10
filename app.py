from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
     data="sarisha"     
     age=19
     return render_template("index.html",data=data,age=age)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/filecss")
def filecss():
    return render_template("index2.html")

@app.route("/about/<data>")
def sayHi(data):
    return f"Hello {data}"

@app.route('/register',methods=["GET","POST"])
def register():
    error=""
    if request.method=="POST":
        name=request.form['txtfullname']
        email=request.form['txtEmail']
        password=request.form['txtPassword']
        repass=request.form['RetypePassword']
     
        if password!= repass:
            error="password doesnot match "
            return render_template("register.html", error=error)
         
        return f"Name: {name} and Email: {email}"
 
    return render_template("register.html",error=error)

if __name__ =="__main__":
    app.run(debug=True)
