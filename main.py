# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:30:48 2023

@author: HP
"""

import uvicorn ##ASGI
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To College Predictor App': f'{name}'}




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload