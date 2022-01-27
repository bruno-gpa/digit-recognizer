from flask import Flask, render_template, request
from PIL import Image
import time
import numpy as np


app = Flask(__name__)
app.secret_key = "hafjionfonforfnofnerohae"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
