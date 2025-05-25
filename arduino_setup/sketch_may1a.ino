#include <NewPing.h>

#define echo1 3 
#define trigger1 2

NewPing sensor1(trigger1, echo1, 400);

void setup() {
  Serial.begin(115200);
}

void loop() {
  delay(1000);
  int reading1 = sensor1.ping_cm();
  if(reading1 != 0){
    Serial.print("totalDistance = ");
    Serial.println(reading1);
  }
}