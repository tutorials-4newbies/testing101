import requests


class Clock:
    @staticmethod
    def now(timezone: str):
        data = Clock._get_time(timezone=timezone)
        return data["currentDateTime"]

    @staticmethod
    def _get_time(timezone: str):
        res = requests.get(f"http://worldclockapi.com/api/json/{timezone}/now")
        data = res.json()

        return data
