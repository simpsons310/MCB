#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include "DHT.h"
#include "SharpGP2Y10.h"
#include "index.h"

#define MUXA 5
#define MUXB 4
#define ANALOG A0
#define DUSTD 14
#define DHTPIN 12
#define DHTTYPE DHT11   
#define LED 2
DHT dht(DHTPIN, DHTTYPE);
SharpGP2Y10 dustSensor(ANALOG, DUSTD,3.3);

//const char* ssid = "FPT_2";
//const char* password = "abcd1234";
//const char* ssid = "CangTmin2";
//const char* password = "giang115";
const char* ssid = "tang_2";
const char* password = "12345679";


ESP8266WebServer server(80);

void handleRoot() {
 String s = MAIN_page; //Read HTML contents
 server.send(200, "text/html",s); //Send web page
}

void handleData(){
 float hum = dht.readHumidity();
 float temp = dht.readTemperature();
 delay(10);
 digitalWrite(MUXA,LOW);
 digitalWrite(MUXB,HIGH);
 float light1 = analogRead(ANALOG);
 delay(10);
 digitalWrite(MUXA,HIGH);
 digitalWrite(MUXB,LOW);
 float light2 = analogRead(ANALOG);
 delay(10);
 digitalWrite(MUXA,LOW);
 digitalWrite(MUXB,LOW);
 float dust = dustSensor.getDustDensity();
 delay(10);
 String s = String(hum) +"#"+ String(temp) +"#"+ String(light1) +"#"+ String(light1) +"#"+ String(dust) + "#";
 server.send(200, "text/plane", s);
}

void handleLED() {
 String ledState = "OFF";
 String t_state = server.arg("LEDstate"); //Refer  xhttp.open("GET", "setLED?LEDstate="+led, true);
 Serial.println(t_state);
 if(t_state == "ON"){
  digitalWrite(LED,LOW); //LED ON
  ledState = "OFF"; //Feedback parameter
 }else{
  digitalWrite(LED,HIGH); //LED OFF
  ledState = "ON"; //Feedback parameter  
 }
 server.send(200, "text/plane", ledState); //Send web page
}

void setup() {
  Serial.begin(115200); 
  pinMode(MUXA,OUTPUT);
  pinMode(MUXB,OUTPUT);
  pinMode(LED,OUTPUT);
  dht.begin();
  WiFi.begin(ssid, password);
  Serial.println("");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
 
  server.on("/", handleRoot);
  server.on("/setLED", handleLED);
  server.on("/data", handleData);

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
