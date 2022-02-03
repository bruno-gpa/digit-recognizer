from flask import Flask, render_template, request
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mim
import time
import io
import base64


app = Flask(__name__)
app.secret_key = "hafjionfonforfnofnerohae"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        base = request.form["img"]
        img = decode(base)
        pixels = resize(img)
        matrix = pixel_array(pixels, img)
        print(matrix)

        img = mim.imread(img, format="PNG")
        plt.imshow(img, interpolation="nearest")
        plt.show()
       
    return render_template("index.html")


def decode(string):
    base = string.replace('data:image/png;base64,', '').replace(' ', '+')
    if len(base) % 4:
        base += "=" * (4 - len(base) % 4)
    img = io.BytesIO(base64.b64decode(base))
    return mim.imread(img, format="PNG")


def resize(img):
    img = Image.fromarray(img)
    img = img.resize((28, 28), Image.ANTIALIAS)
    img = img.convert("L")
    return img.load()


def pixel_array(pixels, img):
    matrix = []
    for i in range(28):
        row = []
        for j in range(28):
            row.append(255 - pixels[j, i])
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    app.run(debug=True)
