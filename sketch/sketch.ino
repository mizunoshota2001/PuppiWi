#include <Stepper.h>

const int stepsPerRevolution = 2048;  // 28BYJ-48は一回転あたり2048ステップ

// ステッピングモーターを制御するためのStepクラスのインスタンス
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  // モーターのスピードを設定
  myStepper.setSpeed(10);  // 速度は10RPM
  Serial.begin(9600);
}

void loop() {
  // 時計回りに1回転
  Serial.println("時計回りに1回転");
  myStepper.step(stepsPerRevolution);
  delay(1000);

  // 反時計回りに1回転
  Serial.println("反時計回りに1回転");
  myStepper.step(-stepsPerRevolution);
  delay(1000);
}
