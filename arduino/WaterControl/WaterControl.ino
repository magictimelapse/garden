
// include the TinkerKit library
#include <TinkerKit.h>
/*
  Blink
 Turns on an LED on for one second, then off for one second, repeatedly.
 
 This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
#define MAX_NUMBER_OF_VALVES 4
int led = 13;
TKRelay relay0(O0);
TKRelay relay1(O1);
TKRelay relay2(O2);
TKRelay relay3(O3);
TKRelay relay4(O4);
TKRelay relay5(O5);

long previousMillis[MAX_NUMBER_OF_VALVES];
bool valveOpen[MAX_NUMBER_OF_VALVES];
long interval = 30000; 
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  int i;
  for (i =0; i<MAX_NUMBER_OF_VALVES; i++)
    previousMillis[i] = 0;
  valveOpen[i] = false;
}

char serialReadWithTimeout(long timeout){
  char retVal;
  unsigned long timeStart = millis();
  while(Serial.available() == 0){ // check for timeout
    if(millis() - timeStart > timeout)
    {
      retVal = '\0';
      return retVal;
    } 
  }
  retVal = Serial.read();
  return retVal;

}

// the loop routine runs over and over again forever:
void loop() {
  unsigned long currentMillis = millis();
  int i;
  for (i =0; i<MAX_NUMBER_OF_VALVES; i++)
  {
    if(currentMillis - previousMillis[i] > interval && valveOpen[i])
    {
      previousMillis[i] = currentMillis;
      if(i == 0)
      {
        valveOpen[0] = false;
        relay3.off();
        Serial.write('e'); // arduino closed a valve
        Serial.write('0'); /// valve number 0
      }
    }

  }
  if(Serial.available()) {
    char serialIn = Serial.read();
    Serial.write(serialIn);
    if(serialIn == 'o') // open a valve
    {
      serialIn = serialReadWithTimeout(1000);
      Serial.write(serialIn);
      if(serialIn == '0') // open valve 0
      {
        relay3.on();
        previousMillis[0] = millis();
        valveOpen[0] = true;
        Serial.write('k'); // confirm
      }

      //relay3.off();
      //Serial.write('d');

    }
    else if(serialIn == 'c') // close a valve 
    {
       serialIn = serialReadWithTimeout(1000);
      if(serialIn == '0')  // close valve 0
      {
        relay3.off(); 
        valveOpen[0] = false;
        Serial.write('k'); // confirm
      }
    }
    Serial.write("d");
    delay(1000);
  }
}






