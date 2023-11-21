import numpy as np
import pickle
import pandas as pd
import flask
from flask import Flask, render_template, request

model = pickle.load(open("sales_demand_forecasting.pkl", "rb"))
app = Flask(__name__)

def sales_demand_forecasting(x):
    # Your sales demand forecasting logic here
    pred = model.predict(x)


    return pred[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    pred = None

    if request.method == 'POST':
        try:
            x = [[float(x) for x in request.form.values()]]
            prediction_text = sales_demand_forecasting(x)
        except Exception as e:
            return "An error occurred: " + str(e)
    print(pred)

    return render_template('predict.html', prediction_text=prediction_text)


if __name__ == "__main__":
    app.run()
