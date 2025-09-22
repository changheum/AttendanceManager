import pytest
from mission2.attendance import *

def test_factory_singletone_정상인가():
    person_factory1 = PersonFactory()
    person_factory2 = PersonFactory()
    assert person_factory1 is person_factory2

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_file('not-found')

def test_all():
    load_file("C:\\Users\\User\\PycharmProjects\\AttendanceManager\\mission2\\attendance_weekday_500.txt")

def test_attendance_weekday_test_case_wrong_line():
    with pytest.raises(ValueError):
        load_file("C:\\Users\\User\\PycharmProjects\\AttendanceManager\\mission2\\attendance_weekday_test_case_wrong_line.txt")

def test_잘못된_요일_입력():
    name, day = "test", "요일"
    with pytest.raises(ValueError):
        day_validator(day)

def test_노말인데_수요일():
    name, day = "test", "wednesday"
    person = PersonFactory.create_or_get_person(name)
    person.add_attendance(day)

    show_score_and_result()
