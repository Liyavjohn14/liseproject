# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fKqGENiyDMLsavgH8U6c1zWF5CjjEz99
"""

from flask.templating import render_template_string
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:33:38 2021

@author: MY BOOK
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
temp= pickle.load(open('svd.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('dress home.html')

@app.route('/predict',methods=['POST'])
def predict():
  weight=float(request.form["weight"])
  height = float(request.form["height"])
  age = int(request.form["age"])
  bust_size = float(request.form["bust_size"])
  occasion = request.form["occasion"]
  #session['ans']=str(occasion)
  arr=np.array([weight,age,height,bust_size])
  answer=predict(arr)
  arr1=np.array([answer,occasion])
  result=predict(arr1)
  #session['ansi']=str(answer)
  return render_template('recom.html',answer=result)
  
'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
  ans=session.get('ans')
  ansi=session.get('ansi')
  result=np.array([ans,ansi])
  recomm=model.predict(result)
  return recomm
  '''
 



if __name__ == "__main__":
    app.run(debug=True)