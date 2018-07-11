import cPickle as pickle
import io
import numpy as np
import cv2
from picamera import PiCamera
from rccontrol import *
from sklearn.preprocessing import StandardScaler

camera = PiCamera()
model = pickle.load( open('model2.p', 'rb') )
scaler = pickle.load( open('scaler.p', 'rb') )

def testDrive():
    while True:
      #capture and process image
      stream = io.BytesIO()
      camera.capture(stream, use_video_port=True, format='jpeg')
      data = np.fromstring(stream.getvalue(), dtype=np.uint8)
      image = cv2.imdecode(data, 0)[240:, :]
      small_img = scaler.transform(cv2.resize(image, (288, 96)).flatten())

      #choose highest-probability direction, and go that way
      prediction = model.predict_proba([small_img])
      max_index, max_value = max(enumerate(prediction[0]), key=lambda p: p[1])
      if max_index == 0:
          goDirection('forward')
      elif max_index == 1:
          goDirection('reverse')
      elif max_index == 2:
          goDirection('forward_left')
      elif max_index == 3:
          goDirection('forward_right')

if __name__ == "__main__":
    testDrive()
