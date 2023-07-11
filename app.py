# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:01:48 2023

@author: HP
"""

import uvicorn
from fastapi import FastAPI
from Inputs import user_input
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("clg_prd.pkl","rb")
rf=pickle.load(pickle_in)
df = pd.read_csv('IIT_cleanData.csv')
df['Sr.'] = df['Sr.'].astype(float)
df['Opening'] = df['Opening'].astype(float)
df['Closing'] = df['Closing'].astype(float)
d1={'GEN': 0,
 'GEN-EWS': 1,
 'GEN-EWS-PWD': 2,
 'GEN-PWD': 3,
 'OBC-NCL': 4,
 'OBC-NCL-PWD': 5,
 'SC': 6,
 'SC-PWD': 7,
 'ST': 8,
 'ST-PWD': 9}
d2={'Female-Only': 0, 'Gender-Neutral': 1}

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def README():
    return "ALLOWED CATEGORY TYPES: GEN, GEN-EWS, GEN-EWS-PWD, GEN-PWD, OBC-NCL, OBC-NCL-PWD, SC, SC-PWD,ST, ST-PWD  ;  ALLOWED POOL TYPES: Female-Only, Gender-Neutral"
            
# Adding Predicition functionality
@app.post('/predict')
def PREDICT_COLLEGE(data:user_input):
    data = data.dict()
    Category=data['Category']
    Pool=data['Pool']
    Rank=data['Rank']
    Delta=data['Delta']
    test_df=[[d1[Category],d2[Pool],Rank-Delta,Rank+Delta]]
    predictions = rf.predict_proba(test_df)[0]
    res = np.argsort(predictions)[-20:]
    j=0
    i=0
    ans=[]
    while((j<10) and (i<20)):
        if(d1[df.iloc[res[0][-1-i]][6]]==test_df[0][0]):
            if(d2[df.iloc[res[0][-1-i]][7]]==test_df[0][1]):
                ans.append(df.iloc[res[0][-1-i]][2:8])
                j=j+1
        i=i+1
    return ans

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload