from datetime import datetime, timedelta


class DateSendInvitationService():

    def __init__(self, time_period, event_date):
        self.time_period = time_period
        self.event_date = event_date

    def date_to_send_invitation(self):
        return self.event_date - timedelta(days=1)

