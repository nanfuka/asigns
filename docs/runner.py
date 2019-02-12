import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from PIL import Image
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import urllib
# import cv2
 


UPLOAD_FOLDER = '/Users/Emmanuel/asigns/docs/pics'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return  render_template('index.html')


# METHOD #1: OpenCV, NumPy, and urllib
@app.route('/yokya', methods=['GET', 'POST'])

def url_to_image():
	# download the image, convert it to a NumPy array, and then read
	# # it into OpenCV format
	# resp = urllib.urlopen(url)
	# image = np.asarray(bytearray(resp.read()), dtype="uint8")
	# image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# # return the image
	# return image



  img = Image.open('/Users/Emmanuel/asigns/docs/pics/WIN_20180104_14_51_23_Pro.jpg')
  return  render_template('index.html', image = img )

if __name__ == '__main__':
  app.run(debug=True)
   