import datetime

import requests


class Clock:
    @staticmethod
    def now(timezone: str):
        data = Clock._get_time(timezone=timezone)
        data_as_datetime = datetime.datetime.strptime(data['currentDateTime'], "%Y-%m-%dT%H:%M%z")
        if 14 < data_as_datetime.hour < 18:
            return f"it's {data_as_datetime.strftime('%H:%M')} o'clock in {timezone}, teatime!"
        else:
            return f"it's {data_as_datetime.strftime('%H:%M')} o'clock in {timezone}, not a good time for tea!"


    @staticmethod
    def _get_time(timezone: str):
        # what's the problem here?
        res = requests.get(f"http://worldclockapi.com/api/json/{timezone}/now")

        data = res.json()

        return data
