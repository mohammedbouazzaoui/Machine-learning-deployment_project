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
sys.path.append("./preprocessing")


from prediction import predictprice
from cleaning_data2 import clean_immodata2
import pandas as pd
from flask import Flask,render_template,request


app = Flask(__name__)
 
@app.route('/')
def alive():
    return render_template('alive.html')

@app.route('/main/',methods = ['POST', 'GET'])
def main2():
    if request.method == 'GET':
        message = "Please try to pass trough POST          "
        return message
    if request.method == 'POST':
        pass
    
    form_data = request.form
    print(form_data)
    return render_template('mainform.html')

@app.route('/cleanup/')
def cleanup():
    return render_template('cleanupform.html')

@app.route('/cleanupinfo/', methods = ['POST', 'GET'])
def cleanupinfo():
    if request.method == 'GET':
        message = "Please try to pass trough main form            "
        return message
    if request.method == 'POST':
        pass
        #form_data = request.form
        #print("we#@@@@@@@@@@@",form_data)
        #print("***********")
    #present some info about cleaning
    #run cleaning
    clean_immodata2("./data/data_homes.csv","./data/data_homes_cleaned.csv")
    
    #print("@@@@@@@22@@@@@@@@@@")
    #return f
    return render_template('cleanupinfoform.html')

@app.route('/input/', methods = ['POST', 'GET'])
def form():
    return render_template('inputform.html')
 
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
        #print("we#@@@@@@@@@@@",form_data)

    

        gardensurface=form_data['gardensurface']
        constructionYear=form_data['constructionYear']
        house_json={"data": 
                    {"constructionYear": constructionYear,
                     "gardensurface":gardensurface}
                    }
        
        
        prediction_price=predictprice(house_json)
        #print("############",prediction_price)
        return render_template('predict.html',prediction_price=prediction_price,house_json=house_json)

    
#######################################
# MAIN
#######################################
#clean_immodata("./data/data_homes.csv","./data/data_homes_cleaned.csv")

app.run(host='localhost', port=5000)
