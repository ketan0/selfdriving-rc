import json
import socket
import time
import copy
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 12345 #default socket used by pi-rc code.

# frequency repeats specific to Tech Brix R/C car.
#These may work for some other 27 MHz cars;
#see pi-rc documentation for details on finding
#an RC car's control parameters.
command_repeats = {
    "forward" : 11,
    "left" : 59,
    "forward_left" : 27,
    "right" = 64,
    "forward_right" : 33,
    "reverse" : 39,
    "reverse_left" : 51,
    "reverse_right" : 45,
    "stop" : 0
}


default_command = [
    {
        "frequency": 26.995,
        "dead_frequency": 49.830,
        "burst_us": 1200,
        "spacing_us": 400,
        "repeats": 4
    },
    {
        "frequency": 26.995,
        "dead_frequency": 49.830,
        "burst_us": 400,
        "spacing_us": 400,
        "repeats": 0
    }
]

stop_command = [
    {
        "frequency": 26.995,
        "dead_frequency": 49.830,
        "burst_us": 1200,
        "spacing_us": 400,
        "repeats": 4
    }
]

#Set up the Pi to be ready to listen for JSON-formatted commands.
os.system("sudo pi-rc/pi_pcm -v")

#broadcast a command using the defined-above constants
#sendCommand('forward'), sendCommand('stop'), etc.
def sendCommand(command_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command = copy.deepcopy(default_command)
    command[1]["repeats"] = command_repeats.get(command_name, "stop")
    s.send(json.dumps(command))
    s.close()

#make a short movement in the specified direction, then stop.
#goDirection('forward'), goDirection('stop'), etc.
def goDirection(command_name):
    sendCommand(command_name)
    time.sleep(0.1)
    sendCommand('stop')

#may be useful to produce a quicker stop.
def brake():
    sendCommand('reverse')
    time.sleep(0.3)
    sendCommand('stop')

#ensure all commands work properly.
def test():
    for command_name in command_repeats:
        sendCommand(command_name)
        time.sleep(2)
