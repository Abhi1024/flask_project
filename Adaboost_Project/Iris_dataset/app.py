from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

Ada = pickle.load(open("Ada.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def predict():

    SepalLengthCm	=   request.form["spll"]
    SepalWidthCm	=   request.form["splw"]
    PetalLengthCm	=   request.form["ptll"]
    PetalWidthCm    =   request.form["ptlw"]

    result = Ada.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    return render_template("index.html",ans = result)

if __name__ == "__main__":
    app.run(debug=True)