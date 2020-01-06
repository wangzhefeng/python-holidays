from datetime import date

from dateutil.easter import easter, EASTER_ORTHODOX
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import *
from holidays.holiday_base import HolidayBase


class Belarus(HolidayBase):
    """
    http://president.gov.by/en/holidays_en/
    http://www.belarus.by/en/about-belarus/national-holidays
    """

    def __init__(self, **kwargs):
        self.country = "BY"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1998
        # http://laws.newsby.org/documents/ukazp/pos05/ukaz05806.htm
        if year <= 1998:
            return

        # New Year's Day
        self[date(year, JAN, 1)] = "Новый год"

        # Jan 2nd is the national holiday (New Year) from 2020
        # http://president.gov.by/uploads/documents/2019/464uk.pdf
        if year >= 2020:
            # New Year's Day
            self[date(year, JAN, 2)] = "Новый год"

        # Christmas Day (Orthodox)
        self[date(year, JAN, 7)] = "Рождество Христово " \
                                   "(православное Рождество)"

        # Women's Day
        self[date(year, MAR, 8)] = "День женщин"

        # Radunitsa ("Day of Rejoicing")
        self[easter(year, method=EASTER_ORTHODOX) + rd(days=9)] = "Радуница"

        # Labour Day
        self[date(year, MAY, 1)] = "Праздник труда"

        # Victory Day
        self[date(year, MAY, 9)] = "День Победы"

        # Independence Day
        self[date(year, JUL, 3)] = "День Независимости Республики Беларусь " \
                                   "(День Республики)"

        # October Revolution Day
        self[date(year, NOV, 7)] = "День Октябрьской революции"

        # Christmas Day (Catholic)
        self[date(year, DEC, 25)] = "Рождество Христово " \
                                    "(католическое Рождество)"


class BY(Belarus):
    pass
