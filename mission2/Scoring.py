from abc import ABC, abstractmethod

# day point
MONDAY_POINT = 1
TUESDAY_POINT = 1
WEDNESDAY_POINT = 3
THURSDAY_POINT = 1
FRIDAY_POINT = 1
SATURDAY_POINT = 2
SUNDAY_POINT = 2

class Scoring:
    @classmethod
    def scoring(cls, attendances: list) -> int:
        total_score = 0
        for attendance in attendances:
            # 출석 점수
            if attendance == "monday":
                total_score = total_score + MONDAY_POINT
            elif attendance == "tuesday":
                total_score = total_score + TUESDAY_POINT
            elif attendance == "wednesday":
                total_score = total_score + WEDNESDAY_POINT
            elif attendance == "thursday":
                total_score = total_score + THURSDAY_POINT
            elif attendance == "friday":
                total_score = total_score + FRIDAY_POINT
            elif attendance == "saturday":
                total_score = total_score + SATURDAY_POINT
            elif attendance == "sunday":
                total_score = total_score + SUNDAY_POINT
            else:
                raise ValueError("요일 정보가 잘못 되었습니다.")

        return total_score

    @classmethod
    def special_scoring(cls, attendances) -> int:
        total_score = 0
        wednesday_attendance = 0
        saturday_attendance = 0
        sunday_attendance = 0

        for attendance in attendances:
            if attendance == "wednesday":
                wednesday_attendance = wednesday_attendance + 1
            elif attendance == "saturday":
                saturday_attendance = saturday_attendance + 1
            elif attendance == "sunday":
                sunday_attendance = sunday_attendance + 1

        if wednesday_attendance >= 10:
            total_score = total_score + 10
        if saturday_attendance + sunday_attendance >= 10:
            total_score = total_score + 10

        return total_score
