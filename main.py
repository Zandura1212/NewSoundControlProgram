# SoundControlProgram
# Made By Zandura1212
# Version 1.1.1

import json
import win32api
import win32con
from time import sleep
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

class JsonFiles:
    options = open('options.json')
    options_data = options.read()
    options.close()

    options_loads = json.loads(options_data)
    options_programs_list = options_loads['programs']
    options_sleep_list = options_loads['sleep']
    options_volume_lv_list = options_loads['volume_lv']
    program_count = len(options_programs_list)

def control_volume(volume_up):

    sessions_to_adjust = []
    
    for i in range(JsonFiles.program_count):

        sessions = AudioUtilities.GetAllSessions()

        for session in sessions:

            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            current_volume = volume.GetMasterVolume()

            if (session.Process and session.Process.name() == JsonFiles.options_programs_list[i].get('p_name')):
                sessions_to_adjust.append((volume, current_volume))

    for volume, current_volume in sessions_to_adjust:

        if volume_up: adjust_volume(volume, current_volume, float(JsonFiles.options_volume_lv_list))
        else: adjust_volume(volume, current_volume, -float(JsonFiles.options_volume_lv_list))

def adjust_volume(volume, current_volume, step):

    if current_volume == 1 and step > 0: pass
    elif current_volume == 0 and step < 0: pass
    else:

        new_volume = max(0, min(1, current_volume + step))
        volume.SetMasterVolume(new_volume, None)

def is_pressed(key):
    return win32api.GetAsyncKeyState(key) & (1 << 15)

while True:

    JF_options_sleep_list = JsonFiles.options_sleep_list

    if is_pressed(win32con.VK_CONTROL) and is_pressed(win32con.VK_SHIFT) and is_pressed(ord('0')):

        control_volume(True)

        if JF_options_sleep_list.get('enable') == True:
            sleep(JF_options_sleep_list.get('time'))
        

    if is_pressed(win32con.VK_CONTROL) and is_pressed(win32con.VK_SHIFT) and is_pressed(ord('9')):

        control_volume(False)

        if JF_options_sleep_list.get('enable') == True:
            sleep(JF_options_sleep_list.get('time'))