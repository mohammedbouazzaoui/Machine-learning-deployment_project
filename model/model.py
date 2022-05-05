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
        self.X=[]
        self.y=[]
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

    def split_data(self):

        self.X=self.Xy.drop(columns=[self.yname])
        self.y=self.Xy[self.yname]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, random_state=self.random_state, train_size=self.train_size)

        
    def balance_data(self):
        pass
    
class Model():
    model_storage={}   
    def __init__(self, filename: str, model = []):
        self.model = model
        self.filename = filename
        self.regressor=[]
        self.accuracy_score =[]
        mname="model"+str(len(Model.model_storage))
        Model.model_storage[mname]=self
        self.columns=[]
        
    def fit_model(self,X_train,y_train,X_test,y_test): #train the model
        self.regressor=self.model.fit(X_train,y_train)
        self.accuracy_score=self.regressor.score(X_test,y_test)
        self.columns=X_train.columns
        print("66665555@@",self.accuracy_score,"@@@@@@@@@")
    
    def save(self):
        pickle.dump(self.model, open(self.filename, 'wb'))
        
    def load(self):
        # Function : loads a model file
        # load the model from disk
        self.model = pickle.load(open(self.filename, 'rb'))
        
    def predict_model(self,X):
        ypred=self.model.predict(X)
        return ypred       
        
    def test_model():
        pass
    def visu_model():
        pass   

