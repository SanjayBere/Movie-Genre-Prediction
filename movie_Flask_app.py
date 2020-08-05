from flask import Flask , render_template , request
import  pickle

pickle.load(open())


app = Flask(__name__)

@app.route('/')
def home():
    render_template("index.html")

@app.route('/predict',method = ['POST'])
def predict():
    if request.method == 'POST':
        message = request.form(['message'])
        data = [message]

