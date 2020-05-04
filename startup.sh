#!/usr/bin/env sh
gpio write 29 0
cd ~/thermostat/src || exit 1
export FLASK_APP=thermostat.py
python3 -m flask run --host 0.0.0.0 &
python3 switch.py &
