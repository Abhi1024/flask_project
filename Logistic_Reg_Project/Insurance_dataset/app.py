from flask import Flask,render_template,request,session
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

logis = pickle.load(open("insurance.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def predict():

    logi = LogisticRegression()

    age = float(request.form['Age'])
    # print(age)

    fin_test = np.array([(age)])
    print("fin = ",fin_test)
    predict = logis.predict([[age]])
    print(predict)
    return render_template("index.html",predict=predict)


if __name__ == "__main__":
    app.run(debug=True)