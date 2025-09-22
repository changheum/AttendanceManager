from abc import ABC, abstractmethod
from mission2.Person import Person


class Grade(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_passed(self, person: Person) -> bool:
        pass

class GoldGrade(Grade):
    def get_name(self):
        return "GOLD"

    def is_passed(self, person: Person) -> bool:
        if person.score > 50:
            return True
        return False

class SilverGrade(Grade):
    def get_name(self):
        return "SILVER"

    def is_passed(self, person: Person) -> bool:
        if person.score > 30:
            return True
        return False

class NormalGrade(Grade):
    def get_name(self):
        return "NORMAL"

    def is_passed(self, person: Person) -> bool:
        return True

class Grader:
    grades = [
        GoldGrade(),
        SilverGrade(),
        NormalGrade()
    ]

    @classmethod
    def get_grade(cls, person: Person):
        for grade in cls.grades:
            if grade.is_passed(person):
                return grade.get_name()

        return cls.grades[-1].get_name()