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
sys.path.append(".")
sys.path.append("./predict")
sys.path.append("./preprocessing")
sys.path.append("./model")


from model import Model
from model import Defmodel
from model import Inputdata

from webscraper import scraper
from prediction import predictprice
from cleaning_data import clean_immodata
import pandas as pd
from flask import Flask,render_template,request
from datetime import datetime


from sklearn.linear_model import LinearRegression


app = Flask(__name__)
 
@app.route('/',methods = ['POST', 'GET'])
def alive():
    # Getting the current date and time
    dt = datetime.now()
    # getting the timestamp
    ts = datetime.timestamp(dt)
    
    return render_template('alive.html',dt=dt,ts=ts)

@app.route('/main/',methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        pass
        #message = "Please try to pass trough POST          "
        #return message
    if request.method == 'POST':
        pass
    
    form_data = request.form
    print(form_data)
    return render_template('main.html')

@app.route('/cleanup/', methods = ['POST', 'GET'])
def cleanup():
    #if request.method == 'GET':
    #    message = "Please try to pass trough main form            "
    #    return message
    #if request.method == 'POST':
    #    pass
        #form_data = request.form
        #print("we#@@@@@@@@@@@",form_data)
        #print("***********")
    #present some info about cleaning
    #run cleaning
    clean_immodata("./data/data_homes.csv","./data/data_homes_cleaned.csv")
    return render_template('cleanupinfo.html')

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
    #HERE INFO ON CLEANUP !!!!!!!!!!!!!!!!
    #present some info about cleaning
    #run cleaning
    #clean_immodata2("./data/data_homes.csv","./data/data_homes_cleaned.csv")
    
    #print("@@@@@@@22@@@@@@@@@@")
    #return f
    return render_template('cleanupinfo.html')

@app.route('/input/', methods = ['POST', 'GET'])
def inputform():
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

@app.route('/webscraper/', methods = ['POST', 'GET'])
def webscraper():
    return render_template('webscraper.html')
@app.route('/webscraper_run/', methods = ['POST', 'GET'])
def webscraperrun():
    #start scraper
    scraper()
    print("past scraper")
    return render_template('main.html')   

@app.route('/model_create/', methods = ['POST', 'GET'])
def model_create():
    #if request.method == 'GET':
    #    pass
    
    return render_template('model_create.html')

@app.route('/model_create_selected/', methods = ['POST', 'GET'])
def model_create_selected():
    inpdata=Inputdata("./data/data_homes_cleaned.csv")
    inpdata.prepare()
    
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':

        # Getting the current date and time
        dt = datetime.now()
        # getting the timestamp
        ts = datetime.timestamp(dt)
        #
        form_data = request.form
        selected_model=form_data['selected_model']
        filename="./model/savedmodels/"+selected_model+str(ts)
        print("wesdfsdf#@@@@@@@@@@@",form_data['selected_model'])
        if selected_model == 'linearregression':

            print("w#####df#@@@@@@@@@@@",form_data['selected_model'])
            #createmodel(LinearRegression(),form_data['ratio'],form_data['balance'])
            now_model=Model(LinearRegression(),filename)
            print("$$$$$$$$$$$$$$")
            now_model.fit_model(inpdata.X_train,inpdata.y_train)
            print("111$$$$$$$$$$$$$$")
            now_model.save()
            print("222$$$$$$$$$$$$$$")
        #return render_template('main.html')

        #model()
    #print("past model")
    return render_template('main.html')




@app.route('/model_load/', methods = ['POST', 'GET'])
def model_load():
 
    return render_template('model_load.html')

@app.route('/model_load_selected/', methods = ['POST', 'GET'])
def model_load_selected():
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        form_data = request.form
        #print("wesdfsdf#@@@@@@@@@@@",form_data['selected_model'])
        
        #loadmodel(form_data['selected_model'],form_data['ratio'],form_data['balance'])
     
        #return render_template('main.html')

        #model()
    #print("past model")
    return render_template('main.html')

#######################################
# MAIN
#######################################
#clean_immodata("./data/data_homes.csv","./data/data_homes_cleaned.csv")


app.run(host='localhost', port=5000)
