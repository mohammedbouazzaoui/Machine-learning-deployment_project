# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:28:54 2022

@author: bmadmin
"""
import pandas as pd
import pickle

#from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
        
        
class Inputdata:
    columns=[]
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
        Inputdata.columns=self.Xy.columns

    def split_data_prev(self):

        self.X=self.Xy.drop(columns=[self.yname])
        self.y=self.Xy[self.yname]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, random_state=self.random_state, train_size=self.train_size)

    def split_data(self):

        self.X=self.Xy.drop(columns=[self.yname])
        self.y=self.Xy[self.yname]

        self.X, self.y = make_classification(random_state=42)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, random_state=self.random_state)

        #X, y = make_classification(random_state=42)
        #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        
    def balance_data(self):
        pass
    
class Model2():
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
        self.columns=Inputdata.columns
        print("66665555@@",self.accuracy_score,"@@@@@@@@@")

        # prepare
        from sklearn.datasets import make_classification
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        
        #X, y = make_classification(random_state=42)
        #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        #pipe = make_pipeline(StandardScaler(), LogisticRegression())
        #pipe.fit(X_train, y_train)  # apply scaling on training dataPipeline(steps=[('standardscaler', StandardScaler()), ('logisticregression', LogisticRegression())])
        #pipe.score(X_test, y_test) 

    
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