

from keras.models import load_model
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.preprocessing import image

img_width, img_height = 299, 299
print("loading model...")
model = load_model('inceptionv3_1.h5')
print (model.summary())
print("model loaded")

import numpy as np
import tensorflow as tf
import glob
from PIL import Image

graph = tf.get_default_graph()
def show_pil_image(img):
    filename = "aa_image.jpg"
    img.save(filename)
    import webbrowser
    webbrowser.open(filename)

def predict(image_file):
    img = image.load_img(image_file, target_size=(img_width,img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return preds


def classify_last_image(path):
    filenames = sorted(glob.glob(os.path.join(path,"*.jpg")))
    lastfilename = filenames[-1]
    predictions = predict(lastfilename)

