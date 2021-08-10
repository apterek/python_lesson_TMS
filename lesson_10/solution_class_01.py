from __future__ import division


class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.second = seconds

        self.overall = hours * 60 * 60 - minutes * 60 + seconds

    def __eq__(self, other):
        return self.overall == other.overall

    def __ne__(self, other):
        return self.overall != other.overall

    def __lt__(self, other):
        return self.overall < other.overall

    def __gt__(self, other):
        return self.overall > other.overall

    def __le__(self, other):
        return self.overall <= other.overall

    def __ge__(self, other):
        return self.overall >= other.overall

    def __add__(self, other):
        self.overall += other.overall

    def __sub__(self, other):
        self.overall -= other.overall

    def __mul__(self, other):
        self.overall *= other.overall

    def __truediv__(self, other):
        self.overall /= other.overall


