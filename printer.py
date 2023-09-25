from flask import Flask
from flask import request
import json
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.post('/')
def login_post():
    data = request.get_json()
    image_url = data['image']
    image_source_url = data['image_source']
    image_qr_url = data['image_qr']

    img = Image.open(requests.get(image_url, stream=True).raw)

    # change to see fit
    img_out = img.resize((128, 128))
    img_out.show()

    img_src = Image.open(requests.get(image_source_url, stream=True).raw)

    img_src_out = img_src.resize((128, 128))
    img_src_out.show()

    img_qr = Image.open(requests.get(image_qr_url, stream=True).raw)

    img_qr_out = img_qr.resize((64, 64))

    # printer code for images
    return "ok"
