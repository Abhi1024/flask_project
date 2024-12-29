from flask import Flask,request,session,render_template
import numpy as np
import pickle
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)

sinpol = pickle.load(open("ice_cream.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def predict():
    poly = PolynomialFeatures()

    temp = float(request.form["temp"])

    final = np.array([[(temp)]])
    ans = sinpol.predict(poly.fit_transform(final))
    # print(ans)
    return render_template("index.html",predict=ans)

if __name__ == "__main__":
    app.run(debug=True)