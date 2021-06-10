#include <Bridge.h>

#define SENSOR_PIN_1 2
#define SENSOR_PIN_2 3

void setup()
{
  Bridge.begin();
  pinMode(SENSOR_PIN_1,INPUT);  
  pinMode(SENSOR_PIN_2,INPUT);  
}

void loop()
{
  delay(100);
  int value1 = digitalRead(SENSOR_PIN_1);
  int value2 = digitalRead(SENSOR_PIN_2);
  String dataString = String(value1) + "/" + String(value2);
  Bridge.put("WH_DATA", dataString);
}
