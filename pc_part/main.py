#!/usr/bin/env python3
import os, signal, gi, serial, pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='own-server.zzz.com.ua',
    user='Kirill',
    password='My271320!Ps_21Qt',
    db='kirillstrelok_1',
)
 
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk, AppIndicator3
from gi.repository import Notify as notify

folder_with_icons = "/home/kirill/projects/Light-Control/pc_part/icons"
lamp_on_icon = folder_with_icons + "/lamp_on.png"
lamp_off_icon = folder_with_icons + "/lamp_off.png"

class Indicator(object):
    def __init__(self, name):
        self.app = name
        
        self.light_switch = AppIndicator3.Indicator.new(self.app, lamp_off_icon, AppIndicator3.IndicatorCategory.OTHER)
        self.light_switch.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.light_switch.set_menu(self.create_menu())

    def create_menu(self):
        menu = Gtk.Menu()
        item_turn_on = Gtk.MenuItem(label='Turn On')
        item_turn_on.connect('activate', self.turn_on)

        item_turn_off = Gtk.MenuItem(label='Turn Off')
        item_turn_off.connect('activate', self.turn_off)

        menu.append(item_turn_on)
        menu.append(item_turn_off)

        menu.show_all()
        return menu

    def turn_on(self, source):
        self.light_switch.set_icon(lamp_on_icon)
        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("UPDATE sh_smart_home SET state=1 WHERE id=1")

    def turn_off(self, source):
        self.light_switch.set_icon(lamp_off_icon)
        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("UPDATE sh_smart_home SET state=0 WHERE id=1")

Indicator('light')

signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
connection.close()