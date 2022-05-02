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

def createmainform():
    dr="./templates/"
    f="mainformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    
    fp=open(dr+f,"w")
    fp.write("<form action=\"/cleanup/\" method = \"POST\">\n")
    line="<p>    PRESS TO CLEANUP SCRAPED DATA</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f

def createinputform():
    dr="./templates/"
    f="inputformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    flds=[("constructionYear","Construction Year"),
          ("gardensurface", "Garden Surface")
          ]
    fp=open(dr+f,"w")
    fp.write("<form action=\"/predict/\" method = \"POST\">\n")
    for fld in flds:
        #print(fld[0],fld[1])
        line="<p>"+fld[1]+" <input type = \"text\" name = \""+fld[0]+"\" /></p>\n"
        fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f

def createcleanupform():
    dr="./templates/"
    f="cleanupformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    
    fp=open(dr+f,"w")
    fp.write("<form action=\"/cleanupinfo/\" method = \"POST\">\n")
    line="<p>    PRESS TO CLEANUP SCRAPED DATA</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f
def createcleanupinfoform():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    dr="./templates/"
    f="cleanupinfoformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    fp=open(dr+f,"w")
    fp.write("<form action=\"/input/\" method = \"POST\">\n")
    line="<p>    PRESENT INFO ABOUT CLEANING press to go to input form</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    return f

app = Flask(__name__)
 
@app.route('/')
def alive():
    return render_template('alive.html')

@app.route('/cleanup/')
def cleanup():
    return render_template(createcleanupform())

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
    return render_template(createcleanupinfoform())

@app.route('/input/', methods = ['POST', 'GET'])
def form():
    return render_template(createinputform())
 
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
