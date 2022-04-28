# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:17:15 2022

@author: bmadmin


#### Step 4: Create your API

In your `app.py` file, create a Flask API that contains:

- A route at `/` that accept:
  - `GET` request and return `"alive"` if the server is alive.
- A route at `/predict` that accept:
  - `POST` request that receives the data of a house in JSON format.
  - `GET` request returning a string to explain what the `POST` expect (data and format).
"""
import sys
sys.path.append("./predict")

from prediction import predictprice

from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/')
def alive():
    return render_template('alive.html')

@app.route('/input/')
def form():
    return render_template('input.html')
 
@app.route('/predict/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        message = "Please try to pass a json like :\
               json\
            {\
              \"data\": {\
                \"area\": int,\
                \"property-type\": \"APARTMENT\" | \"HOUSE\" | \"OTHERS\",\
                \"rooms-number\": int,\
                \"zip-code\": int,\
                    ...\
                    ...\
              }\
            }\
            "
        return message
    if request.method == 'POST':
        form_data = request.form
        '''
        a=[]
        try:
            area=float(form_data['area'])
        except:
            a.append('area')
             
        try:
            property_type=float(form_data['property_type'])
        except:
            a.append('property_type')
             
        try:
            rooms_number=float(form_data['rooms_number'])
        except:
            a.append('rooms_number')
        
        if a != []:
            return render_template('error.html',error = a)
        '''
    
        
        house_json={"data": {"area": 9000,"property-type": "APARTMENT" ,"rooms-number": 5}}
        
        
        prediction_price=predictprice(house_json)
        
        return render_template('predict.html',prediction_price=prediction_price,house_json=house_json)
 
#app.run(host='localhost', port=5000)
