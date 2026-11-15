from flask import Flask, render_template, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():

    if "image" not in request.files:
        return "Image not found", 400

    file = request.files["image"]

    if file.filename == "":
        return "No image selected", 400

    output = remove(file.read())

    return send_file(
        io.BytesIO(output),
        mimetype="image/png",
        download_name="Syed-AI-Photo.png"
    )

if __name__ == "__main__":
    app.run()
