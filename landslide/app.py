import numpy as np
from flask import Flask, request,render_template,jsonify
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = []
    for x in request.form.values():
        if not x.isnumeric():
            response = {"status" : 500,"status_msg": "Some fields are empty !"}
            return jsonify(response)

        float_features.append(int(x))

    
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    response = {"status" : 200,"status_msg": "No chance for Landslide"}

    if prediction == "yes":
        response = {"status" : 200,"status_msg": "Landslide may occur..!!"}

    return jsonify(response)

if __name__ == "__main__":
    flask_app.run(debug=True)