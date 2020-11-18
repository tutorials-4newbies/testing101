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

    def is_it_open_now(self):
        pass

