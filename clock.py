import requests


class Clock:
    @staticmethod
    def now(timezone: str):
        data = Clock._get_time(timezone=timezone)
        return f"{data['currentDateTime']} oclock in {timezone}"

    @staticmethod
    def _get_time(timezone: str):
        # what's the problem here?
        res = requests.get(f"http://worldclockapi.com/api/json/{timezone}/now")
        data = res.json()

        return data
