# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
sys.path.append("./predict")
sys.path.append("./preprocessing")

def createmainform():
    dr="./templates/"
    f="mainformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    
    fp=open(dr+f,"w")
    fp.write("<form action=\"/cleanup/\" method = \"POST\">\n")
    line="<p>    PRESS TO CLEANUP SCRAPED DATA</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f

def createinputform():
    dr="./templates/"
    f="inputformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    flds=[("constructionYear","Construction Year"),
          ("gardensurface", "Garden Surface")
          ]
    fp=open(dr+f,"w")
    fp.write("<form action=\"/predict/\" method = \"POST\">\n")
    for fld in flds:
        #print(fld[0],fld[1])
        line="<p>"+fld[1]+" <input type = \"text\" name = \""+fld[0]+"\" /></p>\n"
        fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f

def createcleanupform():
    dr="./templates/"
    f="cleanupformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    
    fp=open(dr+f,"w")
    fp.write("<form action=\"/cleanupinfo/\" method = \"POST\">\n")
    line="<p>    PRESS TO CLEANUP SCRAPED DATA</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    #print("@@@@@@@@@@@@@@@",f)
    return f
def createcleanupinfoform():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    dr="./templates/"
    f="cleanupinfoformdyn.html"
    #['classified.building.constructionYear','classified.outdoor.garden.surface']
    #['classified.price']
    fp=open(dr+f,"w")
    fp.write("<form action=\"/input/\" method = \"POST\">\n")
    line="<p>    PRESENT INFO ABOUT CLEANING press to go to input form</p>\n"
    fp.write(line)
    fp.write("<p><input type = \"submit\" value = \"Submit\" /></p>\n")
    
    fp.write("</form>")
    fp.close()
    return f

