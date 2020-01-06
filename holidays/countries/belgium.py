from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Belgium(HolidayBase):
    """
    https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
    https://nl.wikipedia.org/wiki/Feestdagen_in_Belgi%C3%AB
    """

    def __init__(self, **kwargs):
        self.country = "BE"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New years
        self[date(year, JAN, 1)] = "Nieuwjaarsdag"

        easter_date = easter(year)

        # Easter
        self[easter_date] = "Pasen"

        # Second easter day
        self[easter_date + rd(days=1)] = "Paasmaandag"

        # Ascension day
        self[easter_date + rd(days=39)] = "O.L.H. Hemelvaart"

        # Pentecost
        self[easter_date + rd(days=49)] = "Pinksteren"

        # Pentecost monday
        self[easter_date + rd(days=50)] = "Pinkstermaandag"

        # International Workers' Day
        self[date(year, MAY, 1)] = "Dag van de Arbeid"

        # Belgian National Day
        self[date(year, JUL, 21)] = "Nationale feestdag"

        # Assumption of Mary
        self[date(year, AUG, 15)] = "O.L.V. Hemelvaart"

        # All Saints' Day
        self[date(year, NOV, 1)] = "Allerheiligen"

        # Armistice Day
        self[date(year, NOV, 11)] = "Wapenstilstand"

        # First christmas
        self[date(year, DEC, 25)] = "Kerstmis"


class BE(Belgium):
    pass
