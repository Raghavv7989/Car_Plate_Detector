import cv2
import pytesseract
import numpy as np
import platform

# macOS/Linux users: no need to set tesseract_cmd if installed via brew or apt
if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Path to the input image
image_path = 'car.jpg'

# Load the image
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Copy for display
display_image = image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to reduce noise
filtered = cv2.bilateralFilter(gray, 11, 17, 17)

# Edge detection
edged = cv2.Canny(filtered, 30, 200)

# Find contours
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Detect number plate contour
plate = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        plate = approx
        break

text = ""
if plate is not None:
    # Draw bounding box
    cv2.drawContours(display_image, [plate], -1, (0, 255, 0), 3)

    # Mask and crop
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [plate], 0, 255, -1)
    x, y = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    cropped = gray[topx:bottomx+1, topy:bottomy+1]

    # OCR
    text = pytesseract.image_to_string(cropped, config='--psm 8').strip()
    print("Detected Number Plate Text:", text)
    cv2.putText(display_image, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
else:
    print("Number plate could not be detected.")
    cv2.putText(display_image, "Plate Not Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

# Display the result
cv2.imshow("Number Plate Detection", display_image)
cv2.waitKey(0)
cv2.destroyAllWindows()