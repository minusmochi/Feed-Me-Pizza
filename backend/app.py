from flask import Flask
import pizza

app = Flask(__name__)

@app.route('/pizza')
def getPizza():
    return pizza.getPizzaTweet()