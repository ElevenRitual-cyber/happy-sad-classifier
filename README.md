# happy-sad-classifier
A **Convolutional Neural Network (CNN)** built using **TensorFlow** and **OpenCV** to classify facial expressions as either **happy** or **sad**. This project demonstrates image preprocessing, model training, evaluation, and prediction from uploaded or file-based images.
---
## 🧠 Features
- Image preprocessing using OpenCV
- CNN architecture built with TensorFlow/Keras
- Training on labeled "happy" and "sad" face images
- Prediction on new images (file paths or file-like objects)
- Ready for integration into web apps (e.g., Flask or Streamlit)
---
## 🛠️ Technologies Used
- Python 3.x
- TensorFlow 2.x
- OpenCV
- NumPy
- scikit-learn (for data splitting and encoding)
- Flask (for building the API)
---
## 📦 Dataset
This project uses the [Happy-Sad Images Dataset](https://www.kaggle.com/datasets/billbasener/happy-sad-images) from Kaggle.
- The dataset contains labeled facial expression images stored in `happy/` and `sad/` folders.
- Download and extract it into the `dataset/` folder before training.
---
## 🌐 Flask API

This project also includes a **Flask API** (`app.py`) for serving the trained CNN model. The API allows users to upload an image and receive a prediction indicating whether the face is **happy** or **sad**.


   ```bash
   pip install -r requirements.txt
