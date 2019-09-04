from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import cv2
try:
    import cPickle as pickle
except:
    import pickle

import numpy as np

if __name__ == "__main__":
    model = MLPClassifier(solver="adam", alpha=1e-5, hidden_layer_sizes=(100, 100), random_state=1)
    scaler = StandardScaler()
    train_size = 2000

    X = [pickle.load( open("train_images/train%d.jpg" % n, "rb") ) for n in xrange(train_size)]
    X = np.array([cv2.resize(image[240:, :], (288, 96)).flatten() for image in X])
    scaler.fit(X)
    X = scaler.transform(X)
    y = pickle.load( open("moves.p", "rb") )
    y = np.array(y)

    model.fit(X, y)
    print model.score()

    #caution: will overwrite existing model if filename is same
    pickle.dump(model, open("model2.p", "wb"))

    #save the same scaler object to transform the test data
    pickle.dump(scaler, open("scaler.p", "wb"))
