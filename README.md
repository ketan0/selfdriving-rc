# autonomous-rc

In this project, I built an autonomous RC car using Raspberry Pi, a Pi Camera, and an inexpensive RC car.

In order to control the RC car, the [pi-rc](https://github.com/bskari/pi-rc) library was used to turn the Raspberry Pi into a radio-frequency transmitter. Functions for basic directional control are contained in `rccontrol.py`. In order to send commands successfully, one must simultaneously run `make` and `sudo ./pi_pcm -v` in the `pi_pcm` folder.

A multi-layer perceptron (MLP) neural network was implemented using the [scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier) package. The network takes as input the flattened, grayscaled contents of a Pi Camera image, and outputs one of four directions: forward, left, right, or reverse. For training, the car should be driven through a track of some sort (I used paper for the lanes.)

[![Autonomous test](https://img.youtube.com/vi/bulzQxh9DlI/maxresdefault.jpg)](https://www.youtube.com/watch?v=bulzQxh9DlI)

## Credit

https://github.com/bskari/pi-rc
http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier


Inspiration for this project taken from:
http://blog.davidsingleton.org/nnrccar/
Andrew Ng's Machine Learning course on Coursera.
