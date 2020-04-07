from datetime import timedelta


class DateSendInvitationService():

    def __init__(self, time_period, event_date):
        self.time_period = time_period
        self.event_date = event_date

    @classmethod
    def get_time_and_event_date(cls, validated_data):
        time_period, event_date = validated_data['time_period'], validated_data['event_date']
        return cls(time_period, event_date)

    def __call__(self, *args, **kwargs):

        _TIME_PERIOD = {
            'HOUR':self.event_date - timedelta(hours=1),
            'DAY':self.event_date - timedelta(days=1),
            'WEEK': self.event_date - timedelta(weeks=1),
        }.get(self.time_period, self.event_date)

        return _TIME_PERIOD