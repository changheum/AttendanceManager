import pytest
from mission2.attendance import load_file

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_file('not-found')

def test_all():
    load_file("C:\\Users\\User\\PycharmProjects\\AttendanceManager\\mission2\\attendance_weekday_500.txt")
