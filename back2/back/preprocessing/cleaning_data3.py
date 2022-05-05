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

import numpy as np
import pandas as pd
inputfile = "../data/data_homes.csv"
#inputfile = "C:/Users/bmadmin/Desktop/Octocat/mohammedbouazzaoui/challenge-machine-learning-api-deployment/data/data_homes.csv"
# some abstraction
DELIMITER=","

fields={"housetype"	:	"classified.type",
"subtype"	:	"classified.subtype",
"price"	:	"classified.price",
"transactionType"	:	"classified.transactionType",
"zipcode"	:	"classified.zip",
"kitchen"	:	"classified.kitchen.type",
"constructionYear"	:	"classified.building.constructionYear",
"buildingcondition"	:	"classified.building.condition",
"conditionheatingType"	:	"classified.energy.heatingType",
"EnergyConsumptionLevel"	:	"classified.certificates.primaryEnergyConsumptionLevel",
"bedroomcount"	:	"classified.bedroom.count",
"landsurface"	:	"classified.land.surface",
"atticExists"	:	"classified.atticExists",
"basementExists"	:	"classified.basementExists",
"gardensurface"	:	"classified.outdoor.garden.surface",
"terraceexists"	:	"classified.outdoor.terrace.exists",
"SMEofficeexists"	:	"classified.specificities.SME.office.exists",
"hasSwimmingPool"	:	"classified.wellnessEquipment.hasSwimmingPool",
"parkingSpaceCountindoor"	:	"classified.parking.parkingSpaceCount.indoor",
"parkingSpaceCountoutdoor"	:	"classified.parking.parkingSpaceCount.outdoor",
"conditionNew"	:	"classified.condition.isNewlyBuilt",
"customername"	:	"customer.name",
"customerfamily"	:	"customer.family"
}


    
  
dfraw=pd.read_csv(inputfile)


# Cleaning steps
# remove unnecessary columns
#	user.loginStatus	user.id	user.personal.language	classified.id	classified.type	classified.subtype	classified.price	classified.transactionType	classified.zip	classified.visualisationOption	classified.kitchen.type	classified.building.constructionYear	classified.building.condition	classified.energy.heatingType	classified.certificates.primaryEnergyConsumptionLevel	classified.bedroom.count	classified.land.surface	classified.atticExists	classified.basementExists	classified.outdoor.garden.surface	classified.outdoor.terrace.exists	classified.specificities.SME.office.exists	classified.wellnessEquipment.hasSwimmingPool	classified.parking.parkingSpaceCount.indoor	classified.parking.parkingSpaceCount.outdoor	classified.condition.isNewlyBuilt	customer.id	customer.name	customer.family	customer.groupInfo.id	customer.groupInfo.name	customer.networkInfo.id	customer.networkInfo.name	screen.name	screen.language

#keep= ["classified.type","classified.subtype","classified.price","classified.transactionType","classified.zip","classified.kitchen.type","classified.building.constructionYear","classified.building.condition","classified.energy.heatingType","classified.certificates.primaryEnergyConsumptionLevel","classified.bedroom.count","classified.land.surface","classified.atticExists","classified.basementExists","classified.outdoor.garden.surface","classified.outdoor.terrace.exists","classified.specificities.SME.office.exists","classified.wellnessEquipment.hasSwimmingPool","classified.parking.parkingSpaceCount.indoor","classified.parking.parkingSpaceCount.outdoor","classified.condition.isNewlyBuilt","customer.name","customer.family"]

#keep selected fields
keep=list(fields.values())

df=dfraw[keep]


# DROP ROWS
# drop "fromprice - toprice" these are 'housegroups'
df=df[df[fields['price']].str.find('-') == -1]



# FILL/TRANSFORM
################
#----------- replace nan
flds=[fields["price"],
      fields["gardensurface"],
      fields["parkingSpaceCountindoor"],
      fields["parkingSpaceCountoutdoor"],
      fields["bedroomcount"]]
for fld in flds:
    df[fld]=df[fld].replace(np.nan, 0)

flds=[ 
      fields["gardensurface"]
       ]
for fld in flds:
    df[fld]=df[fld].replace('None', 0)
#----------- replace 'no price'
flds=[fields["price"]]
for fld in flds:
    df[fld]=df[fld].replace('no price', 0)
    
#----------- replace nan,False,True
flds=[fields["atticExists"],
      fields["basementExists"],
      fields["terraceexists"],
      fields["SMEofficeexists"],
      fields["hasSwimmingPool"],
      fields["conditionNew"]]
for fld in flds:
    df[fld]=df[fld].replace(np.nan, 0)
    df[fld]=df[fld].replace(False, 0)
    df[fld]=df[fld].replace(True, 1)


# CALCULATED VALUES
###################
# maybe later replace by mean value of city now by mean_all
#MEANGARDEN=df[fields['gardensurface']].mean()
MEANGARDEN=50
flds=[fields["gardensurface"]]
for fld in flds:
    df[fld]=df[fld].replace(np.nan, MEANGARDEN)


# CHANGE TYPE
#############
#classified.condition.isNewlyBuilt 


df[fields['price']] = df[fields['price']].astype(np.int64)
df[fields['gardensurface']] = df[fields['gardensurface']].astype(np.int64)

# REFORMAT COLUMNS
# remove all nans for now
#df=df.dropna()
#
# Save cleaned data for model
df.to_csv("../data/data_homes_cleaned.csv",index=False)
