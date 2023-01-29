from flask import Flask, render_template
import requests
from request_choices import get_top_and_bottom

app = Flask(__name__)

@app.route("/")
def dsg_index():
    bottom, top = get_top_and_bottom()
    return render_template("index.html", bottom=bottom, top=top)