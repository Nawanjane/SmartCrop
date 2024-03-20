from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import joblib

# Load the trained model and scaler
model = tf.keras.models.load_model('my_model.h5')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        input_features = [float(request.form.get(feature)) for feature in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        
        # Scale the features
        input_features = np.array(input_features).reshape(1, -1)
        input_features_scaled = scaler.transform(input_features)
        
        # Make prediction
        prediction = model.predict(input_features_scaled)
        predicted_class = np.argmax(prediction, axis=1)
        
        # Convert class index to label
        label_encoder = joblib.load('label_encoder.pkl')  # Make sure to save the label encoder during model training
        predicted_label = label_encoder.inverse_transform(predicted_class)[0]
        
        return render_template('index.html', prediction=predicted_label)
    except Exception as e:
        return render_template('index.html', prediction=str(e))

if __name__ == '__main__':
    app.run(debug=True)
