from flask import request,render_template,request
import tensorflow as tf
from model import predictor


def register_route(app):

   @app.route('/predict', methods=['GET', 'POST'])
   def predict():
        if request.method == 'GET':
            return render_template('home.html')

        if 'file' not in request.files:
            return 'No file uploaded', 400

        img = request.files['file']
        yhat = predictor(img)
        print(yhat)
        emotion = "Happy" if yhat < 0.5 else "Sad"
        return render_template('home.html', emotion=emotion),200


