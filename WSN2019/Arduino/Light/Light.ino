#define digital_in 2
#define analog_in A0

void setup (){

  pinMode(digital_in,INPUT);
  pinMode(analog_in,INPUT);
  Serial.begin(9600);
  
}

void loop (){

   int digital_value = digitalRead(analog_in);
   int analog_value = analogRead(analog_in);
   Serial.println(digital_value);
   Serial.println(analog_value);
   Serial.println();
   delay(1000);
}
