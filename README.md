# Autonomous RC Car

In this project, I built an autonomous RC car using Raspberry Pi, a Pi Camera, and a [toy-grade RC car](https://www.ebay.com/itm/R-C-Tech-Brix-Remote-Control-Customize-Body-w-Lego-Mega-Bloks-Any-Brick-System-/183036421261) (I found this for $5 at a dollar store.)

## Materials
- Raspberry Pi (Wi-Fi capable, such as RPi 3 Model B)
- Pi Camera
- RC car that runs on 27 or 49 MHz band

## Setup
In order to control the RC, the [pi-rc](https://github.com/bskari/pi-rc) library was used to turn the Raspberry Pi into a radio-frequency transmitter. Python functions for basic directional control are contained in `rccontrol.py`. To set up RC control, do the following from the command line on your Raspberry Pi:

  git clone https://github.com/bskari/pi-rc
  cd pi-rc
  make
  sudo ./pi_pcm -v
  python3 host_files.py
 
See https://github.com/bskari/pi-rc for more information on how the RC commands are formatted, and troubleshooting.

## Data Collection & Training

In order to train the neural network, you must run `collectData()` in [rctrain.py](https://github.com/ketan0/selfdriving-rc/blob/master/rctrain.py), which allows you to incrementally move the car through a paper track, recording a picture and the direction traveled at each timestep.

Before being input to the neural network, the images are grayscaled, cut in half (only the bottom half really contains useful info,) reduced to 288 x 96 px resolution, and flattened into a one-dimensional array.

## Testing

In order to run the car in test mode, run `rctest.py`. In test mode, the program continually takes a picture and passes it through the trained neural network to choose the most probable direction to go: either forward, left, right, or reverse.

## Demo
[![Autonomous car](https://img.youtube.com/vi/bulzQxh9DlI/maxresdefault.jpg)](https://www.youtube.com/watch?v=bulzQxh9DlI)

## Thanks
Libraries used:

https://github.com/bskari/pi-rc

http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier


Inspiration for the neural net architecture:
http://blog.davidsingleton.org/nnrccar/
