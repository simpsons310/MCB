int measurePin = A0;
int ledPower = 2;
 
int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;
 
float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;
 
void setup(){
  Serial.begin(115200);
  pinMode(ledPower,OUTPUT);
}
 
void loop(){
  digitalWrite(ledPower,LOW); 
  delayMicroseconds(samplingTime);  
  voMeasured = analogRead(measurePin); 
  delayMicroseconds(deltaTime);
  digitalWrite(ledPower,HIGH); 
  delayMicroseconds(sleepTime); 
 
  calcVoltage = voMeasured * (3.3/ 1024); 
  dustDensity = 0.17 * calcVoltage - 0.1;
 
 
  Serial.print("Raw Signal Value (0-1023): ");
  Serial.println(voMeasured);
  Serial.print(" Voltage: ");
  Serial.println(calcVoltage);
  Serial.print(" Dust Density: ");
  Serial.println(dustDensity);
  delay(2000);
}
