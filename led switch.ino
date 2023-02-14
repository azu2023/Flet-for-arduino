#include <Arduino.h>

int led_1 = 11;
int led_2 = 3;
int led_3 = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led_1,OUTPUT);
  pinMode(led_2,OUTPUT);
  pinMode(led_3,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    char c = Serial.read();
    if(c=='r'){
      digitalWrite(led_1,HIGH);
    }
    if(c=='x')
    {
      digitalWrite(led_1,LOW);
    }
    if(c=='b'){
      digitalWrite(led_2,HIGH);
    }
    if(c=='c')
    {
      digitalWrite(led_2,LOW);
    }
    if(c=='g'){
      digitalWrite(led_3,HIGH);
    }
    if(c=='v')
    {
      digitalWrite(led_3,LOW);
    }
    }
  }
