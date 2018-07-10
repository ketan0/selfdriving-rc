import json
import socket
import time
import copy

TCP_IP = '127.0.0.1'
TCP_PORT = 12345

forward = 11
left = 59
forward_left = 27
right = 64
forward_right = 33
reverse = 39
reverse_left = 51
reverse_right = 45
stop = 0

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

def sendCommand(repeats):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    if repeats:
        command = copy.deepcopy(default_command)
        command[1]["repeats"] = repeats
    else:
        command = copy.deepcopy(stop_command)
    s.send(json.dumps(command))
    s.close()

def goDirection(command):
    sendCommand(command)
    time.sleep(0.1)
    sendCommand(stop)

def brake():
    sendCommand(reverse)
    time.sleep(0.5)
    sendCommand(stop)

def test():
    sendCommand(forward)
    time.sleep(2)
    sendCommand(reverse)
    time.sleep(2)
    sendCommand(left)
    time.sleep(2)
    sendCommand(right)
    time.sleep(2)
    sendCommand(forward_left)
    time.sleep(2)
    sendCommand(reverse_left)
    time.sleep(2)
    sendCommand(forward_right)
    time.sleep(2)
    sendCommand(reverse_right)
    time.sleep(2)
    sendCommand(stop)
