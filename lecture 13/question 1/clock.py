from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np
import pytz

# Initialization, define some constants
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
gmt_hand_length = 80
gmt_hand_width = 4
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()
ax.axis("off")

plt.imshow(background)

# Initial draw of clock hands
local_time = datetime.now()
gmt_time = datetime.now(pytz.timezone('UTC'))

hour = local_time.hour if local_time.hour <= 12 else local_time.hour - 12
minute = local_time.minute
second = local_time.second
gmt_hour = gmt_time.hour

hour_vector = clock_hand_vector(hour / 12 * 2 * np.pi, hour_hand_length)
minute_vector = clock_hand_vector(minute / 60 * 2 * np.pi, minute_hand_length)
second_vector = clock_hand_vector(second / 60 * 2 * np.pi, second_hand_length)
gmt_vector = clock_hand_vector(gmt_hour / 24 * 2 * np.pi, gmt_hand_length)

hour_hand = plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length=3, linewidth=hour_hand_width, color='black')
minute_hand = plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth=minute_hand_width, color='black')
second_hand = plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth=second_hand_width, color='red')
gmt_hand = plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], linewidth=gmt_hand_width, color='yellow')

while True:
    local_time = datetime.now()
    gmt_time = datetime.now(pytz.timezone('UTC'))

    hour = local_time.hour if local_time.hour <= 12 else local_time.hour - 12
    minute = local_time.minute
    second = local_time.second
    gmt_hour = gmt_time.hour

    # Calculate new end points of hour, minute, second, GMT
    hour_vector = clock_hand_vector(hour / 12 * 2 * np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute / 60 * 2 * np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second / 60 * 2 * np.pi, second_hand_length)
    gmt_vector = clock_hand_vector(gmt_hour / 24 * 2 * np.pi, gmt_hand_length)

    # Update the arrow objects
    hour_hand.remove()
    minute_hand.remove()
    second_hand.remove()
    gmt_hand.remove()

    hour_hand = plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length=3, linewidth=hour_hand_width, color='black')
    minute_hand = plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth=minute_hand_width, color='black')
    second_hand = plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth=second_hand_width, color='red')
    gmt_hand = plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], linewidth=gmt_hand_width, color='yellow')

    plt.pause(0.1)
