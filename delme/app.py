
from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/input/')
def form():
    return render_template('input.html')
 
@app.route('/output/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/input' to submit form"
    if request.method == 'POST':
        form_data = request.form
        a=[]
        try:
            salary=float(form_data['salary'])
        except:
            a.append('salary')
             
        try:
            bonus=float(form_data['bonus'])
        except:
            a.append('bonus')
             
        try:
            taxes=float(form_data['taxes'])
        except:
            a.append('taxes')
        
        if a != []:
            return render_template('error.html',error = a)
        
        result = salary + bonus - taxes   
        
        return render_template('output.html',result=result,salary=salary,bonus=bonus,taxes=taxes)
 
#app.run(host='localhost', port=5000)
