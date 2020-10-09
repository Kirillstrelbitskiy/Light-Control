import os, pymysql, serial, time
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='own-server.zzz.com.ua',
    user='Kirill',
    password='My271320!Ps_21Qt',
    db='kirillstrelok_1',
)

while(True):
    with connection:
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT id, state FROM sh_smart_home")

        for state in db_cursor:
            if(state[0] == 2):
                if(state[1] == 1):
                    with connection:
                        db_cursor_update = connection.cursor()
                        db_cursor_update.execute("UPDATE sh_smart_home SET state=0 WHERE id=2")
                    os.system('gnome-screensaver-command -l')
                
            if(state[0] == 3):
                if(state[1] == 1):
                    with connection:
                        db_cursor_update = connection.cursor()
                        db_cursor_update.execute("UPDATE sh_smart_home SET state=0 WHERE id=3")
                    os.system('gnome-session-quit --power-off')

    time.sleep(0.1)

connection.close()
