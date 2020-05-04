import time
from piutils import PiUtils
from thermostat import Helper


def switch_heat():
    data = Helper().read_data()
    humidity, temp = PiUtils().get_ht_data()
    if data['set_temp'] > temp:
        heat = True
    else:
        heat = False
    Helper().write_data(current_temp=temp, humidity=humidity, heat=heat)
    PiUtils().control_relay_switch(enable=heat)


while True:
    switch_heat()
    time.sleep(60)
