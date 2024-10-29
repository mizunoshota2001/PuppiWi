#include <Servo.h>
Servo myServo;

void setup()
{
  myServo.attach(9);
}

void loop()
{
  myServo.write(0);
  delay(5000);
  myServo.write(180);
  delay(5000);
}
