# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:28:54 2022

@author: bmadmin
"""
import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



        
class Inputdata:
    def __init(self,Xy,yname='y',random_state=42,train_size=0.8):
        self.Xy=Xy
        self.yname=yname
        self.random_state=random_state
        self.train_size=train_size
        
    def balance_data(self):
        pass
    def read_csv(self,datafile,delim=','):
        self.Xy=pd.read_csv(datafile,delimiter=delim)
        
    def split_data(self):
        X=self.Xy.drop(column=self.yname)
        y=self.Xy[self.yname]

        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=self.random_state, train_size=self.train_size)

        return X_train, X_test, y_train, y_test
        
    
    
class Defmodel:
    def __init__(self, model, filename: str):
        self.model = model
        self.filename = filename
        
    def save(self):
        pickle.dump(self.model, open(self.filename, 'wb'))
    
    def load(self):
        # Function : loads a model file
        # load the model from disk
        self.model = pickle.load(open(self.filename, 'rb'))


class Model(Defmodel):
    def __init__(self, model, filename: str = "./model/savedmodels/dummymodel.model"):
        super.__init__(model, filename)
        self.model = model
        self.filename = filename
        self.mdl=[]
        
    def fit(self): #train the model
        self.mdl=model.fit(X_train,y_train)
        pass
    
    def predict_model(self,X):
        ypred=self.mdl.predict(X)
        return ypred
    
    def test_model():
        pass
    def visu_model():
        pass
    
myregmodel = Model(LinearRegression(),"./model/savedmodels/firstmodel.model")
myregmodel.fit()
myregmodel.save()
myregmodel.load()
#Main
model = LogisticRegression()
X_train=[],X_test=[]
y_train=[], y_test=[]

#save_model("logisticregression.model",model,X_train,y_train)
#model=load_model("logisticregression.model")
#predict_model(model,X_test,y_test)