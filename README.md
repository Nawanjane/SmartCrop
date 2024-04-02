

# Crop Prediction App

The Crop Prediction App is a machine learning-powered Flask application that assists farmers and agricultural professionals in making informed decisions about crop selection based on various soil and environmental factors.

## Description

This application uses historical data on crop performance, soil composition, and climate patterns to predict the most suitable crops for a given set of conditions. It leverages a machine learning model with a 97% accuracy rate, providing users with reliable and actionable insights.

## Getting Started

### Dependencies

- Python 3.6+
- Flask
- TensorFlow
- NumPy
- Pandas
- scikit-learn
- joblib

### Installing

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/crop-prediction-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crop-prediction-app
   ```
3. Set Up a Virtual Environment (Optional but Recommended)
   It is a good practice to create a virtual environment for your project to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Executing the program

1. Run the Flask application:
   ```bash
   export FLASK_APP=app.py
   flask run
   ```
2. Access the web interface at `http://127.0.0.1:5000/` in your browser.

## Deployment

The app is currently running on localhost for development and testing. Plans for deployment to an online server are underway to make the app publicly accessible.

## Results

The app successfully predicts suitable crops with a 97% accuracy rate. Validation and testing have been conducted to ensure the model's reliability.

## Help

Any issues or questions can be directed to the Issues section of the GitHub repository.

## Contributing

Contributions are welcome! Please Contact Us for details on our code of conduct and the process for submitting pull requests.

## Authors

Nimendra Nawanjane
nimendradandeniya@gmail.com

## License

This project is licensed under the MIT License 

