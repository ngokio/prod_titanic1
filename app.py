import pandas as pd
import joblib
from house_functions import first_letter
import sklearn
from flask import Flask,request

#chargement model
pipeline=joblib.load('titanic1.model')

#Demarer l'application Flask
app = Flask("__name__")

#Predictions
@app.route('/predict',methods=['POST'])
def predict():
  df=pd.DataFrame(request.json)
  resultat=pipeline.predict(df)[0]
  return (str(resultat),201)

# tester mon API
@app.route("/ping",methods=['GET'])
def ping():
  return ('pong',200)

# creation de la page d'accueil
@app.route('/')
def index():
  return "<h1>Bienvenu dans la page de predictions des survies du titanic</h1>"


if __name__=="__main__":
  app.run(host='0.0.0.0')