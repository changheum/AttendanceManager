person_order = []
person_data = {}

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

# day point
MONDAY_POINT = 1
TUESDAY_POINT = 1
WEDNESDAY_POINT = 3
THURSDAY_POINT = 1
FRIDAY_POINT = 1
SATURDAY_POINT = 2
SUNDAY_POINT = 2

# grades
GRADE_GOLD = "GOLD"
GRADE_SILVER = "SILVER"
GRADE_NORMAL = "NORMAL"

def load_file() -> None:
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                name, day = line.strip().split()
                check_attendance(name, day)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def check_attendance(name, day) -> None:
    global person_data

    if name not in person_data.keys():
        person_order.append(name)
        person_data[name] = {}

        for _day in days:
            person_data[name][_day] = 0

    person_data[name][day] = person_data[name][day] + 1

def special_scoring(name) -> int:
    global person_data

    special_score = 0
    if person_data[name]["wednesday"] >= 10:
        special_score = special_score + 10
    if person_data[name]["saturday"] + person_data[name]["sunday"] >= 10:
        special_score = special_score + 10

    return special_score

def scoring(name) -> int:
    global person_data

    score = 0

    # 출석 점수
    score = score + person_data[name]["monday"] * MONDAY_POINT
    score = score + person_data[name]["tuesday"] * TUESDAY_POINT
    score = score + person_data[name]["wednesday"] * WEDNESDAY_POINT
    score = score + person_data[name]["thursday"] * THURSDAY_POINT
    score = score + person_data[name]["friday"] * FRIDAY_POINT
    score = score + person_data[name]["saturday"] * SATURDAY_POINT
    score = score + person_data[name]["sunday"] * SUNDAY_POINT

    # 특별 점수
    score = score + special_scoring(name)

    return score

def grading(score) -> str:
    global person_data

    if score >= 50:
        return GRADE_GOLD
    elif score >= 30:
        return GRADE_SILVER

    return GRADE_NORMAL

def result() -> None:
    global person_data

    removed_player = []

    for name in person_order:
        score = scoring(name)
        grade = grading(score)

        print(f"NAME : {name}, POINT : {score}, GRADE : {grade}")

        if grade == GRADE_NORMAL and person_data[name]["wednesday"] == 0 and person_data[name]["saturday"] == 0 and person_data[name]["sunday"] ==0:
            removed_player.append(name)

    print("\nRemoved player")
    print("==============")
    for name in removed_player:
        print(name)



if __name__ == "__main__":
    load_file()
    result()