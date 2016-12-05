#include <ESP8266WiFi.h>
#include <WiFiUDP.h>
#include <Adafruit_NeoPixel.h>

#define PIN 2
#define PIXELS 120

#define UDP_BUFF_SIZE 512
byte packetBuffer[512];

Adafruit_NeoPixel strip = 
  Adafruit_NeoPixel(PIXELS, PIN, NEO_GRB + NEO_KHZ800);

const char* ssid = ""; // WiFI SSID
const char* pass = ""; // WiGI Password

unsigned int localPort = 1337;

IPAddress ip_addr(192,168,1,99);
IPAddress gw(192,168,1,1);
IPAddress netmask(255,255,255,0);

WiFiUDP Udp;


void setup() {
  strip.begin();
  strip.show();

  WiFi.config(ip_addr,gw,netmask);
  WiFi.begin(ssid, pass);

  Serial.begin(115200);
  Serial.println("Turning LEDs OFF");
  
  Serial.print("[Connecting]");
  Serial.print(ssid);
  int tries=0;
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    tries++;
    if (tries > 30){
      break;
    }
    ESP.wdtFeed();
  }

  Udp.begin(localPort);
}

void loop() {
  int packet_size = Udp.parsePacket();
  int color[3] = {0,0,0};
  uint8_t pixels = packet_size/4;

  if(packet_size>0 && packet_size<UDP_BUFF_SIZE && !(packet_size & 0x03)) {
    Udp.read(packetBuffer,packet_size);
    
    for(uint8_t i; i<pixels; i++) {
      color[0] = packetBuffer[(i*4)+1];
      color[1] = packetBuffer[(i*4)+2];
      color[2] = packetBuffer[(i*4)+3];
      strip.setPixelColor(
        packetBuffer[(i*4)], 
        strip.Color(color[0], color[1], color[2]));
      ESP.wdtFeed();
    }

    strip.show();
  }
}
