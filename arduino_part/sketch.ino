#define lamp_port 2

void setup() {
  Serial.begin(9600);
  pinMode(lamp_port, OUTPUT);
  digitalWrite(lamp_port, true);
}

void loop() {
  while(Serial.available()){
    char command = (char)Serial.read(); // 1 - turn_on   0 - turn_off
    Serial.println(command);

    if(command == '1')
      digitalWrite(lamp_port, true);
    else if(command == '0')
      digitalWrite(lamp_port, false);
  }
}
