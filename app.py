from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

# Define o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        if "image" in request.files:
            img = request.files["image"]
            path = os.path.join(UPLOAD_FOLDER, img.filename)
            img.save(path)
            text = pytesseract.image_to_string(Image.open(path))
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
