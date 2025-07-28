# 🚗 Car Number Plate Detection

This is a computer vision project that detects a number plate from an image of a car and extracts the text using Tesseract OCR.

## 🔍 Features

- Detects and highlights the number plate on a car image
- Extracts the text (plate number) using `pytesseract`
- Displays the annotated image in a popup window
- Prints the number plate text in the terminal

---

## 🖼️ Example Output

![Example Output](demo_output.jpg)

---

## 📁 Project Structure

Car_Number_Plate_Detection/
│
├── main.py # Main detection code
├── car.jpg # Input image (replace with your own)
├── requirements.txt # Python dependencies
└── README.md # Project details

---

## 🔧 Requirements

- Python 3.7+
- OpenCV
- NumPy
- pytesseract
- Tesseract OCR engine (system-installed)

---

## 💻 Installation & Usage

### 1. Clone the repo or download the ZIP

```bash
git clone https://github.com/Raghavv7989/Car-Number-Plate-Detection.git
cd Car-Number-Plate-Detection
2. Install Python dependencies
pip install -r requirements.txt
3. Install Tesseract (if not already)
macOS
brew install tesseract
Ubuntu
sudo apt install tesseract-ocr
Windows
Download Tesseract for Windows
Then add path to main.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
4. Run the Project
python main.py
A popup will appear with:
Green box around the number plate
Extracted number at the top of the image
Number also printed in your terminal
