from __future__ import division


class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.overall = hours * 60 * 60 + minutes * 60 + seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def translate(self, overall):
        hours = overall // (60 * 60)
        minutes = (overall - hours * 60 * 60) // 60
        seconds = (overall - hours * 60 * 60 - minutes * 60) % (60 * 60)
        return MyTime(hours, minutes, seconds)

    def __add__(self, other):
        overall = self.overall + other.overall
        return self.translate(overall)

    def __sub__(self, other):
        overall = self.overall - other.overall
        return self.translate(overall)

    def __mul__(self, other):
        self.overall = self.overall * other.overall

    def __eq__(self, other):
        return self.overall == other.overall

    def __ne__(self, other):
        return self.overall != other.overall

    def __gt__(self, other):
        return self.overall > other.overall

    def __lt__(self, other):
        return self.overall < other.overall

    def __ge__(self, other):
        return self.overall <= other.overall

    def __le__(self, other):
        return self.overall >= other.overall