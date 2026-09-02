#include <WiFiUdp.h>

WiFiUDP udp;
// IPAddress destIP(192,168,1,100);  // your laptop
IPAddress destIP(192,168,10,102);
const uint16_t destPort = 12345;
uint8_t packet[40];
long cap_vals[8] = {0};

void setup() {
  delay(500);
  Serial.begin(115200);

  Serial.println("");
  Serial.println("Attempting Ethernet Setup...");
  ethernet_init();

  Serial.println("Attempting Sensing Setup...");
  sensing_setup();
}

void loop() {
  take_measurements(cap_vals);
  uint64_t t = millis();
  memcpy(packet, &t, sizeof(t));
  // Serial.print(t);
  // Serial.print(" ");
  // Serial.print(sizeof(t));
  // Serial.print(" ");

  // for (long cap : cap_vals) {
  //   Serial.print(cap);
  //   Serial.print(" ");
  // }
  // Serial.println();



  for (int i = 0; i<8; i++) {
    memcpy(packet + 8 + i * sizeof(long), &cap_vals[i], sizeof(long));
  }

  udp.beginPacket(destIP, destPort);
  // udp.print("hello from esp32\n");
  udp.write(packet, sizeof(packet));
  udp.endPacket();

  // delay(500);
}
