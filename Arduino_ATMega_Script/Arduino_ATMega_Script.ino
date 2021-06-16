// Include library for hardware bridge communication
#include <Bridge.h>

// Define pin numbers for sensor.

// Contact sensor
#define SENSOR_PIN_1 2

// Non-contact sensor
#define SENSOR_PIN_2 3

// Initialization procedure
void setup()
{
  // Srart hardware sbirdge communication
  Bridge.begin();

  // Configure hareware port
  pinMode(SENSOR_PIN_1, INPUT);
  pinMode(SENSOR_PIN_2, INPUT);
}

// Routine procedure
void loop()
{
  // Wait for 100ms = 0.1s
  delay(100);

  // Read binary value (on/off) from (hardware) port
  int value1 = digitalRead(SENSOR_PIN_1);
  int value2 = digitalRead(SENSOR_PIN_2);

  // Convert value to string and concatenate to send it via bridge
  String dataString = String(value1) + "/" + String(value2);

  // Send stringified data via hardware birdge
  Bridge.put("WH_DATA", dataString);
}
