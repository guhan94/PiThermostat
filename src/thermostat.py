import json
from datetime import datetime
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home():
    """
    Home page for PiThermostat that displays all necessary information and controls.
    :return: Home page.
    """
    data = Helper().read_data()
    return render_template('main.html', set_temp=data['set_temp'], date_time=data['date_time'], heat=data['heat'],
                           humidity=data['humidity'], current_temp=data['current_temp'])


@app.route('/change/<status>/<int:temp>')
def change(status, temp):
    """
    Invoked when user updates set temperature via UI
    :param status: minus or plus based on what user clicks
    :param temp: existing set temperature on UI
    :return: Home page.
    """
    if status == 'plus' and temp < 30:
        temp += 1
        Helper().write_data(set_temp=temp)
    elif status == 'minus' and temp > 16:
        temp -= 1
        Helper().write_data(set_temp=temp)
    return redirect(url_for('home'))


class Helper(object):
    def __init__(self):
        self.file_path = './data.json'
        self.datetime_format = "%d-%b-%Y %H:%M"

    def _current_datetime(self) -> str:
        """
        Get current date and time
        :return: str(Date time)
        """
        obj = datetime.now()
        return obj.strftime(self.datetime_format)

    def read_data(self) -> dict:
        """
        Read data from data.json and return dict
        :return: dict(data)
        """
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            return data

    def write_data(self, set_temp: int = None, heat=False, current_temp: int = None, humidity: int = None):
        """
        Write dictionary data on to data.json based on input params. 2 scenarios: when user updates set_temp and
         when switch.py updates with current temperature, humidity and heat status.
        :param set_temp: User set temperature via UI
        :param heat: Turned on or off
        :param current_temp: Current temperature from DHT sensor
        :param humidity: Current humidity from DHT sensor
        :return: None
        """
        data = self.read_data()
        if set_temp is not None:
            data_dict = {"set_temp": set_temp,
                         "date_time": f'{self._current_datetime()}',
                         "heat": data['heat'],
                         "current_temp": data['current_temp'],
                         "humidity": data['humidity']}
        else:
            data_dict = {"set_temp": data['set_temp'],
                         "date_time": data['date_time'],
                         "heat": heat,
                         "current_temp": current_temp,
                         "humidity": humidity}
        with open(self.file_path, 'w') as f:
            json.dump(data_dict, f)
