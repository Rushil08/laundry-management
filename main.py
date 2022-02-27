from flask import Flask, render_template, request, flash, url_for
tees=0
pant=0
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('login.html')

database={'admin':'pass'}

@app.route("/login",methods=["POST","GET"])
def login():
    name=request.form['username']
    pwd=request.form['password']
    if name in database and database[name]==pwd:
        return render_template('home.html',value=name)
    else:
        return render_template('login.html',info='Invalid Username or Password')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/returntopage")
def returntopage():
    return render_template("login.html")

@app.route("/savinginfo",methods=['POST','GET'])
def savinginfo():
    name1=request.form['username_create']
    pwd1=request.form['password_create']
    database[name1]=pwd1
    return render_template("login.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")
@app.route("/status")
def status():
    return render_template("status.html",tees=tees,pant=pant)
@app.route("/deposit")
def deposit():
    return render_template("deposit.html")
@app.route("/page")
def page():
    return render_template('home.html')
@app.route("/dep",methods=["POST","GET"])
def dep():
    global tees,pant
    tees=request.form.get('tees')
    pant=request.form.get('pant')
    return render_template("status.html",tees=tees,pant=pant)

if __name__ == '__main__':
   app.run()