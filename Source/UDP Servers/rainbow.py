# IoT LED Stripe Controller v0.1
# UDP Server to display rainbow colors on the stripe
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

import sys, pygame
import socket, math

UDP_IP = "192.168.1.99"

UDP_PORT = 1337

sock = socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM) # UDP

# run the event loop
packet  = [None] * 480 # Full LED Stripe
rainbow = [None] * 360

gammaR = [None] * 181
gammaG = [None] * 181
gammaB = [None] * 181

for i in range(0,181):
  gammaR[i] = int(round(25 * math.pow(i/181.0, 1/0.75)))
  gammaG[i] = int(round(25 * math.pow(i/181.0, 1/0.50)))
  gammaB[i] = int(round(25 * math.pow(i/181.0, 1/0.40)))


# Pre-Compute rainbow
rVal = 0
rDir = 1
gVal = 120
gDir = 0
bVal = 120
bDir = 1

for i in range(0,120):
  rainbow[(i*3)+0] = rVal
  rainbow[(i*3)+1] = gVal
  rainbow[(i*3)+2] = bVal

  if rDir == 1:
    rVal = rVal + 3
    if rVal > 180:
      rDir = 0
      rVal = 180
  else:
    rVal = rVal - 3
    if rVal < 0:
      rDir = 1
      rVal = 0

  if gDir == 1:
    gVal = gVal + 3
    if gVal > 180:
      gDir = 0
      gVal = 180
  else:
    gVal = gVal - 3
    if gVal < 0:
      gDir = 1
      gVal = 0

  if bDir == 1:
    bVal = bVal + 3
    if bVal > 180:
      bDir = 0
      bVal = 180
  else:
    bVal = bVal - 3
    if bVal < 0:
      bDir = 1
      bVal = 0

step = 0
while True:
  for i in range(0,120):
    rainbowPos = i+step%120
    if rainbowPos > 119:
      rainbowPos = rainbowPos-120
    packet[(i*4)+0] = i
    packet[(i*4)+1] = gammaR[rainbow[(rainbowPos*3)+0]]
    packet[(i*4)+2] = gammaG[rainbow[(rainbowPos*3)+1]]
    packet[(i*4)+3] = gammaB[rainbow[(rainbowPos*3)+2]]
  payload = "".join(map(chr, packet))
  sock.sendto(payload,(UDP_IP, UDP_PORT))
  pygame.time.wait(25)
  step = step + 1
