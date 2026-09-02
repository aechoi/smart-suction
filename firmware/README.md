# End-effector firmware

Firmware for the smart suction cup end effector. Reads eight capacitance
channels from an AD7746 CDC (multiplexed through GPIO switches) and streams
them over UDP/Ethernet to a host PC running `software/` `udp_receiver.py`.

## Target

- **MCU:** ESP32 with a LAN8720 Ethernet PHY (e.g. WT32-ETH01 / Olimex
  ESP32-POE). RMII pins are set in `ethernet.ino`
  (`MDC=23`, `MDIO=18`, `CLK=GPIO0`, `POWER=-1`).
- **Sensor:** AD7746 capacitance-to-digital converter on I2C
  (`SDA=32`, `SCL=33`, `RDY=36`, address `0x48`), with 8 channels selected
  one at a time via the switch pins in `sensing.ino`.

## Toolchain

Arduino IDE (or `arduino-cli`) with the **esp32 by Espressif** board package.
No external libraries — `ETH.h`, `WiFiUDP.h`, and `Wire.h` all ship with the
core.

The three files form one sketch (`firmware.ino` holds `setup()` / `loop()`;
`ethernet.ino` and `sensing.ino` are additional tabs). Arduino requires the
main file to match the folder name, hence `firmware.ino` in `firmware/`.

## Network configuration

Edit before flashing:

| Where | Constant | Meaning |
|-------|----------|---------|
| `firmware.ino` | `destIP`, `destPort` | host PC address + UDP port (default `12345`) |
| `ethernet.ino` | `localIP`, `gateway`, `subnet` | static IP of the end effector |

## Wire format

One 40-byte UDP packet per sample loop:

| Bytes | Type | Contents |
|-------|------|----------|
| 0–7   | `uint64` LE | `millis()` timestamp |
| 8–39  | 8 × `int32` LE | raw AD7746 counts, channels 0–7 |

Convert counts to femtofarads with `count2ff()` in `sensing.ino`
(`(counts - 208400) * (4.096 * 1000 * 2) / 2^24`).
