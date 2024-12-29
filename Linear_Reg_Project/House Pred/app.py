from flask import Flask,render_template,request,session
import numpy as np
import pickle

app = Flask(__name__)

lin = pickle.load(open("homeprices.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict():
    area = int(request.form['area'])
    bedroom = int(request.form['bedroom'])
    age = int(request.form['age'])

    final_test = np.array([(area,bedroom,age)])
    predict = lin.predict(final_test)
    ans = round(float(predict))
    return render_template("index.html",pred = int(ans))

if __name__ == "__main__":
    app.run(debug=True)