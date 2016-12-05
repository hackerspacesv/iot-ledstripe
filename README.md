# IoT WS8211 LED Stripe Controller
This is a simple OpenSource-Hardware project to control WS2811 LEDs stripes using only a ESP8266 and a Android cellphone or tablet.

The project is just a proof-of-concept to demonstrate the capabilities of the ESP8266 module on it most basic form-factor and with a minimum of external hardware.

## What's on this repository
We tried to include all the basic pieces to build and run this project. This are the project folders an it's contents:

1. *Arduino*: Contains the sketch used with the ESP8266. The sketch **LEDStripeIoT** sets-up a small web server and also controls the LED stripe. The sketch **UDPLEDStripe** listen for UDP packets to change the LED colors.
2. *AppInventor*: Includes the MIT's App Inventor project file that you can use as a template to control the LED stripe from Android.
3. *Fritzing*: This contains a fritzing project to help you to connect all the pieces together.
3. *Source*: Contains Python 2.7 examples to send UDP packets when using the UDPLEDStripe sketch.

## Materials (BOM)
To build this project you'll need at least this components:
* ESP8266-01
* Voltage Level Converter
* 3.3V linear Regulator
* 5V@4A voltage source
* WS2811 RGB LED stripe.

To program the ESP8266 you'll also need:
* FTDI USB<->Serial converter working at 3.3V

## How to use it
* Edit the Arduino Sketch and modify the options for wireless access and static IP address to use:

```c++
/* Agrega el nombre y clave de acceso de tu red inalambrica*/
#define SSID "Manda internet al 2020" // Network name (between quotes)
#define PW "nohayinternet" // Password (between quotes)

/* Cambia la configuración IP de tu red local */
#define LOCALIP "192.168.0.226" // String for the local server configuration 
IPAddress ip_addr(192,168,0,126); // Static IP to use
IPAddress gw(192,168,0,1); // Default gateway
IPAddress netmask(255,255,255,0); // Netmask

/* PIN de la tira de LED */
#define PIN 2 // Pin for RGB LED stripe
#define STRIP_SIZE 60 // Number of LEDs
```
* Upload your Sketch to the ESP8266, this Sketch also requires the Adafruit's NeoPixel library https://github.com/adafruit/Adafruit_NeoPixel (1)
* Connect everything as shown on the Fritzing project file.
* Install the App RemoteRGBTest.apk included on "AppInventor/binaries". If you don't trust me download the "aia" Project for MIT App Inventor and compile the APK from there
* Power everything up and cross your fingers
* If you are still alive and nothing was burn in the process open the App in your cellphone and specify the IP address of the module. To change colors use the sliders and click on "Send color" when ready
* Have fun

(1) Here is a really good tutorial if you don't know how to do it: http://makezine.com/2015/04/01/installing-building-arduino-sketch-5-microcontroller/

A detailed tutorial (in Spanish) can be found at http://blog.teubi.co/2015/12/Tira-LED-IoT.html

## Who are you and where can I find more projects like this?
TeUbi.co is an electronic component store based in El Salvador, a small but beautiful country in Central Americas.

To find more projects like this you can follow us on any (or all) of this social networks:

https://www.facebook.com/tiendateubico

https://www.instagram.com/teubico

http://blog.teubi.co/

https://twitter.com/teubico

https://www.youtube.com/tiendateubico

## Copyrights
IoT LED Stripe Controller v0.1
Copyright 2015. Mario Gómez <em>mario -dot- gomez -at- teubi.co</em>

http://blog.teubi.co

For source files if not specified on the header:
```
IoT LED Stripe Controller v0.1
Copyright 2015. Mario Gómez <mario _dot_ gomez -at- teubi.co>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License.

    This program is distributed in the hope that it will be useful, but 
    WITHOUT ANY WARRANTY; without even the implied warranty of 
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
    General Public License for more details.

    You should have received a copy of the GNU General Public License 
    along with this program.  If not, see 
    <http://www.gnu.org/licenses/>.
```

For design files (EAGLE, Fritzing, MIT App Inventor project files, images and renders):
```
IoT LED Stripe Controller v0.1
Copyright 2015.  Mario Gómez <mario _dot_ gomez -at- teubi.co>
Distributed under CC-BY License version 3.0

Summary:

You are free to:
    Share — copy and redistribute the material in any medium or format.
    Adapt — remix, transform, and build upon the material for any
    purpose, even commercially.
    The licensor cannot revoke these freedoms as long as you follow the
    license terms.

Under the following terms:
    Attribution — You must give appropriate credit, provide a link to
    the license, and indicate if changes were made. You may do so in any
    reasonable manner, but not in any way that suggests the licensor
    endorses you or your use.
    No additional restrictions — You may not apply legal terms or
    technological measures that legally restrict others from doing
    anything the license permits.

Notices:
    You do not have to comply with the license for elements of the
    material in the public domain or where your use is permitted by an
    applicable exception or limitation.
    No warranties are given. The license may not give you all of the
    permissions necessary for your intended use. For example, other
    rights such as publicity, privacy, or moral rights may limit how you
    use the material.

Full License: https://creativecommons.org/licenses/by/3.0/us/legalcode
```
