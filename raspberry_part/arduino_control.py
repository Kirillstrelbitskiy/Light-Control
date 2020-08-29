import os, pymysql, serial, time
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='own-server.zzz.com.ua',
    user='Kirill',
    password='My271320!Ps_21Qt',
    db='kirillstrelok_1',
)
 
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)

devices = ['a', 'b']
state_of_device = {}
for i in devices:
    name = i + "0"
    arduino.write(name.encode()) # initialization with off state
    state_of_device.update({i: 0})

while(True):
    with connection:
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT address, state FROM sh_smart_home")

        for state in db_cursor:
            if(state[0] >= 'a' and state[0] <= 'z'):
                print(state_of_device.get(state[0]), state[1])
                if(state_of_device.get(state[0]) != state[1]):
                    print("yes")
                    command_to_send = state[0] + str(state[1])
                    arduino.write(command_to_send.encode()) # command changing lamp state
                    state_of_device.update({state[0]: state[1]})
    time.sleep(0.1)

connection.close()
