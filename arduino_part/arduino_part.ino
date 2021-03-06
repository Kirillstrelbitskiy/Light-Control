#include <IRremote.h>

IRrecv irrecv(7);
decode_results results;

int number_of_devices = 4;
int devices_ports[] = {3, 2, 4, 5, 6};
char devices_names[] = {'a', 'b', 'c', 'd', 'e'};

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
  
  for (int i = 0; i < number_of_devices; i++) {
    pinMode(devices_ports[i], OUTPUT);
    digitalWrite(devices_ports[i], false);
  }
}

void loop() {
  if ( irrecv.decode( &results )) {
    if(results.value == 3914386312)
      digitalWrite(devices_ports[0], true);
    else if (results.value == 2042961284)
        digitalWrite(devices_ports[0], false);
        
    if(results.value == 3326928104)
      digitalWrite(devices_ports[1], true);
    else if (results.value == 373699500)
        digitalWrite(devices_ports[1], false);
        
    irrecv.resume();
  }

  String recieved_command = "";
  while (Serial.available()){
    recieved_command += (char)Serial.read();
    delay(30);
  }
  
  if(recieved_command != ""){
    char device = recieved_command[0],
        command = recieved_command[1];

    int device_id = find_device_id(device);
    Serial.println(device_id);
    if(device_id != -1){
      if(device_id == 2)
        change_computer_state();
      else if(device_id == 3)
        power_on_computer();
      else{
        if (command == '1')
          digitalWrite(devices_ports[device_id], true);
        else if (command == '0')
          digitalWrite(devices_ports[device_id], false);
      }
      
      Serial.println("Ready");
    }
  }
}

void change_computer_state(){
  digitalWrite(devices_ports[2], HIGH);
  delay(2000);
  digitalWrite(devices_ports[2], LOW);
}

void power_on_computer(){
  digitalWrite(devices_ports[3], HIGH);
  delay(500);
  digitalWrite(devices_ports[3], LOW);
}

int find_device_id(char device_name) {
  for (int i = 0; i < number_of_devices; i++)
    if (devices_names[i] == device_name)
      return i;
  return -1;
}
