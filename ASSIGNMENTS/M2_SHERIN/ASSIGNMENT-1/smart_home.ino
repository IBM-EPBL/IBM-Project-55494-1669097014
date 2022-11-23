// C++ code
//
#define LED_PIN 12
int tempVal;
int sensorValue;
const int buzzer = 9;

void setup()
{
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop()
{
  sensorValue = analogRead(0);
  tempVal = analogRead(1);
  float volt = tempVal*(5.0/1024);
  float temp = (volt-0.5)*100;
  Serial.println("Temperature:");
  Serial.print(temp);
  Serial.print(" deg C");
  Serial.println("");
  Serial.print("Gas Sensor Value:");
  Serial.println(sensorValue, DEC);
  if (sensorValue>=500);
  	digitalWrite(LED_PIN,HIGH);
  	tone(buzzer,1000);
  	delay(1000);
  	noTone(buzzer);
    digitalWrite(LED_PIN,LOW);
  delay(1000);
}
