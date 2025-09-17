from flask import Flask
'''it create an instance of flask class
which will be your wsgi(web server gateway interdface)application'''
#wsgi application
app=Flask(__name__)

@app.route("/school")
def welcome():
    return "welcome to flak course"


