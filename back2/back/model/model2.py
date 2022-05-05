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
    def __init__(self,datafile: str,train_size: int = 80, yname='classified.price'):
        self.datafile=datafile
        self.train_size=train_size
        self.yname=yname
        self.Xy=[]
        self.X_train,self.X_test, self.y_train, self.y_test = []
        
    def prepare(self):
        self.read_csv()
        self.split_data()
        
        
    def read_csv(self):
        self.Xy=pd.read_csv(self.datafile)
        
    def split_data(self):
        self.X=self.Xy.drop(column=self.yname)
        self.y=self.Xy[self.yname]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, random_state=self.random_state, train_size=self.train_size)
        #return X_train, X_test, y_train, y_test
        
    def balance_data(self):
        pass
    
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
        super.__init__(self,model, filename)
        self.model = model
        self.filename = filename
        self.mdl=[]
        
    def fit_model(self,InputData): #train the model
        self.mdl=self.model.fit(X_train,y_train)
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