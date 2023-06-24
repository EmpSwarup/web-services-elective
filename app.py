# import flask module
from flask import Flask, render_template,request, redirect
import pymysql

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        a_email = request.form["email"]
        a_password = request.form["password"]
        print(a_email,a_password)
        
        print("Connecting to database")
        conn = pymysql.connect(
            host='localhost',
            user="root",
            password="",
            db='elective' 
        )
  
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE username='%s' and password='%s';" % (a_email,a_password)
        cur.execute(query)
        output = cur.fetchall()
        print(output)
        conn.close()
        if len(output) > 0:
            return redirect('/home')

    return render_template("login.html")
  
@app.route("/register")
def register(  ):
    return render_template("register.html")
  
@app.route("/home")
def home():
   return "<p>Hello, daku</p>"
    
if __name__ == '__main__':  
  app.run(debug=True)