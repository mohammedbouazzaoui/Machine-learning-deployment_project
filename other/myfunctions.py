# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:52:11 2022

@author: bmadmin
"""

import sys
sys.path.append(".")
sys.path.append("./predict")
sys.path.append("./preprocessing")
sys.path.append("./model")
sys.path.append("./other")




def debug(DEBUG,m):
    if DEBUG:
        print("\nDEBUG@@@:---",m,"---@@@\n")