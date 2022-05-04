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
#from model import Defmodel
from model import Inputdata

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

@app.route('/customerview/',methods = ['POST', 'GET'])
def customerview():
    # Getting the current date and time
    #dt = datetime.now()
    # getting the timestamp
    #ts = datetime.timestamp(dt)
    print("$$$--",type(Model.model_storage),"---$$$")
    modellist=[]
    for mp in Model.model_storage:
        print("===###",mp,Model.model_storage[mp],"====###")
        modellist.append([mp,Model.model_storage[mp].filename])
    print("===###",modellist,"###===")
    
    for m in modellist:
        print(m,"@@",m[0],"@@",m[1])
    #Model.model_storage.append([mname,self])

    
    return render_template('customerview.html',modellist=modellist) 

@app.route('/customerview_select/',methods = ['POST', 'GET'])
def customerview_select():
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
        print("@@@@1@@",form_data,"@@1@@@")
        mp=form_data['models']
        actualmodel=Model.model_storage[mp]

    
    return render_template('predict.html') 

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


@app.route('/predict/', methods = ['POST', 'GET'])
def predict():

    return render_template('predict.html')
@app.route('/predict_show/', methods = ['POST', 'GET'])
def predict_show():
    global actualmodel
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        form_data = request.form
        print("we#@@@@@@@@@@@",form_data)

    

        gardensurface=form_data['gardensurface']
        constructionYear=form_data['constructionYear']
        house_json={"constructionYear": constructionYear,
                     "gardensurface":gardensurface}
               
        print("in predict_show")
        print("@@@@",house_json)
        X=[house_json['constructionYear'],house_json['gardensurface']]
        print("@@@@$$$$$$$$$$$$",X)
        #X=pd.DataFrame(X)
        #prediction_price=predictprice(actualmodel,house_json)
        #actualmodel=[]
        prediction_price=predictprice(actualmodel.model,house_json)
        print("afterpredict############",prediction_price)
        #prediction_price=actualmodel.predict_model(X)

        #print("############",prediction_price)
        #return render_template('predict.html',prediction_price=prediction_price,house_json=house_json)
        return render_template('predict_show.html',prediction_price=prediction_price,house_json=house_json)


 
@app.route('/predict_NOTUSED/', methods = ['POST', 'GET'])
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
    #NOT USED FOR NOW
    #scraper()
    #################
    print("past scraper")
    return render_template('main.html')   

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
    print("in create model")
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
        print("wesdfsdf#@@@@@@@@@@@",form_data['selected_model'])
        if selected_model == 'linearregression':

            print("w#####df#@@@@@@@@@@@",form_data['selected_model'])
            #createmodel(LinearRegression(),form_data['ratio'],form_data['balance'])
            now_model=Model(filename,LinearRegression())
            print("$$$$$$$$$$$$$$")
            now_model.fit_model(inpdata.X_train,inpdata.y_train)
            print("111$$$$$$$$$$$$$$")
            now_model.save()
            actualmodel=now_model
            
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
    global actualmodel
    print("in load_model")
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        print("load POST")
        form_data = request.form   # get model filename
        filename=form_data['myfile']
        filename="./model/savedmodels/"+filename
        print("filename @@@@@@@@@@@",filename," @@@@@@@@@@@@@")
        #createmodel(LinearRegression(),form_data['ratio'],form_data['balance'])
        now_model=Model(filename)
        print("load$$$$$$$$$$$$$$")
        now_model.load()
        actualmodel=now_model
        print("MODEL LOADED",filename)
    return render_template('main.html')

#######################################
# MAIN
#######################################

#clean_immodata("./data/data_homes.csv","./data/data_homes_cleaned.csv")
'''  
    if request.method == 'GET':
        pass
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
        #return message
'''

#app.run(host='localhost', port=5000)
