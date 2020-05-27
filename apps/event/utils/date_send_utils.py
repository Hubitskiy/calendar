from datetime import timedelta


class DateSendInvitation:

    def __init__(self, validated_data):
        self.validated_data = validated_data

    def __call__(self, *args, **kwargs):
        time_period = self.validated_data["time_period"]
        event_date = self.validated_data["event_date"]
        _time_period = {
                'HOUR': event_date - timedelta(hours=1),
                'DAY':  event_date - timedelta(days=1),
                'WEEK': event_date - timedelta(weeks=1),
            }.get(time_period, event_date)

        return _time_period
