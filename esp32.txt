#include <WiFi.h>
#include <HTTPClient.h>
#include <SoftwareSerial.h>
SoftwareSerial ss(4, 3);

const char* ssid = "No Internet";
const char* password = "abcdefgh";
String GOOGLE_SCRIPT_ID = "AKfycbyY0rYxiLoYppMUElMJ6OxrkASb0NORlsqELCQNiRcWg7FDSGrNKFfpCpo0JQGMrMQv";

HTTPClient http;
//Configuring the http client

void setup() {
  Serial.begin(9600);
  ss.begin(9600);
  //Connecting to Wifi
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  Serial.println("Connected to Wifi");

  
  
}

void loop(){
 {
  byte gpsData = ss.read();

  String urlFinal = "https://script.google.com/macros/s/"+GOOGLE_SCRIPT_ID+"/exec?id=Sensor_1&value="+ String(gpsData);
  Serial.println("POSTing data to spreadsheet:");
  http.begin(urlFinal.c_str());
  http.setFollowRedirects(HTTPC_STRICT_FOLLOW_REDIRECTS);
  int httpCode = http.GET(); 
  Serial.print("HTTP Status Code: ");
  Serial.println(httpCode);
  delay(10000);
 }
}
