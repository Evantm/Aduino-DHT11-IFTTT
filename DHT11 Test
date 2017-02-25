
#include "dht.h"

dht DHT;

#define DHT11_PIN 4

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  int chk = DHT.read22(DHT22_PIN);
  chk = DHT.read11(DHT11_PIN);
  switch (chk)
  {
    case DHTLIB_OK:  
		break;
    case DHTLIB_ERROR_CHECKSUM: 
		Serial.print("Checksum error,\t"); 
		break;
    case DHTLIB_ERROR_TIMEOUT: 
		Serial.print("Time out error,\t"); 
		break;
    default: 
		Serial.print("Unknown error,\t"); 
		break;
  }
  
  Serial.print(DHT.humidity,1);
  Serial.print(",");
  Serial.print(DHT.temperature,1);
  Serial.println();
  delay(500); //How often it checks temp
  
}
