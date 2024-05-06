#include <AccelStepper.h>
#include <MultiStepper.h>

/******** Definiciones ********/
#define N_ang 3
#define steps 200
#define stepPin1 2
#define dirPin1 5
#define stepPin2 3
#define dirPin2 6
#define stepPin3 4
#define dirPin3 7
#define LSwitch1 9
#define LSwitch2 10
#define LSwitch3 11

/******** Constructores ********/
AccelStepper stepper1(AccelStepper::DRIVER, stepPin1, dirPin1);
AccelStepper stepper2(AccelStepper::DRIVER, stepPin2, dirPin2);
AccelStepper stepper3(AccelStepper::DRIVER, stepPin3, dirPin3);

/******** Variables ********/
String cmd_python = "";
String cmd_back = "";
float T[N_ang];

/******** Funciones ********/
void calibrar(AccelStepper& stepper, bool dir, int SwitchPin) {
    stepper.setMaxSpeed(5000);
    stepper.setAcceleration(5000.0);

    if (dir) {
        stepper.setSpeed(5000);
        while (!digitalRead(SwitchPin)) {
            stepper.runSpeed();
        }
    } else {
        stepper.setSpeed(-5000);
        while (!digitalRead(SwitchPin)) {
            stepper.runSpeed();
        }
    }
    stepper.setCurrentPosition(0);
}

void mover_kin_rot(AccelStepper& stepper, float dist, float relacion, float speed) {
    dist = round((dist * steps * relacion) / 360);
    Serial.println(dist);
    stepper.moveTo(dist);
    stepper.setSpeed(speed);
    stepper.runSpeedToPosition();
}

void setup() {
    Serial.begin(115200);
    pinMode(LSwitch1, INPUT_PULLUP);
    pinMode(LSwitch2, INPUT_PULLUP);
    pinMode(LSwitch3, INPUT_PULLUP);
    calibrar(stepper1, 1, LSwitch1);
    calibrar(stepper2, 1, LSwitch2);
    calibrar(stepper3, 1, LSwitch3);
}

void loop() {
    if (Serial.available() > 0) {
        cmd_python = Serial.readStringUntil('\n');
        //cmd_back = Serial.print(cmd_python);
        int prevIndex = 0;
        int nextIndex = cmd_python.indexOf(',');

        for (int i = 0; i < N_ang; i++) {
            if (nextIndex > 0) {
                T[i] = cmd_python.substring(prevIndex, nextIndex).toFloat();
                prevIndex = nextIndex + 1;
                nextIndex = cmd_python.indexOf(',', prevIndex);
            } else {
                T[i] = cmd_python.substring(prevIndex).toFloat();
                break;
            }
        }
        Serial.println(T[0]);
        Serial.println(T[1]);
        Serial.println(T[2]);
        
    }
    mover_kin_rot(stepper1, T[0], 100, 5000);
        mover_kin_rot(stepper2, T[1], 50, 5000);
        mover_kin_rot(stepper3, T[2], 1, 5000);
}
