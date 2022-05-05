# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:13:08 2022

@author: bmadmin


#### Step 2: Preprocessing pipeline

This python module will contain all the code to preprocess your data. 
Make sure to think about what will be the format of your data to fit 
the model.
Also, be sure to know which information HAVE to be there and which one
 can be empty (NAN).

In the `preprocessing/` folder:

- Create the `cleaning_data.py` file that will contain all the code that 
will be used to preprocess the data you will receive to predict a new price. 
(fill the NaN values, handle text data, etc...).
- This file should contain a function called `preprocess()` that will take a 
new house's data as input and return those data preprocessed as output.
- If your data doesn't contain the required information, you should return an 
error to the user.
"""
import sys
sys.path.append(".")
sys.path.append("./predict")
sys.path.append("./preprocessing")
sys.path.append("./model")
sys.path.append("./other")

from myfunctions import debug

import pandas as pd
import numpy as np

DEBUG=True

def clean_immodata(inputfile:str = "../data/data_homes.csv",cleaned_file:str = "../data/data_homes_cleaned.csv"):
    debug(DEBUG,"clean_immodata")

    #
    # function : will clean the immoweb data containing all the houses
    #
    # input: file with immoweb data
    # output: clean data
    #

    df=pd.read_csv(inputfile,delimiter=",")
    
    
    # Cleaning steps
    ################
    # Checking how many rows of each attribute are NaN
    df.isna().sum()
    
    # drop columns
    dropcolmns=['classified.type','classified.condition.isNewlyBuilt','classified.transactionType','customer.id','classified.visualisationOption','classified.id','screen.language','screen.name','customer.networkInfo.id','customer.networkInfo.name',\
                'customer.groupInfo.name','customer.groupInfo.id','user.loginStatus',\
                'Unnamed: 0','user.personal.language','user.id',\
                'customer.name','customer.family']
    df = df.drop(columns=dropcolmns)
    df.isna().sum()
    print(df.shape)
    #drop duplicates
    df=df.drop_duplicates()
    print(df.shape)
    df.head()
    
    # drop "fromprice - toprice" these are 'housegroups'
    df=df[df['classified.price'].str.find('-') == -1]
    # drop bad rows
    df=df[df['classified.kitchen.type'] != 'classified.kitchen.type']
    df=df[df['classified.building.condition'] != 'classified.building.condition']
    df=df[df['classified.price'] != 'no price']
    
    # get ordinals and categoricals
    for i in df.columns:
        if len(df[i].unique()) < 100 :
            print(i,": ",len(df[i].unique()),df[i].unique())
            
    # transformm ordinals and categoricals        
    #categoricals
    #############
    #classified.type :  4 ['house' 'classified.type' 'apartment' nan]
    #classified.subtype :  22 ['apartment block' 'classified.subtype' 'apartment' 'bungalow' 'castle'
                # 'chalet' 'country cottage' 'duplex' 'exceptional property' 'farmhouse'
                # 'flat studio' 'ground floor' 'house' 'villa' 'mixed use building'
                # 'town house' 'mansion' 'manor house' 'other property' nan
                # 'classified details' 'penthouse']
    #classified.type :  8 ['house' 'en' 'classified.type' 'apartment' nan 'apartment group' 'en;;' 'house group']
    #classified.energy.heatingType :  8 ['gas' nan 'fueloil' 'electric' 'classified.energy.heatingType' 'pellet'
    # 'wood' 'carbon']
    #other type
    ################
    #classified.kitchen.type :  10 ['semi equipped' 'installed' nan 'usa installed' 'hyper equipped'
    # 'not installed' 'usa hyper equipped' 'classified.kitchen.type'
    # 'usa semi equipped' 'usa uninstalled']
    #classified.building.condition :  8 ['to be done up' 'as new' 'to renovate' 'good' nan
    # 'classified.building.condition' 'just renovated' 'to restore']
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('not installed' ,1)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('installed' ,2)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('semi equipped' ,3)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('hyper equipped' ,4)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('usa uninstalled' ,1)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('usa installed' ,2)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('usa semi equipped' ,3)
    df['classified.kitchen.type'] = df['classified.kitchen.type'].replace('usa hyper equipped' ,4)
    
    df['classified.building.condition'] = df['classified.building.condition'].replace('to renovate',1)
    df['classified.building.condition'] = df['classified.building.condition'].replace('to restore',2)
    df['classified.building.condition'] = df['classified.building.condition'].replace('to be done up',3)
    df['classified.building.condition'] = df['classified.building.condition'].replace('good',5)
    df['classified.building.condition'] = df['classified.building.condition'].replace('just renovated',6)
    df['classified.building.condition'] = df['classified.building.condition'].replace('as new',7)
    
    
    
    # set 0
    ################
    #----------- replace nan/None
    flds=[
          "classified.outdoor.garden.surface",
          "classified.parking.parkingSpaceCount.indoor",
          "classified.parking.parkingSpaceCount.outdoor",
          "classified.bedroom.count"
         ]
    for fld in flds:
        df[fld]=df[fld].replace(np.nan, 0)
        df[fld]=df[fld].replace('None', 0)
    
    #----------- replace nan,False,True
    flds=[
          "classified.atticExists",
          "classified.basementExists",
          "classified.outdoor.terrace.exists",
          "classified.specificities.SME.office.exists",
          "classified.wellnessEquipment.hasSwimmingPool"
            ]
    for fld in flds:
        df[fld]=df[fld].replace(np.nan, 0)
        df[fld]=df[fld].replace('false', 0)
        df[fld]=df[fld].replace('true', 1)
    print(df.columns)    
    
    print('###########################################################')
    # get the nan field of a column
    #df[df['classified.land.surface'].isna() == True]
    #df['classified.land.surface']=df['classified.land.surface'].replace(np.nan,9999)
        
    
    
    # drop all rows with nan
    df=df.dropna()
    
    # change type
    df['classified.price'] = df['classified.price'].astype(np.float)
    df['classified.building.constructionYear'] = df['classified.building.constructionYear'].astype(np.float)
    df['classified.certificates.primaryEnergyConsumptionLevel'] = df['classified.certificates.primaryEnergyConsumptionLevel'].astype(np.float)
    df['classified.bedroom.count'] = df['classified.bedroom.count'].astype(np.int64)
    df['classified.land.surface'] = df['classified.land.surface'].astype(np.float)
    df['classified.outdoor.garden.surface'] = df['classified.outdoor.garden.surface'].astype(np.float)
    df['classified.parking.parkingSpaceCount.indoor'] = df['classified.parking.parkingSpaceCount.indoor'].astype(np.int64)
    df['classified.parking.parkingSpaceCount.outdoor'] = df['classified.parking.parkingSpaceCount.outdoor'].astype(np.int64)
    
    dum=pd.get_dummies(df['classified.energy.heatingType'])
    df=df.join(dum)
    df=df.drop(columns=['classified.energy.heatingType'])
    #
    df=df.drop(columns=['classified.subtype'])
    #
    ########################################################
    # leave only needed columns
    ########################################################
    #
    '''
    # all available fields:
    Index(['classified.price', 'classified.kitchen.type',
       'classified.building.constructionYear', 'classified.building.condition',
       'classified.certificates.primaryEnergyConsumptionLevel',
       'classified.bedroom.count', 'classified.land.surface',
       'classified.atticExists', 'classified.basementExists',
       'classified.outdoor.garden.surface',
       'classified.outdoor.terrace.exists',
       'classified.specificities.SME.office.exists',
       'classified.wellnessEquipment.hasSwimmingPool',
       'classified.parking.parkingSpaceCount.indoor',
       'classified.parking.parkingSpaceCount.outdoor', 'carbon', 'electric',
       'fueloil', 'gas', 'pellet', 'wood'],
      dtype='object')
    '''
    select_columns=['classified.price','classified.building.constructionYear', 'classified.building.condition',
       'classified.certificates.primaryEnergyConsumptionLevel',
       'classified.bedroom.count', 'classified.land.surface',
       'classified.outdoor.garden.surface']
    df=df[select_columns]
    #
    # Save cleaned data for model
    df.to_csv(cleaned_file,index=False)
    #df.to_csv("../data/data_homes_cleaned.csv",index=False)

#print("TESTINGG####")
#clean_immodata("../data/data_homes.csv","../data/data_homes_cleaned.csv")
