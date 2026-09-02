#include <ETH.h>

#define CONFIG_ETH_USE_ESP32_EMAC 1
#define ETH_PHY_TYPE  ETH_PHY_LAN8720
#define ETH_PHY_ADDR  0
#define ETH_PHY_POWER -1
#define ETH_PHY_MDC   23
#define ETH_PHY_MDIO  18
#define ETH_CLK_MODE  ETH_CLOCK_GPIO0

// IPAddress localIP(192,168,1,50);
IPAddress localIP(192,168,10,50);
IPAddress gateway(0,0,0,0);
IPAddress subnet(255,255,255,0);

void ethernet_init() {
  ETH.begin();
  ETH.config(localIP, gateway, subnet);

  while (!ETH.linkUp()) {
    delay(100);
  }

  udp.begin(12345);  // local source port (arbitrary)
}
