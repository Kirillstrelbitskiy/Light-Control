#!/usr/bin/env python3
import os, signal, gi, serial

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3
from gi.repository import Notify as notify

folder_with_icons = "/home/kirill/.light_control/icons"
lamp_on_icon = folder_with_icons + "/lamp_on.png"
lamp_off_icon = folder_with_icons + "/lamp_off.png"

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
arduino.write(b'0') # initialize lamp with off state

class Indicator():
    def __init__(self):
        self.app = 'show_proc'

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
        arduino.write(b'1') # command changing lamp state

    def turn_off(self, source):
        self.light_switch.set_icon(lamp_off_icon)
        arduino.write(b'0') # command changing lamp state

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
