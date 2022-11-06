from flask import Flask,request, url_for, redirect, render_template, jsonify
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# set path to model files here
model = pickle.load(open('model/dt2.pkl', 'rb'))

cols = ['gender', 'age', 'Systolic BP', 'Weight', 'Height','BMI','Symptoms','Melena','hematochezia','Initial Hb',
       'BUN/Cr', 'aPTT', 'INR', 'NSAIDS', 'Anticoag','Antiplatelet','PPI']


@app.route('/')
def home():
    return render_template("home.html")

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 17)
    result = model.predict(to_predict)

    return result[0]

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        pred = ValuePredictor(to_predict_list)
        pred = int(pred)
       
        print("Units of Blood Required: ",pred)
        
        return render_template('home.html',pred="Units of Blood Required: {}".format(pred))

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction =model.predict(data_unseen)
   
    output = int(prediction[0])
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
