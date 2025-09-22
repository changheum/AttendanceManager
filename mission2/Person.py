
from abc import ABC, abstractmethod

from mission2.Scoring import Scoring

class Person:
    def __init__(self, name):
        self.name = name
        self.attendances = []

    def add_attendance(self, day):
        self.attendances.append(day)

    @property
    def score(self):
        total_score = Scoring.scoring(attendances=self.attendances) + Scoring.special_scoring(attendances=self.attendances)

        return total_score

class PersonFactory:
    _instance = None  # Static 인스턴스 변수

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PersonFactory, cls).__new__(cls)
            cls._instance.caching = {}
            cls._instance.person_order = []

        return cls._instance

    @classmethod
    def create_or_get_person(cls, name) -> Person:
        if cls._instance is None:
            cls._instance = super(PersonFactory, cls).__new__(cls)
            cls._instance.caching = {}
            cls._instance.person_order = []

        if name in cls._instance.caching.keys():
            return cls._instance.caching[name]
        else:
            person = Person(name)
            cls._instance.caching[name] = person
            cls._instance.person_order.append(name)

            return person

    @classmethod
    def get_person_order(cls):
        return cls._instance.person_order
