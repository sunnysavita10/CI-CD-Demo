from ast import Return
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "CI-CD pipelines has been created."


if __name__=="__main__":
    app.run()