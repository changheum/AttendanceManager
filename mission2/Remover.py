from mission2.Grades import Grader
from mission2.Person import Person


class Remover:
    @classmethod
    def check_remove(cls, person: Person) -> bool:
        grade = Grader.get_grade(person)

        if grade != Grader.grades[-1].get_name():
            return False
        for attendance in person.attendances:
            if attendance == "wednesday":
                return False
            elif attendance == "saturday":
                return False
            elif attendance == "sunday":
                return False
        return True