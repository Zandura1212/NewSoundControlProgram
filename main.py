from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import json
import keyboard
from time import sleep

options = open('options.json')
options_data = options.read()

options_loads = json.loads(options_data)
options_programs_list = options_loads['programs']
options_volume_lv_list = options_loads['volume_lv']

program_count = len(options_programs_list)

# print("program_count:", i + 1,"/", program_count)
# print("list:", options_programs_list[i])
# print("list name:", options_programs_list[i].get('name'))
# print("list p_name:", options_programs_list[i].get('p_name'))
# print("list volume_lv:", options_loads['volume_lv'])
# print("list float(volume_lv):", float(options_loads['volume_lv']))

# 늘리는거
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
            
            print(options_programs_list[i].get('name'))


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
            
            print(options_programs_list[i].get('name'))


while True:
    if keyboard.is_pressed('ctrl+)'):
        volume_p()
        sleep(0.1)

    if keyboard.is_pressed('ctrl+('):
        volume_m()
        sleep(0.1)