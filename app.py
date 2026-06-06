from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    qr_image = None

    if request.method == "POST":

        data = request.form["data"]

        history.append(data)

        img = qrcode.make(data)

        if not os.path.exists("static"):
            os.makedirs("static")

        img.save("static/qrcode.png")

        qr_image = "qrcode.png"

    return render_template(
        "index.html",
        qr_image=qr_image,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)