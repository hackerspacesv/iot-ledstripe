# IoT LED Stripe Controller v0.1
# UDP Server to display MIDI events mapped to the LED Stripe
# Copyright 2015. Mario Gómez <mario _dot_ gomez -at- teubi.co>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License.
#
#  This program is distributed in the hope that it will be useful, but 
#  WITHOUT ANY WARRANTY; without even the implied warranty of 
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License 
#  along with this program.  If not, see 
#  <http://www.gnu.org/licenses/>.

import sys, pygame, pygame.midi
import socket

UDP_IP = "192.168.1.99"

UDP_PORT = 1337

sock = socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM) # UDP

# set up pygame
pygame.init()
pygame.midi.init()

# list all midi devices
for x in range( 0, pygame.midi.get_count() ):
   print pygame.midi.get_device_info(x)

# open a specific midi device
inp = pygame.midi.Input(1)

# run the event loop
try:
        while True:
          if inp.poll():
            # no way to find number of messages in queue
            # so we just specify a high max value
            payload = ""
            for val in inp.read(1000):
              print val
              bytes = []
              if val[0][0]==128:
                bytes = [(val[0][1]-36)*2, 0, 0, 0]
              if val[0][0]==144:
                bytes = [(val[0][1]-36)*2, val[0][2]*2, val[0][2]*2, val[0][2]*2]
              payload = payload + "".join(map(chr, bytes))
              if val[0][0]==128:
                bytes = [(val[0][1]-36)*2+1, 0, 0, 0]
              if val[0][0]==144:
                bytes = [(val[0][1]-36)*2+1, val[0][2]*2, val[0][2]*2, val[0][2]*2]
              payload = payload + "".join(map(chr, bytes))
            sock.sendto(payload,(UDP_IP, UDP_PORT))
          # wait 10ms - this is arbitrary, but wait(0) still resulted
          # in 100% cpu utilization
          pygame.time.wait(10)
except KeyboardInterrupt:
  print "adios :) "
  packet  = [None] * 480 # Full LED Stripe
  for a in range(120):
    packet[(a*4)]=a;
    packet[(a*4)+1]=0
    packet[(a*4)+2]=0
    packet[(a*4)+3]=0
  payload = "".join(map(chr, packet))
  sock.sendto(payload,(UDP_IP, UDP_PORT))
