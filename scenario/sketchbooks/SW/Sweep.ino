/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <VarSpeedServo.h>

VarSpeedServo servo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  servo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
    // in steps of 1 degree
    servo.write(180,5,true);              
    delay(15);
    servo.write(0,30,true);              
    delay(15);                            
}
 

