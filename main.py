# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 10:29:13 2025

@author: DIZZLER
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    
    # defining the datatypes of the parameters
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age: int
    
# loading the saved model
diabetes_model = pickle.load(open('C:/Users/DIZZLER/Downloads/ML, DL and AI/ML API in Heroku/diabetes_trained_model.sav', 'rb'))

@app.post('/diabetes_prediction_by_Ahmed_Masood')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data) # dictionary created
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list]) # putting the list in a list using [] to tell the model this is just 1 datapoint.
                                                      # this helps to avoid the reshape thing
    
    if prediction[0]==0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'