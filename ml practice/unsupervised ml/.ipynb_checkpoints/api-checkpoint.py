from flask import Flask,request,jsonify
import joblib
import pandas as pd

# create flask app
app = Flask(__name__)

# connect postcall to predict
@app.route('/predict',methods=['POST'])
def predict():
    # get json data
    feat_data = request.json
    # convert to pandas df
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    # predict and return
    prediction = list(model.predict(df))
    return jsonify({'prediction':str(prediction)})

# load model and column names
if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('col_names.pkl')

    app.run(debug=True)


