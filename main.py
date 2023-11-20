# SoundControlProgram
# Made By Zandura1212
# Version 1.1

import json
import win32api
import win32con
from time import sleep
from win10toast import ToastNotifier
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

options = open('options.json')
options_data = options.read()

options_loads = json.loads(options_data)
options_programs_list = options_loads['programs']
options_sleep_list = options_loads['sleep']
options_volume_lv_list = options_loads['volume_lv']

program_count = len(options_programs_list)

alarm = ToastNotifier()
alarm.show_toast(
    "SoundControlProgram",
    "프로그램이 실행되었습니다!",
    duration = 0,
    icon_path = "icon.ico",
    threaded = True)

def volume_p():

    for i in range(program_count):

        sessions = AudioUtilities.GetAllSessions()

        for session in sessions:
            
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            current_volume = volume.GetMasterVolume()

            if session.Process and session.Process.name() == options_programs_list[i].get('p_name'):

                if current_volume == 1:
                    pass

                if current_volume + float(options_loads['volume_lv']) >= 1:
                    volume.SetMasterVolume(1, None)

                else:
                    volume.SetMasterVolume(current_volume + float(options_loads['volume_lv']), None)


def volume_m():

    for i in range(program_count):

        sessions = AudioUtilities.GetAllSessions()

        for session in sessions:
            
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            current_volume = volume.GetMasterVolume()

            if session.Process and session.Process.name() == options_programs_list[i].get('p_name'):

                if current_volume == 0:
                    pass

                if current_volume - float(options_loads['volume_lv']) <= 0:
                    volume.SetMasterVolume(0, None)

                else:
                    volume.SetMasterVolume(current_volume - float(options_loads['volume_lv']), None)

def is_pressed(key):
    return win32api.GetAsyncKeyState(key) & (1 << 15)

while True:

    if is_pressed(win32con.VK_CONTROL) and is_pressed(win32con.VK_SHIFT) and is_pressed(ord('0')):

        volume_p()

        if options_sleep_list.get('enable') == True:
            sleep(options_sleep_list.get('time'))
        

    if is_pressed(win32con.VK_CONTROL) and is_pressed(win32con.VK_SHIFT) and is_pressed(ord('9')):

        volume_m()

        if options_sleep_list.get('enable') == True:
            sleep(options_sleep_list.get('time'))