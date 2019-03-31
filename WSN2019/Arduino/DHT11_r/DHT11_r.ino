#define Pin  2

float temperature = 0;
float humidity = 0;

int read_dht(int pin)
{  
  // BUFFER TO RECEIVE
  uint8_t bits[5];
  uint8_t cnt = 7;
  uint8_t idx = 0;

  // EMPTY BUFFER
  for (int i=0; i< 5; i++) bits[i] = 0;

  // REQUEST SAMPLE
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW);
  delay(18);
  digitalWrite(pin, HIGH);
  delayMicroseconds(40);
  pinMode(pin, INPUT);

  // ACKNOWLEDGE or TIMEOUT
  unsigned int loopCnt = 80;
  while(digitalRead(pin) == LOW)
  {
    delayMicroseconds(1);
    if (loopCnt-- < 0) return -1;
  }

  loopCnt = 80;
  while(digitalRead(pin) == HIGH)
  {
    delayMicroseconds(1);
    if (loopCnt-- < 0) return -1;
  }

  //READ DATA: 40bit = 5bytes
  for (int i=0; i<40; i++)
  {
    loopCnt = 50;
    while(digitalRead(pin) == LOW)
    {
      delayMicroseconds(1);      
      if (loopCnt-- < 0) return -1;
    }
    unsigned long t = micros();
    while(digitalRead(pin) == HIGH){}
      
    if ((micros() - t) > 40) bits[idx] |= (1 << cnt);
    if (cnt == 0) 
    {
      cnt = 7;
      idx++;
    }
    else cnt--;
  }

  humidity = float(bits[0]) + float(bits[1])/100;
  temperature = float(bits[2]) + float(bits[3])/100;
  Serial.print(humidity);
  Serial.print(temperature);
  
  uint8_t sum = bits[0] + bits[1] + bits[2] + bits[3];  

  if (bits[4] != sum) return -2;
  return 0;
}

void setup() {
  Serial.begin(115200);
}
 
void loop() {
  yield();
  delay(1);
  int message = read_dht(Pin);
  if (message == -1) Serial.println("Error Timeout");   
  else if (message == -2) Serial.println("Error Checksum");
  else
  {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" *C");
    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");
    Serial.println("------------------------------------");
  }
  Serial.println("");
  delay(1000);                     
}
