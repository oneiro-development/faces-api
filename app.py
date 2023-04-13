from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import faces

app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # get the uploaded files from the request object
    files = request.files.getlist('image')

    # create an empty list to store the ndarray for each image
    img_arrays = []

    # loop over each uploaded file
    for file in files:
        # open the image file using Pillow
        img = Image.open(file)

        # convert the image to a NumPy ndarray
        img_array = np.array(img)

        # append the ndarray to the list
        img_arrays.append(img_array)

    return jsonify(any(faces.compare_faces2(img_arrays[0], img_arrays[1]))), 200

if __name__ == '__main__':
    app.run(port=5001)
