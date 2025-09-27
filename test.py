from flask import Flask,app
from flask import render_template ,request
'''it create an instance of flask class
which will be your wsgi(web server gateway interdface)application'''
#wsgi application
app=Flask(__name__)

@app.route("/school")
def welcome():
    return "hii i am a kumar yadav"

@app.route("/about")
def about():
    return "<html><H1>welcome to flask course guys I am a boy that </H1></html>"
    
@app.route("/form",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form.get('name')
        return f'hello{name}!'
    return render_template ('index.html')

@app.route("/submit",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form.get('name')
        return f'hello{name}!'
    return render_template ('index.html')


if __name__=="__main__":
    app.run(debug=True)