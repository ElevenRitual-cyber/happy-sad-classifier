import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2

def predictor(imgx):
    # Case 1: If it's a file-like object (e.g., from upload)
    if not isinstance(imgx, np.ndarray):
        file_bytes = np.frombuffer(imgx.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Image decoding failed. Make sure the uploaded file is a valid image.")
    else:
        # Case 2: It's already a NumPy array (e.g., from cv2.imread)
        img = imgx

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize to match model input
    img = cv2.resize(img, (256, 256))

    # Normalize and expand dims
    img = img / 255.0
    input_array = np.expand_dims(img, axis=0)

    # Load the model
    model = load_model('happysad.keras')

    # Predict
    yhat = model.predict(input_array)
    return yhat
