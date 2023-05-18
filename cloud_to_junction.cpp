/*  Project : Read Google Spread Sheet Data from ESP32  */
/*Refer following video for complete project : https://youtu.be/0LoeaewIAdY*/



/****************************/
//Things to change


#include <WiFi.h>
#include <HTTPClient.h>

#include <Wire.h>


const char * ssid = "Rahul";
const char * password = "rahulnote10s";
String GOOGLE_SCRIPT_ID = "AKfycbyQwuel6RUsje7t793ao2yIxfXHRz8fW1jV4523gelsSJBgH9O7m69rzYzUJGbuOmMelQ";

const int sendInterval = 5000; 
/****************************/

WiFiClientSecure client;

void spreadsheet_comm(void) {
   HTTPClient http;
   String url="https://script.google.com/macros/s/"+GOOGLE_SCRIPT_ID+"/exec?read";
//   Serial.print(url);
  Serial.print("Making a request");
  http.begin(url.c_str()); //Specify the URL and certificate
  http.setFollowRedirects(HTTPC_STRICT_FOLLOW_REDIRECTS);
  int httpCode = http.GET();
  String payload;
    if (httpCode > 0) { //Check for the returning code
        payload = http.getString();

        Serial.println(httpCode);
        Serial.println(payload);
      }
    else {
      Serial.println("Error on HTTP request");
    }
  http.end();
}

void setup() {
  Serial.begin(9600);
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println("Started");
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

Serial.println("Ready to go");
}

void loop() {
  spreadsheet_comm();
  delay(sendInterval);
}