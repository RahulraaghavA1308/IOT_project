#include<WiFi.h>
#include<HTTPClient.h>

const char ss_id = "blank";
const char pwd= "abhipunda etha podu inga";
String Gscpt = " ";

WiFiClientSecure client;

void setup() {Serial.begin(9800);
WiFi.mode(WIFI_STA);
WiFi.begin(ss_id,pwd);


  pinMode(1,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
}

void loop() { 
  String W;
  W=spreadsheet();
  if(W[0]=='N')
   {if(W[1]=='E')
     digitalWrite(1,HIGH);
   else if(W[1]=='S')
     digitalWrite(2,HIGH);
   else if(W[1]=='W')
     digitalWrite(3,HIGH);}
  else if(W[0]=='E')
   {if(W[1]=='N')
     digitalWrite(4,HIGH);
    else if(W[1]=='S')
     digitalWrite(5,HIGH);
    else if(W[1]=='W')
     digitalWrite(6,HIGH);}
  else if(W[0]=='S')
   {if(W[1]=='E')
    digitalWrite(7,HIGH);
    else if(W[1]=='N')
     digitalWrite(8,HIGH);
    else if(W[1]=='W')
     digitalWrite(9,HIGH);}
  else if(W[0]=='W')
  {if(W[1]=='E')
    digitalWrite(10,HIGH);
  else if(W[1]=='S')
    digitalWrite(11,HIGH);
  else if(W[1]=='N')
    digitalWrite(12,HIGH);}
}

char* spreadsheet(){
  HTTPClient http;
  String url=" /"+Gscpt+"/ ";
  http.begin(url.c_str());
  http.setFollowRedirects(HTTP_STRICT_FOLLOW_REDIRECTS);
  int httpCode= http.GET();
  String X;
   if(httpCode>0){
    X= http.getString();
    return X;}
  http.end();
   }
  
}