from flask import Flask
app=Flask(__name__)
@app.route("/hello")
def index():
    return "Flask Working fine"
@app.route("/laptop")
def india():
    return "abcddef"
if __name__=="__main__":
    app.run(host="0.0.0.0")


    
    
