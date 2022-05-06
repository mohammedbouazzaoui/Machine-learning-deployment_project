# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:17:15 2022

@author: bmadmin

"""

from predict.prediction import predictprice
from preprocessing.cleaning_data import clean_immodata
from flask import Flask,render_template,request
from datetime import datetime
from sklearn.linear_model import LinearRegression

#from webscraper import scraper
from model.model import Model
from model.model import Inputdata
from other.myfunctions import debug

global actualmodel

app = Flask(__name__)

DEBUG=False
        
@app.route('/predict/', methods = ['POST', 'GET'])
def predict():
    global actualmodel
    
    debug(DEBUG,"predict")
    columns=actualmodel.columns

    return render_template('predict.html',columns=columns)

@app.route('/predict_show/', methods = ['POST', 'GET'])
def predict_show():
    global actualmodel
    
    debug(DEBUG,"predict_show")
    if request.method == 'POST':
        debug(DEBUG,"in request.method") 
        form_data = request.form
        house_json=dict(form_data)
        debug(DEBUG,house_json)
        prediction_price=predictprice(actualmodel.model,house_json)
        prediction_price = '{0:g}'.format(prediction_price[0]) + " \N{euro sign}"
  
        return render_template('predict_show.html',prediction_price=prediction_price,house_json=house_json)


@app.route('/customerview/',methods = ['POST', 'GET'])
def customerview():
    debug(DEBUG,"customerview")

    modellist=[]
    for mp in Model.model_storage:
        modellist.append([mp,Model.model_storage[mp].filename])

    return render_template('customerview.html',modellist=modellist) 

@app.route('/customerview_select/',methods = ['POST', 'GET'])
def customerview_select():
    debug(DEBUG,"customerview_select")
    global actualmodel

    if request.method == 'POST':
        form_data = request.form
        mp=form_data['models']
        actualmodel=Model.model_storage[mp]
        
    columns=actualmodel.columns

    return render_template('predict.html',columns=columns)

@app.route('/cleanup/', methods = ['POST', 'GET'])
def cleanup():
    
    clean_immodata("./data/data_homes.csv","./data/data_homes_cleaned.csv")
    return render_template('cleanupinfo.html')

@app.route('/cleanupinfo/', methods = ['POST', 'GET'])
def cleanupinfo():

    if request.method == 'POST':
        pass

    return render_template('cleanupinfo.html')

@app.route('/webscraper/', methods = ['POST', 'GET'])
def webscraper():
    
    return render_template('webscraper.html')

@app.route('/webscraper_run/', methods = ['POST', 'GET'])
def webscraperrun():

    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)  

@app.route('/model_create/', methods = ['POST', 'GET'])
def model_create():

    return render_template('model_create.html')

@app.route('/model_create_selected/', methods = ['POST', 'GET'])
def model_create_selected():
    global actualmodel
    
    inpdata=Inputdata("./data/data_homes_cleaned.csv")
    inpdata.prepare()

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

@app.route('/main/',methods = ['POST','GET'])
def main():
    global actualmodel
    global firstpass
    
    debug(DEBUG,"def main")
    if firstpass:
        debug(DEBUG,"main firstpass")
        #load customer model
        actualmodel=Model('./model/savedmodels/linearregressionCUSTOMER.model')
        actualmodel.load()
        inpdata=Inputdata("./data/data_homes_cleaned.csv")
        inpdata.prepare()
        actualmodel.fit_model(inpdata.X_train,inpdata.y_train,inpdata.X_test,inpdata.y_test)
    
        firstpass=False
    
    info=actualmodel.filename
    score=actualmodel.accuracy_score
    return render_template('main.html',info=info,score=score)
    
@app.route('/',methods = ['POST', 'GET'])
def checkserver():
    # Getting the current date and time
    dt = datetime.now()
    # getting the timestamp
    ts = datetime.timestamp(dt)
    
    return render_template('checkserver.html',dt=dt,ts=ts)   
    
#######################################
# MAIN
#######################################

debug(DEBUG,"before main")
global firstpass
firstpass=True
debug(DEBUG,"after main")


#app.run(host='localhost', port=5000)
