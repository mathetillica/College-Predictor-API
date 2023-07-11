# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:02:31 2023

@author: HP
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class user_input(BaseModel):
    Category: str 
    Pool: str 
    Rank: int 
    Delta: int