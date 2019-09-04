# Autonomous RC Car

In this project, I built an autonomous RC car using Raspberry Pi, a Pi Camera, and a [toy-grade RC car](https://www.ebay.com/itm/R-C-Tech-Brix-Remote-Control-Customize-Body-w-Lego-Mega-Bloks-Any-Brick-System-/183036421261) (I found this for $5 at a dollar store.)

## Materials Needed
- Raspberry Pi (Wi-Fi capable, such as RPi 3 Model B)
- Pi Camera
- RC car that runs on a MhZ (not GhZ) frequency

In order to control the RC, the [pi-rc](https://github.com/bskari/pi-rc) library was used to turn the Raspberry Pi into a radio-frequency transmitter. Python functions for basic directional control are contained in `rccontrol.py`. In order to send commands successfully with `rccontrol.py`, one must simultaneously run `make` and `sudo ./pi_pcm -v` in the `pi-rc` folder.

A multi-layer perceptron (MLP) neural network classifier was implemented using [scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier). I used two hidden layers of size 100 (possibly overkill, but not prohibitively so.) The network takes as input the flattened, grayscaled contents of a Pi Camera image, and classifies the images into one of four output directions: forward, left, right, or reverse. For training, the car should be driven through a track of some sort (I used paper for the lanes.)

Before being input to the neural network, the images are grayscaled, cut in half (only the bottom half really contains useful info,) reduced to 288 x 96 px resolution, and flattened into a one-dimensional array.

In test mode, the program continually takes a picture and chooses the most probable direction to go: either forward, left, right, or reverse.

[![Autonomous car](https://img.youtube.com/vi/bulzQxh9DlI/maxresdefault.jpg)](https://www.youtube.com/watch?v=bulzQxh9DlI)

## Thanks
Libraries used:

https://github.com/bskari/pi-rc

http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier


Inspiration for the neural net architecture:
http://blog.davidsingleton.org/nnrccar/
