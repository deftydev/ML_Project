from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



application= Flask(__name__)
app=application
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.methods=='GET':
        return render_template('home.html')

if __name__ =="__main__":
    app.run(debug=True)
