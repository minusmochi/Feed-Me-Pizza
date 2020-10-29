from flask import Flask
from flask import jsonify
from flask_cors import CORS
import pizza

app = Flask(__name__)
CORS(app)

@app.route('/pizza')
def getPizza():
    return jsonify(pizza.getPizzaTweet())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')