from flask import Flask, request, render_template  # webserver for convenience/demo

from base64 import b64decode # Javascript sends image as base64 encdoded...
from io import BytesIO       # ...bytes

from PIL import Image        # image processing library (required for proof-of-concept)

import re                    # because useful

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route('/')
def index():
    return render_template('index.html', msg='')

@app.route('/result', methods=['POST'])
def process_image():
    b64_image_data = request.form['image-data']
    image_data = re.sub("^data:image/png;base64,", "", b64_image_data)
    image_data = b64decode(image_data)
    image_data = BytesIO(image_data)
    image = Image.open(image_data)
    
    # following is just to demonstrate we're processing it
    
    black_pixels = 0
    for x in range(image.size[0]):
      for y in range(image.size[1]):
          if image.getpixel((x, y)) == (0, 0, 0, 255):
              black_pixels += 1
    msg_html= (
      "Server-side processing with python:<br>"
      "Image is {} by {} pixels<br>of which {} {} black".format(
        image.width, image.height, black_pixels,
        'is' if black_pixels == 1 else 'are')
    )
    return render_template('result.html', msg=msg_html, b64_image_data=b64_image_data)

