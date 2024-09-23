#include <Servo.h>

Servo myServo;  // Servoオブジェクトを作成

void setup() {
  myServo.attach(9);  // サーボモーターの信号線をデジタルピン9に接続
}

void loop() {
  myServo.write(0);    // サーボを0度に設定
  delay(250);         // 1秒待つ

  myServo.write(90);   // サーボを90度に設定
  delay(250);         // 1秒待つ
}
