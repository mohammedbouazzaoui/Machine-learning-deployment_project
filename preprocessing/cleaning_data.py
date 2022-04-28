# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:13:08 2022

@author: bmadmin


#### Step 2: Preprocessing pipeline

This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model.
Also, be sure to know which information HAVE to be there and which one can be empty (NAN).

In the `preprocessing/` folder:

- Create the `cleaning_data.py` file that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, etc...).
- This file should contain a function called `preprocess()` that will take a new house's data as input and return those data preprocessed as output.
- If your data doesn't contain the required information, you should return an error to the user.
"""

import pandas as pd
inputfile = "../data/data_homes.csv"
df=pd.read_csv(inputfile,delimiter=";")


# Cleaning steps
# remove unnecessary columns
keep= ["classified.type","classified.subtype","classified.price","classified.transactionType","classified.zip","classified.kitchen.type","classified.building.constructionYear","classified.building.condition","classified.energy.heatingType","classified.certificates.primaryEnergyConsumptionLevel","classified.bedroom.count","classified.land.surface","classified.atticExists","classified.basementExists","classified.outdoor.garden.surface","classified.outdoor.terrace.exists","classified.specificities.SME.office.exists","classified.wellnessEquipment.hasSwimmingPool","classified.parking.parkingSpaceCount.indoor","classified.parking.parkingSpaceCount.outdoor","classified.condition.isNewlyBuilt","customer.name","customer.family"]
df=df[keep]


# 
# drop "fromprice - toprice"
df=df[df['classified.price'].str.find('-') == -1]

#just to be sure

df['classified.price'] = df['classified.price'].astype(float)


# reformat categorical features
 
#
# Save cleaned data for model
df.to_csv("../data/data_homes_cleaned.csv",index=False)
