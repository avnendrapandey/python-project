@app.route("/index",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        return f'hello{name}!'
    return render_template('index.html')