# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:28:54 2022

@author: bmadmin
"""
import pandas as pd
import pickle

#from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

        
class Inputdata:
    def __init__(self,datafile: str):
        self.datafile=datafile
        self.yname='classified.price'
        self.Xy=[]
        self.X_train=[]
        self.X_test=[]
        self.y_train=[]
        self.y_test = []
        self.random_state = 42
        self.train_size = 0.80
    def prepare(self):
        self.read_csv()
        self.split_data()
        
        
    def read_csv(self):
        self.Xy=pd.read_csv(self.datafile)
        

        Xycol=['classified.building.constructionYear','classified.outdoor.garden.surface','classified.price']
        
        #df=df[['classified.zip','classified.price','classified.building.constructionYear']]
        self.Xy=self.Xy[Xycol]
        

        
    def split_data(self):
        #print("$$$$$$$$$$$$$$$$$$$$",self.Xy.columns)
        self.X=self.Xy.drop(columns=[self.yname])
        self.y=self.Xy[self.yname]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, random_state=self.random_state, train_size=self.train_size)
        #return X_train, X_test, y_train, y_test
        
    def balance_data(self):
        pass
    
class Defmodel:
    def __init__(self,filename: str,  model = []):
        #print("inDefModel",model,filename)
        self.model = model
        self.filename = filename
        
    def save(self):
        #print("111$$$###@@@",self.filename)
        pickle.dump(self.model, open(self.filename, 'wb'))
        #print("2222$$$###@@@",self.filename)
        
    def load(self):
        # Function : loads a model file
        # load the model from disk
        self.model = pickle.load(open(self.filename, 'rb'))
    def predict_model(self,X):
        #ypred=self.mdl.predict(X)
        ypred=self.model.predict(X)
        return ypred

class Model(Defmodel):
    def __init__(self, filename: str, model):
        #print("inModel")
        super().__init__(filename, model)
        self.model = model
        self.filename = filename
        #self.mdl=[]
        
        
    def fit_model(self,X_train,y_train): #train the model
        #print("5555@@@@@@@@@@@")
        #self.mdl=self.model.fit(X_train,y_train)
        self.model.fit(X_train,y_train)
        #print("66665555@@@@@@@@@@@")
    
    
    def predict_model(self,X):
        #ypred=self.mdl.predict(X)
        ypred=self.model.predict(X)
        return ypred
    
    def test_model():
        pass
    def visu_model():
        pass
