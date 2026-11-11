import random
from datetime import date, timedelta


#Return an ID like 'stu001'
def generate_student_id(index):
    return f"stu{index:03d}"


def random_birth_date(start_year=2000, end_year=2006):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))


def generate_grades(n=3, low=0, high=20):
    return [round(random.uniform(low, high), 2) for _ in range(n)]


def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)


def generate_students(seed=None):
    if seed is not None:
        random.seed(seed)

    students = []
    for i in range(1, 11):
        grades = generate_grades()
        students.append({
            "id": generate_student_id(i),
            "birth_date": random_birth_date(),
            "grade1": grades[0],
            "grade2": grades[1],
            "grade3": grades[2],
            "average": calculate_average(grades),
        })
    return students
