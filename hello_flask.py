from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Flask working fine"
  
if __name__=="__main__":
    app.run()