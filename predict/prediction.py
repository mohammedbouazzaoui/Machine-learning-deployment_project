# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:15:43 2022

@author: bmadmin



#### Step 3: Fit your data

Fit your data to your model.

In the `predict/` folder:

- Create the `prediction.py` file that will contain all the code used to predict a new house's price.
- Your file should contain a function `train()` that will create and store the model and a function `predict()` that will take your preprocessed data as an input and return a price as output using your stored model.
"""
import pandas as pd

def trainNOTUSED(house_json):
        
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    
    # read data
    #
    df = pd.read_csv("./data/data_homes_cleaned.csv")
    
    
    Xcol=['classified.building.constructionYear','classified.outdoor.garden.surface']
    ycol=['classified.price']
    Xycol=['classified.building.constructionYear','classified.outdoor.garden.surface','classified.price']
    
    df=df[Xycol]
    
    # prepare
    # finalclean
    #??????????????????????????????????????
    df=df[df['classified.building.constructionYear'] != 'None']
    #
    X=df[Xcol]
    y=df[ycol]


    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=33, train_size=0.8)
    
    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression().fit(X_train,y_train)
    
    ypred=regressor.predict(X_test)
    
    plt.scatter(X_test['classified.outdoor.garden.surface'], ypred,color='green')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')

    return(ypred)


def predictprice(model,house_json):

    X=pd.DataFrame([house_json])

    result=model.predict(X)

    return result