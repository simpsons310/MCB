#include <ESP8266WiFi.h>

//const char* ssid = "CangTin2";
//const char* password = "giang115";
//
//const char* ssid = "duong22";
//const char password = "06111985";
//
const char * ssid = "FPT_2";
const char* password = "abcd1234";

WiFiServer server(80);

void setup(void)
{
  Serial.begin(115200);
  Serial.println();
  
  Serial.printf("Connecting to %s \n", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
  Serial.println("Khoi dong Server");
 
}

void loop() 
{
  WiFiClient client = server.available();
  int t = micros();
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
  s += "<head>";
  s += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">";
  s += "<meta http-equiv=\"refresh\" content=\"60\" />";
  s += "<script src=\"https://code.jquery.com/jquery-2.1.3.min.js\"></script>";
  s += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css\">";
  s += "<style>body{font-size: 24px;} .voffset {margin-top: 30px;}</style>";
  s += "</head>";
  s += "<div class=\"container\">";
  s += "<h1>Theo doi nhiet do va do am</h1>";
  s += "<div class=\"row voffset\">";
  s += "<div class=\"col-md-3\">Thoi gian: </div><div class=\"col-md-3\">" + String(t) + "</div>";
  s += "</div>";
  client.print(s);
  delay(1);
  Serial.println("Client da thoat");
}
