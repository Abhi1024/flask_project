from flask import Flask, render_template,request
import pickle

app = Flask(__name__)

navby = pickle.load(open("navbyies.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def predict():

    Gender = int(request.form["gender"])
    Age = int(request.form["age"])
    EstSal = int(request.form["estsal"])

    # result = navby.predict([[Gender,Age,EstSal]])
    # print(result)

    predict = navby.predict([[Gender,Age,EstSal]])

    if predict == 1:
        ans1 = "Purchased"
    else:
        ans1 = "Not Purchased"

    return render_template("index.html", ans = ans1)

if __name__ == "__main__":
    app.run(debug=True)