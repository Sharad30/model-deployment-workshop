from flask import Flask, request, jsonify
import pandas as pd
import pickle


app = Flask(__name__)


with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        dataframe = pd.DataFrame(data, index=[0])
        prediction = model.predict(dataframe)
        return jsonify({'prediction': prediction[0]})
    except:
        return jsonify({'error': 'error processing request'})

if __name__ == '__main__':
    app.run(debug=True)
