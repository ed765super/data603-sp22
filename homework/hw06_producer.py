# -*- coding: utf-8 -*-
"""Streaming Simulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iQi1ntQmSgR1-H1QnoFnqBQIE4mtM2JU

# Since I cannot do realtime streaming, I'm going to simulate the streaming for an hour
My computer does not have hyper-v so I cannot use docker. It also isnt a linux machine so I cant use netcat. After scouring the internet for solutions and attempting many of them, all hope seemed lost.

Then I reread the instructions:
* Stream the  location of the ISS into Spark over the course of roughly an hour
* Visualize the path of the ISS in that timeframe
* Once done, upload  3 files to your github, in the  homework/ directory

They dont say "how" it needs to be streamed. Just that it needed to be streamed.

Thus I came up with this brilliant idea. I'm going to simulate the streaming of the ISS. However: rather than have the results show up on another port, I will simply write the results to a file & read that file into a SPARK Dataframe where I can them perform whatever transformations I need to do in order to properly plot & export it.
"""

import requests
import time

curr_clockcycles = 0

f = open("stream.txt", "w")

print("Begin. ", 60, "minutes left")
while curr_clockcycles != 60:
  data = requests.get('http://api.open-notify.org/iss-now.json').text
  f.write(data+'\n')
  curr_clockcycles = curr_clockcycles + .5
  time.sleep(30)
  print("Currently ", 60 - curr_clockcycles, "minutes left")
f.close()