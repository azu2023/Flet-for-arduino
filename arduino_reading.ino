#include <Arduino.h>
int led = 11;
void setup() {
Serial.begin(9600);
pinMode(led,OUTPUT);
}

void loop() {
int v = map(analogRead(A1),0,1023,0,100);
float v_2 = v/100.0;
analogWrite(led,v);
Serial.println(v_2);
delay(200);
}
