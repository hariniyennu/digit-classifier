from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import os

# Ensure the model file exists
MODEL_PATH = "model/digit_classifier.keras"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("canvas.html")  
    
@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["image"]
        img = Image.open(file).convert("L")  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to match model input size
        # Convert to NumPy array and normalize
        img = np.array(img).astype("float32") / 255.0  
        img = 1 - img  
        img = img.reshape(1, 28, 28, 1)  
        # print("Expected Model Input Shape:", model.input_shape)
        # print("Processed Image Shape:", img.shape)
        # print("First few pixel values:", img.flatten()[:10])

        # Get model prediction
        prediction = model.predict(img)
        digit = np.argmax(prediction)  
        return jsonify({"digit": int(digit)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error if something goes wrong
if __name__ == "__main__":
    app.run(debug=True)  
