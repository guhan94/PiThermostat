#!/usr/bin/env sh
gpio write 29 0
cd ~/thermostat/src || exit 1
export FLASK_APP=thermostat.py
python3 -m flask run &
python3 switch.py &
