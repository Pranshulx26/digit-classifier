

from flask import Blueprint, render_template, request, jsonify
import os
import numpy as np
from PIL import Image
import io
import base64
import joblib
import datetime

# Blueprint for views
views = Blueprint('views', __name__)

# Load the trained model
MODEL_PATH = r'C:\Users\91965\digit-classifier\notebooks\best_random_forest_model.pkl'
model = joblib.load(MODEL_PATH)

# Ensure correct path for saving images in the app's static folder
SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images")
os.makedirs(SAVE_PATH, exist_ok=True)

@views.route('/')
def index():
    """Render the index page."""
    return render_template("index.html")

@views.route('/predict', methods=['POST'])
def predict_digit():
    """Handle image uploads and return digit predictions."""
    try:
        if 'image' in request.files:
            # Handle uploaded image
            image_file = request.files['image']
            image = Image.open(image_file)

            # Save the uploaded image
            file_name = save_image(image, "uploaded")

            # Process and predict the digit
            prediction = process_image(image)
            return jsonify({"prediction": prediction, "saved_as": file_name}), 200

        elif request.json.get('image'):
            # Handle canvas image (Base64 data)
            image_data = request.json['image']
            image = decode_base64_image(image_data)
            if image:
                # Save the canvas image
                file_name = save_image(image, "canvas")

                # Process and predict the digit
                prediction = process_image(image)
                return jsonify({"prediction": prediction, "saved_as": file_name}), 200
            else:
                return jsonify({"error": "Invalid image data"}), 400

        return jsonify({"error": "No image provided"}), 400

    except Exception as e:
        print(f"Error in predict_digit: {e}")
        return jsonify({"error": "Internal server error"}), 500

def decode_base64_image(base64_data):
    """Decode a base64 image string and return it as a PIL Image."""
    try:
        # Remove the base64 prefix and decode
        image_data = base64.b64decode(base64_data.split(',')[1])
        image = Image.open(io.BytesIO(image_data))
        return image
    except Exception as e:
        print(f"Error decoding image: {e}")
        return None

def save_image(image, prefix):
    """Save the image to the static/images directory."""
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{prefix}_{timestamp}.png"
        file_path = os.path.join(SAVE_PATH, file_name)
        image.save(file_path)
        return file_name
    except Exception as e:
        print(f"Error saving image: {e}")
        return "Error: Could not save image"

from PIL import Image, ImageOps
import numpy as np

def process_image(image):
    """
    Preprocess the uploaded image and predict the digit.
    - Convert the image to grayscale.
    - Resize it to 28x28 pixels.
    - Invert colors if necessary (ensure black digit on white background).
    - Normalize pixel values to [0, 1].
    - Flatten the image to match the model's input format.
    - Predict the digit using the trained model.
    """
    try:
        # Step 1: Convert to grayscale
        image = image.convert('L')

        # Step 2: Invert the image if necessary
        # Check the mean pixel value to decide whether to invert
        if np.mean(np.array(image)) > 128:  # Likely white background, black digit
            image = ImageOps.invert(image)

        # Step 3: Resize to 28x28 pixels
        image = image.resize((28, 28), Image.Resampling.LANCZOS)

        # Step 4: Normalize pixel values to [0, 1]
        image_array = np.array(image) / 255.0

        # Step 5: Flatten the image to match the model input
        image_array = image_array.reshape(1, -1)

        # Debugging: Log preprocessing steps
        print(f"Processed image array shape: {image_array.shape}")
        print(f"Processed image array (first 10 pixels): {image_array[0][:10]}")

        # Step 6: Predict the digit using the trained model
        prediction = model.predict(image_array)
        print(f"Prediction: {prediction}")  # Debugging: Log prediction

        # Return the predicted digit as a string
        return str(prediction[0])

    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error: Prediction failed"