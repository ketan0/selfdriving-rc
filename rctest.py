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
while True:
  stream = io.BytesIO()
  camera.capture(stream, use_video_port=True, format='jpeg')
  data = np.fromstring(stream.getvalue(), dtype=np.uint8)

  image = cv2.imdecode(data, 0)[240:, :]
  print image.shape
  small_img = scaler.transform(cv2.resize(image, (288, 96)).flatten())
  prediction = model.predict_proba([small_img])
  #print "Predicted direction: %s" % prediction
  max_index, max_value = max(enumerate(prediction[0]), key=lambda p: p[1])
  if max_index == 0:
      goDirection(forward)
  elif max_index == 1:
      goDirection(reverse)
  elif max_index == 2:
      goDirection(forward_left)
  elif max_index == 3:
      goDirection(forward_right)
