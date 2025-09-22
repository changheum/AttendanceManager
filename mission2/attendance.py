from typing import Tuple

from mission2.Grades import Grader, NormalGrade

person_order = []

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

from mission2.Person import PersonFactory, Person


def day_validator(day) -> None:
    if day not in days:
        raise ValueError("요일 입력이 잘못 되었습니다.")

def line_validator(line) -> Tuple[str, str]:
    try:
        name, day = line.strip().split()
    except ValueError:
        raise ValueError("파일 내, 라인 유형이 '이름 요일' 형태가 아닙니다.")

    return name, day

def load_file(src: str) -> None:
    try:
        with open(src, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break

                name, day = line_validator(line)
                day_validator(day)

                person = PersonFactory.create_or_get_person(name)
                person.add_attendance(day)

    except FileNotFoundError:
        raise FileNotFoundError("파일을 찾을 수 없습니다.")

def check_remove(person: Person) -> bool:
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

def show_score_and_result() -> None:

    for name in PersonFactory.get_person_order():
        person = PersonFactory.create_or_get_person(name)

        score = person.score
        grade = Grader.get_grade(person)

        print(f"NAME : {name}, POINT : {score}, GRADE : {grade}")

        # if grade == NormalGrade.get_name() and person_data[name]["wednesday"] == 0 and person_data[name]["saturday"] == 0 and person_data[name]["sunday"] ==0:
        #     removed_player.append(name)

    print("\nRemoved player")
    print("==============")
    for name in PersonFactory.get_person_order():
        person = PersonFactory.create_or_get_person(name)
        if check_remove(person):
            print(name)

if __name__ == "__main__":
    load_file("attendance_weekday_500.txt")
    show_score_and_result()