from flask import Flask, render_template,request
import numpy as np
import pickle
# from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

mul_log = pickle.load(open("iris.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def log_predict():

    # log = LogisticRegression()

    SepalLengthCm = float(request.form["text1"])
    SepalWidthCm = float(request.form["text2"])
    PetalLengthCm = float(request.form["text3"])
    PetalWidthCm = float(request.form["text4"])

    arr = np.array([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    predict = mul_log.predict(arr)
    return render_template("index.html", predict=predict)
    # print(predict)

if __name__ == "__main__":
    app.run(debug=True)