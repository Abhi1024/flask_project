from flask import Flask, render_template,request
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

dectre = pickle.load(open("dectree.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/", methods=["POST"])
def predict():

    outlook = request.form["outlook"]
    humidity = request.form["humidity"]
    wind = request.form["wind"]
    temp = request.form["temp"]
    
    # Outlook1 = LabelEncoder()
    # Humidity1 = LabelEncoder()
    # Wind1 = LabelEncoder()
    # Temp1 = LabelEncoder()

    # outlook = Outlook1.fit_transform(outlook)
    # humidity = Humidity1.fit_transform(humidity)
    # wind = Wind1.fit_transform(wind)
    # temp = Temp1.fit_transform(temp)


    result = dectre.predict([[outlook,humidity,wind,temp]])
    return render_template("index.html",predict = result)

if __name__ == "__main__":
    app.run(debug=True)