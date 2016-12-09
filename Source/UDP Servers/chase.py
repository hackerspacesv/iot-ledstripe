# IoT LED Stripe Controller v0.1
# UDP Server to display a chase-light
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

import sys, pygame, socket

UDP_IP = "192.168.1.99"
UDP_PORT = 1337

sock = socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM) # UDP

packet = [None] * 480

step = 0
try:
        while True:
          for i in range(0,120):
            packet[(i*4)+0] = i
            packet[(i*4)+1] = 0
            packet[(i*4)+2] = 0
            packet[(i*4)+3] = 0
            if i == step:
              packet[(i*4)+1] = 25
              packet[(i*4)+2] = 0
              packet[(i*4)+3] = 0

          step = step + 1
          if step > 119:
            step = 0

          payload = "".join(map(chr, packet))

          sock.sendto(payload,(UDP_IP, UDP_PORT))

          pygame.time.wait(25)

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
