# **Digit Classifier Web Application**

This project is a simple web application built using **Flask**, where users can upload or draw an image of a digit, and the application predicts the digit using a  **Random Forest** model. The model is saved using **joblib** and the image is processed using **PIL (Pillow)**. The web app allows the user to upload an image or draw digits on a canvas, and it will predict the digit and display the result. It also saves the image file with a timestamp for reference.

### **Project Overview**

- **Backend**: The backend is powered by **Flask**, a lightweight Python web framework. It handles image uploads, processes them, and returns predictions.
- **Model**: A **Random Forest** classifier is used to predict the digit from the uploaded or drawn image. The model has been pre-trained and saved using **joblib**.
- **Image Processing**: The images are processed using **PIL (Pillow)** to convert them to grayscale, resize them to the required dimensions (28x28 pixels), and normalize pixel values before making predictions.
- **Frontend**: The frontend allows users to either upload an image or draw a digit on an interactive canvas. The user can then submit the image for prediction.
- **Saved Images**: Images uploaded or drawn by the user are saved to a local directory with a timestamp in the filename for easy reference.

### **How the Project Works**

1. **Image Upload**: Users can upload an image of a handwritten digit. The image is processed, and the digit is predicted.
2. **Drawing on Canvas**: Users can also draw a digit on the canvas provided by the web app. The drawn image is captured in base64 format and sent to the backend for prediction.
3. **Prediction**: The model predicts the digit, and the result is displayed on the web page along with the filename of the saved image.
4. **Image Saving**: The uploaded or drawn image is saved with a timestamp to the `static/images` folder, allowing users to track the image and predictions.

### **Technologies Used**

- **Flask**: Web framework to serve the application.
- **PIL (Pillow)**: For image manipulation and processing.
- **scikit-learn**: For training and using the Random Forest model.
- **joblib**: For saving and loading the trained model.
- **Numpy**: For array manipulation and image normalization.

### **How to Download and Set Up the Project**

To run this project locally, follow these steps:

1. **Clone the Repository**:
   Open your terminal and clone the repository using Git:
   ```bash
   git clone https://github.com/your-username/digit-classifier.git
   cd digit-classifier

2. **Set Up Virtual Environment**:
   Create and activate a virtual environment to manage project dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Mac/Linux
   venv\Scripts\activate       # For Windows

3. **Install Dependencies**:
   Install the required dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt

4. **Run the Application**: 
Start the Flask server by running:
```bash
python app.py