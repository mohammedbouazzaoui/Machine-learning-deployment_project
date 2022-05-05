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

def train(house_json):
        
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    
    # read data
    #
    df = pd.read_csv("./data/data_homes_cleaned.csv")
    
    
    Xcol=['classified.building.constructionYear','classified.outdoor.garden.surface']
    ycol=['classified.price']
    Xycol=['classified.building.constructionYear','classified.outdoor.garden.surface','classified.price']
    
    #df=df[['classified.zip','classified.price','classified.building.constructionYear']]
    df=df[Xycol]
    
    # prepare
    # finalclean
    #df['classified.building.constructionYear']=df['classified.building.constructionYear'][df['classified.building.constructionYear'] == 'None'].replace('None',np.nan)
    #df=df.dropna()
    df=df[df['classified.building.constructionYear'] != 'None']
    #
    #X=df[['classified.zip','classified.building.constructionYear']]
    #y=df[['classified.price']]
    X=df[Xcol]
    y=df[ycol]
    #print(X,y)
    '''
    # How to use `sklearn` now with multiple features ? Well, it's simple, you don't change anything. `sklearn` takes care of everything for you.
    
    1. Import `LinearRegression` from `sklearn`
    2. Create a `regressor` variable and instantiate your `LinearRegression` class.
    3. Train your model with `X_train` and `y_train`.
    4. Display the score of your model with `X_train` and `y_train`.
    5. Use the predict method of your model on your test dataset (`X_test`).
    6. Display the score of your model with `X_test` and `y_test`.
    '''
    #print(X)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=33, train_size=0.8)
    
    from sklearn.linear_model import LinearRegression
    #X_train=X_train.reshape(-1, 1)
    #y_train=y_train.reshape(-1, 1)
    regressor=LinearRegression().fit(X_train,y_train)
    
    print("regressor score:",regressor.score(X_train, y_train))
    
    
    ypred=regressor.predict(X_test)
    #X_test
    #ypred
    
    
    plt.scatter(X_test['classified.outdoor.garden.surface'], ypred,color='green')
    #plt.scatter(X_test['classified.building.constructionYear'], ypred,color='blue')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')

    return(ypred)


def predictprice2(house_json):
    '''
      house_json={"data": 
                  {"constructionYear": constructionYear,
                   "gardensurface":gardensurface}
                  }
    '''
    result=train(house_json)
    print("@@@@@@@@@@@@@@",result)
    return result

def predictprice(model,house_json):
    print("in predictprice",house_json)
    '''
      house_json={"constructionYear": constructionYear,
                   "gardensurface":gardensurface}
                
    '''
         
    #Xcol=['classified.building.constructionYear','classified.outdoor.garden.surface']
    #ycol=['classified.price']
    #Xcol=house_json.keys()
    #ycol=house_json.values()
    #Xycol=['classified.building.constructionYear','classified.outdoor.garden.surface','classified.price']
    
    #df=df[['classified.zip','classified.price','classified.building.constructionYear']]
    #df=df[Xycol]
    
    # prepare
    # finalclean
    #df['classified.building.constructionYear']=df['classified.building.constructionYear'][df['classified.building.constructionYear'] == 'None'].replace('None',np.nan)
    #df=df.dropna()
    #df=df[df['classified.building.constructionYear'] != 'None']
    #
    #X=df[['classified.zip','classified.building.constructionYear']]
    #y=df[['classified.price']]
    #data = {'Name':['Tom', 'nick', 'krish', 'jack'],
    #    'Age':[20, 21, 19, 18]}
    #df2 = pd.DataFrame(data, index =['first', 'second'],
      #             columns =['a', 'b1'])
    # Create DataFrame
    #df = pd.DataFrame(data)
    
    
    #X=df[Xcol]
    #y=df[ycol]
    #print(X,y)   
    #Xcol=['classified.building.constructionYear','classified.outdoor.garden.surface']
    #ycol=['classified.price']
    #Xycol=['classified.building.constructionYear','classified.outdoor.garden.surface','classified.price']
    #data=[house_json['constructionYear'],house_json['gardensurface']]
    #print("###@@@$$$",data,Xcol)
    #X=pd.DataFrame([data],columns=Xcol)
    X=pd.DataFrame([house_json])
    print("before predict@@@@@X@@@@",X)
    result=model.predict(X)

    print("afterpredict@@@@@@@@@@@@@@",result)
    return result