from flask import Flask, render_template,request,session
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pickle

app = Flask(__name__)

polylin = pickle.load(open("ice_cream.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict():
    pol = PolynomialFeatures()

    temp = float(request.form['temp'])
    ice_unit = float(request.form['ice_unit'])

    fin_test = np.array([(temp,ice_unit)])
    # print(fin_test)
    predict = polylin.predict(pol.fit_transform(fin_test))
    # ans = round(float(predict))
    # ans = predict
    print(predict)
    return render_template("index.html", predict= predict)

if __name__ == "__main__":
    app.run(debug=True)