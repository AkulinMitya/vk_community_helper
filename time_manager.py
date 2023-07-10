from datetime import datetime


class TimeManager:
    @staticmethod
    def convert_to_unix_timestamp(time_str: str) -> int:
        try:
            time_format = "%Y:%m:%d:%H:%M"
            dt = datetime.strptime(time_str, time_format)
            timestamp = int(dt.timestamp())
            return timestamp
        except ValueError:
            raise ValueError("Invalid time format. Please provide time in the format: year:month:day:hours:minutes.")
