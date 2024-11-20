from PIL import Image
import datetime
import os

SAVE_PATH = os.path.join("static", "images")
os.makedirs(SAVE_PATH, exist_ok=True)


def save_image(image, prefix):
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{prefix}_{timestamp}.png"
        file_path = os.path.join(SAVE_PATH, file_name)
        print(f"Saving image to: {file_path}")  # Debugging step
        image.save(file_path)
        return file_name
    except Exception as e:
        print(f"Error saving image: {e}")  # Log errors
        return "Error: Could not save image"



def save_image_test():
    try:
        dummy_image = Image.new('RGB', (100, 100), color='blue')  # Create a dummy image
        save_image(dummy_image, "test")  # Test the save_image function
    except Exception as e:
        print(f"Test failed: {e}")

save_image_test()
