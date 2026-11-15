from flask import Flask, render_template, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    file = request.files["image"]
    output = remove(file.read())

    return send_file(
        io.BytesIO(output),
        mimetype="image/png",
        download_name="Syed-AI-Photo.png"
    )

if __name__ == "__main__":
    app.run(debug=True)