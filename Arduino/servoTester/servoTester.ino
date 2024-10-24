#include <Servo.h>  // サーボライブラリをインクルード

Servo myServo;      // サーボオブジェクトを作成
const int servoPin = 9; // サーボを接続するピン番号

void setup() {
  myServo.attach(servoPin); // サーボをピンに接続
}

void loop() {
  // 0度から180度まで動かす
  for (int pos = 0; pos <= 180; pos += 1) {
    myServo.write(pos);        // サーボをpos度に設定
    delay(15);                 // 動作の安定のために少し待つ
  }
  
  // 180度から0度まで動かす
  for (int pos = 180; pos >= 0; pos -= 1) {
    myServo.write(pos);        // サーボをpos度に設定
    delay(15);                 // 動作の安定のために少し待つ
  }
}
