import io
from rccontrol import *
from picamera import PiCamera
try:
    import cPickle as pickle
except:
    import pickle
import numpy as np
from sklearn.neural_network import MLPClassifier
import cv2

nn_outputs = {
 'forward' : [1, 0, 0, 0],
 'reverse' : [0, 1, 0, 0],
 'forward_left' = [0, 0, 1, 0],
 'forward_right' = [0, 0, 0, 1]
}

direction_mapping = {
 'w' : 'forward',
 's' : 'reverse',
 'a' : 'forward_left',
 'd' : 'forward_right'
}

def takePicture():
    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('train_images/train%d.jpg' % n, gray_image)

def collectData():
    n = 0
    camera = picamera.PiCamera()
    time.sleep(2)
    moves = []

    while True:
        takePicture()
        #use WASD keys as arrow pad to tell car where to go.
        userInput = raw_input('Please enter a direction (Move %d): ' % n)
        while userInput != 'w' and userInput != 'a' and userInput != 's' and userInput != 'd':
            if userInput == 'x':
                break
            userInput = raw_input('Invalid direction, try again: ')
        direction = direction_mapping[userInput]
        goDirection(direction)
        moves.append(nn_outputs[direction])
        time.sleep(0.5)
        n += 1

    print 'Finished collecting data.'
    #pickled array of move data (expected output for model.)
    pickle.dump( moves, open( "moves.p", "wb" ) )

if __name__ == "__main__":
    collectData()
