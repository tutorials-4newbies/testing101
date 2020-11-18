import datetime

SUNDAY = 6
TUESDAY = 1
OPENING_HOURS = {
    SUNDAY: {
        "open_hour": 8,
        "close_hour": 16
    },
    TUESDAY: {
        "open_hour": 16,
        "close_hour": 20
    }
}


class OpeningHoursHelper:
    def __init__(self, time_provider=datetime.datetime):
        self.time_provider = time_provider

    def is_it_open_now(self):
        now = self.time_provider.now()
        if now.weekday() not in OPENING_HOURS:
            return False
        opening_hours_today = OPENING_HOURS[now.weekday()]

        return opening_hours_today["open_hour"] <= now.hour < opening_hours_today["close_hour"]
