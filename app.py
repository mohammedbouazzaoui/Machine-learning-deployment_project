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
sys.path.append("./other")


from model import Model
#from model import Defmodel
from model import Inputdata
from myfunctions import debug

#NOT USED FOR NOW
#from webscraper import scraper
######################################
from prediction import predictprice
from cleaning_data import clean_immodata
#import pandas as pd
from flask import Flask,render_template,request
from datetime import datetime


from sklearn.linear_model import LinearRegression
global actualmodel




app = Flask(__name__)

DEBUG=True
        
@app.route('/predict/', methods = ['POST', 'GET'])
def predict():
    debug(DEBUG,"predict")
    global actualmodel
    
    columns=actualmodel.columns

    return render_template('predict.html',columns=columns)

@app.route('/predict_show/', methods = ['POST', 'GET'])
def predict_show():
    debug(DEBUG,"predict_show")
    global actualmodel
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        form_data = request.form
        house_json=dict(form_data)
        prediction_price=predictprice(actualmodel.model,house_json)
        return render_template('predict_show.html',prediction_price=prediction_price,house_json=house_json)


@app.route('/customerview/',methods = ['POST', 'GET'])
def customerview():
    debug(DEBUG,"customerview")
    # Getting the current date and time
    #dt = datetime.now()
    # getting the timestamp
    #ts = datetime.timestamp(dt)
    modellist=[]
    for mp in Model.model_storage:
        modellist.append([mp,Model.model_storage[mp].filename])

    return render_template('customerview.html',modellist=modellist) 

@app.route('/customerview_select/',methods = ['POST', 'GET'])
def customerview_select():
    debug(DEBUG,"customerview_select")
    global actualmodel
    # Getting the current date and time
    #dt = datetime.now()
    # getting the timestamp
    #ts = datetime.timestamp(dt)
    if request.method == 'GET':
        pass
        #message = "Please try to pass trough POST          "
        #return message
    if request.method == 'POST':
        form_data = request.form
        mp=form_data['models']
        actualmodel=Model.model_storage[mp]
        
    columns=actualmodel.columns

    return render_template('predict.html',columns=columns)
    #return render_template('predict.html') 
    #return render_template('customerview_select.html') 

@app.route('/',methods = ['POST', 'GET'])
def alive():
    # Getting the current date and time
    dt = datetime.now()
    # getting the timestamp
    ts = datetime.timestamp(dt)
    
    return render_template('checkserver.html',dt=dt,ts=ts)

@app.route('/main/',methods = ['POST', 'GET'])
def main():
    debug(DEBUG,"def main")
    global actualmodel
    if 'firstpass' not in locals():
        #load customer model
        actualmodel=Model('./model/savedmodels/linearregressionCUSTOMER.model')
        actualmodel.load()
        inpdata=Inputdata("./data/data_homes_cleaned.csv")
        inpdata.prepare()
        actualmodel.fit_model(inpdata.X_train,inpdata.y_train,inpdata.X_test,inpdata.y_test)
    
        firstpass=False
    
        
    if request.method == 'GET':
        pass
        #message = "Please try to pass trough POST          "
        #return message
    if request.method == 'POST':
        pass
    
    form_data = request.form
    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)

@app.route('/cleanup/', methods = ['POST', 'GET'])
def cleanup():
    #if request.method == 'GET':
    #    message = "Please try to pass trough main form            "
    #    return message
    #if request.method == 'POST':
    #    pass
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

    return render_template('cleanupinfo.html')


@app.route('/webscraper/', methods = ['POST', 'GET'])
def webscraper():
    return render_template('webscraper.html')
@app.route('/webscraper_run/', methods = ['POST', 'GET'])
def webscraperrun():
    #start scraper
    #NOT USED FOR NOW
    #scraper()
    #################
    print("past scraper")

    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)  

@app.route('/model_create/', methods = ['POST', 'GET'])
def model_create():
    #if request.method == 'GET':
    #    pass
    
    return render_template('model_create.html')

@app.route('/model_create_selected/', methods = ['POST', 'GET'])
def model_create_selected():
    global actualmodel
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
        filename="./model/savedmodels/"+selected_model+str(ts)+".model"

        if selected_model == 'linearregression':


            #createmodel(LinearRegression(),form_data['ratio'],form_data['balance'])
            now_model=Model(filename,LinearRegression())
            now_model.fit_model(inpdata.X_train,inpdata.y_train,inpdata.X_test,inpdata.y_test)
            now_model.save()
            actualmodel=now_model


    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)


@app.route('/model_load/', methods = ['POST', 'GET'])
def model_load():
 
    return render_template('model_load.html')

@app.route('/model_load_selected/', methods = ['POST', 'GET'])
def model_load_selected():
    global actualmodel

    if request.method == 'GET':
        pass
    
    if request.method == 'POST':

        form_data = request.form   # get model filename
        filename=form_data['myfile']
        filename="./model/savedmodels/"+filename

        now_model=Model(filename)
        now_model.load()
        actualmodel=now_model


    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)

#######################################
# MAIN
#######################################

debug(DEBUG,"before main")
main
debug(DEBUG,"after main")
app.run(host='localhost', port=5000)
