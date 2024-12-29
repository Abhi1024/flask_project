from flask import Flask,request, render_template
import pickle

app = Flask(__name__)

randfor = pickle.load(open("Randfor.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def predict():

    SepalWidthCm = request.form["splw"]
    SepalLengthCm = request.form["spll"]
    PetalLengthCm = request.form["ptll"]
    PetalWidthCm =  request.form["ptlw"]

    result = randfor.predict([[SepalWidthCm,SepalLengthCm,PetalLengthCm,PetalWidthCm]])
    print(result)
    return render_template("index.html",ans = result)

if __name__ == "__main__":
    app.run(debug=True)