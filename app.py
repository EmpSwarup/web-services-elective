# import flask module
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world(  ):
    return render_template("login.html")
  
@app.route("/register")
def register(  ):
    return render_template("register.html")
  
@app.route("/home")
def home():
   return "<p>Hello, daku</p>"
    
if __name__ == '__main__':  
  app.run(debug=True)