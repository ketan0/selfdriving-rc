import io
from rccontrol import *
from picamera import PiCamera
import picamera.array
try:
    import cPickle as pickle
except:
    import pickle
import numpy as np
from sklearn.neural_network import MLPClassifier
import cv2

F_out = [1, 0, 0, 0]
B_out = [0, 1, 0, 0]
L_out = [0, 0, 1, 0]
R_out = [0, 0, 0, 1]

def collectData():
    n = 0
    camera = picamera.PiCamera()
    time.sleep(2)
    moves = []

    while True:
        stream = io.BytesIO()
        camera.capture(stream, use_video_port=True, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('train_images/train%d.jpg' % n, gray_image)

        userInput = raw_input("Please enter a direction (Move %d): " % n)
        while userInput != 'w' and userInput != 'a' and userInput != 's' and userInput != 'd' and userInput != 'x':
            userInput = raw_input("Invalid direction, try again: ")
        if userInput == 'w':
            goDirection(forward)
            moves.append(F_out)
        elif userInput == 'a':
            goDirection(forward_left)
            moves.append(L_out)
        elif userInput == 's':
            goDirection(reverse)
            moves.append(B_out)
        elif userInput == 'd':
            goDirection(forward_right)
            moves.append(R_out)
        elif userInput == 'x':
            break
        time.sleep(0.5)
        n += 1

    pickle.dump( moves, open( "moves.p", "wb" ) )

def trainModel():
    X = [cv2.imread('train_images/train%d.jpg' % n)[240:, :, 0].flatten() for n in xrange(205)]
    y = pickle.load( open( "moves.p", "rb" ) )
