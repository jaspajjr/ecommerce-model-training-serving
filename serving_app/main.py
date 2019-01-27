from flask import Flask, request
import pandas as pd

app = Flask(__name__)


class Model:

    def predict(self, data):
        return [1]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        df = pd.DataFrame.from_records(request.json)

        pred = house_price_model.predict(df[['age']])
        pred = pd.DataFrame(pred, columns=['predicted_price'])
        pred = pd.concat([df, pred], axis=1)

        return pred.to_json()


@app.before_first_request
def load_model():
    global house_price_model
    house_price_model = Model()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
