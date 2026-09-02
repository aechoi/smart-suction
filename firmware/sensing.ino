#include <Wire.h>

#define AD7746_ADDR 0x48  // 7-bit address

// AD7746 register map
#define REG_CAP_SETUP  0x07
#define REG_CONF       0x0A
#define REG_CAP_DATA_H 0x01
#define REG_STATUS     0x00
#define REG_EXC        0x09
#define REG_CAPDACA    0x0B
#define REG_CAPDACB    0x0C

// Pin Map
#define SENSE_1 2
#define SENSE_2 3
#define SENSE_3 4
#define SENSE_4 5
#define SENSE_5 13
#define SENSE_6 14
#define SENSE_7 15
#define SENSE_8 16
#define SDA_PIN 32
#define SCL_PIN 33
#define RDY_PIN 36

// IO Pin
// #define GROUND_TRUTH 13

volatile bool newDataReady = false;
const int numSamples = 1;

const int senseLength = 8;
const int sensePins[senseLength] = {SENSE_1, SENSE_2, SENSE_3, SENSE_4, SENSE_5, SENSE_6, SENSE_7, SENSE_8};

volatile long cap;

volatile bool actuating = false;

void sensing_setup() {
  Wire.begin(SDA_PIN, SCL_PIN);

  // pinMode(GROUND_TRUTH, INPUT);

  // Set switch pins
  for (int pin : sensePins) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
  }

  // Configure RDY pin interrupt on pin 2 (INT0)
  pinMode(RDY_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(RDY_PIN), rdyISR, FALLING);

  // Set up AD7746
  setupAD7746();

  delay(100);  // let it settle
}

void take_measurements(long* cap_vals) {
  /*
  Decide what electrode(s) to measure
  Apply switches to achieve that configuration
  Tell CDC to take a measurement
  Read the measurement
  Convert measurement to capacitance
  */
  // setMux(2);
  // delayMicroseconds(300);
  // writeRegister(REG_CONF, 0b00010010); // Request a single conversion sample
  // while (!newDataReady) {} // wait for interrupt
  // noInterrupts();
  // newDataReady = false;
  // interrupts();

  // for (int i = 0; i < senseLength; ++i){
  //   cap_vals[i] = readCapacitance();
  // }

  for (int i = 0; i < senseLength; ++i) {
    setMux(i);
    delayMicroseconds(300);    

    writeRegister(REG_CONF, 0b00010010); // Request a single conversion sample
    while (!newDataReady) {} // wait for interrupt
    noInterrupts();
    newDataReady = false;
    interrupts();

    cap_vals[i] = readCapacitance();
  }
}

void rdyISR() {
  newDataReady = true;
}

void setupAD7746() {
  // Cap setup: enable CAP1 positive input and VSS as negative reference
  writeRegister(REG_CAP_SETUP, 0b10000000);  // CIN1+, VSS

  // Configuration register: conversion rate, conversion type
  // writeRegister(REG_CONF, 0b00000010);  // CAP enabled, single conversion

  // configure excitation
  writeRegister(REG_EXC, 0b00001011);

  // CAPDAC A, essentially acts as an offset to move the zero point to get more usable range
  // writeRegister(REG_CAPDACA, 0b10111111);
  writeRegister(REG_CAPDACA, 0b00000000);

  // CAPDAC B, for single ended, keep zero
  writeRegister(REG_CAPDACB, 0b00000000);
}

long readCapacitance() {
  Wire.beginTransmission(AD7746_ADDR);
  Wire.write(REG_CAP_DATA_H);
  Wire.endTransmission(false);
  Wire.requestFrom(AD7746_ADDR, 3);

  byte msb = Wire.read();
  byte mid = Wire.read();
  byte lsb = Wire.read();

  long value = ((long)msb << 16) | ((long)mid << 8) | lsb;

  return value;
}

void writeRegister(byte reg) {
  Wire.beginTransmission(AD7746_ADDR);
  Wire.write(reg);
  Wire.endTransmission(false);
}
void writeRegister(byte reg, byte val) {
  Wire.beginTransmission(AD7746_ADDR);
  Wire.write(reg);
  Wire.write(val);
  Wire.endTransmission();
}

float count2ff(long counts) {
  return (counts - 208400) * (4.096 * 1000 * 2) / pow(2.0f, 24.0f);
}

void setMux(int switchIdx) {
  // expects a value between 0 and 7
  /*Set previous switch lo and current switch hi*/

  int prevPin = (switchIdx - 1 + 8) % 8;
  digitalWrite(sensePins[prevPin], LOW);
  digitalWrite(sensePins[switchIdx], HIGH);
}
