####bulding url dynamicallly
####variables rule 
###jinga 2 template engine

###jinga2 template engine
'''
{{ }}  expressions to print  output in html
{%...%} condition , for loops
{#...#}this is for comments
'''


from flask import Flask,app
from flask import render_template ,request
'''it create an instance of flask class
which will be your wsgi(web server gateway interdface)application'''
#wsgi application
app=Flask(__name__)


@app.route("/about")
def about():
    return "<html><H1>welcome to flask course guys I am a boy that </H1></html>"
    
'''@app.route("/form",methods=['GET','POST'])
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
    return render_template ('index.html')'''


##variable rule
@app.route('/success/<int:score>')
def success(score):
    return "the marks you got" + str(score)


#bulding url dynamically
'''@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"

        return render_template('result.html', results=res)'''



if __name__=="__main__":
    app.run(debug=True)
