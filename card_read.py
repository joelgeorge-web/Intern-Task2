import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'<C:\Users\Joel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Tesseract-OCR>'

# Function to preprocess the image before OCR
def preprocess_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    # Apply morphological operations
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel, iterations=1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Apply additional image preprocessing techniques if necessary
    # You can experiment with other techniques like resizing, smoothing, etc.

    return closing

# Function to extract numbers from an image region
def extract_numbers(image):
    extracted_numbers = pytesseract.image_to_string(image, config='--psm 6 digits')
    return extracted_numbers

# Function to extract text (name) from an image region
def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, config='--psm 7')
    return extracted_text

# Path to the debit card image
image_path = "id2.jpg"  # Replace with the actual image path

# Load the image
image = cv2.imread(image_path)

# Preprocess the image
preprocessed_image = preprocess_image(image)
plt.imshow(preprocessed_image, cmap='gray')
plt.axis('off')
plt.show()

# Define regions of interest for numbers and text
numbers_roi = preprocessed_image[220:269, 80:523]  # Adjust the coordinates to specify the desired region for numbers
text_roi = preprocessed_image[20:30, 50:50]  # Adjust the coordinates to specify the desired region for text

# Extract numbers from the numbers region
numbers = extract_numbers(numbers_roi)

# Extract text (name) from the text region
text = extract_text(text_roi)

# Print the extracted numbers and text
print("Extracted Numbers:")
print(numbers)

print("Extracted Text:")
print(text)
