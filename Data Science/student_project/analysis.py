import statistics
from datetime import date
from pathlib import Path


# Age in full years at `today` (default: today's date
def calculate_age(birth_date, today=None):
    today = today or date.today()
    before_birthday = (today.month, today.day) < (birth_date.month, birth_date.day)
    return today.year - birth_date.year - int(before_birthday)


# Add an 'age' key to every student
def add_ages(students):
    for s in students:
        s["age"] = calculate_age(s["birth_date"])
    return students


# Computing statistics
def compute_statistics(students):
    # Return a dictionary of class statistics
    averages = [s["average"] for s in students]
    ages = [s["age"] for s in students]
    return {
        "number_of_students": len(students),
        "mean_average": statistics.mean(averages),
        "median_average": statistics.median(averages),
        "std_average": statistics.stdev(averages),   # sample std (n-1)
        "min_average": min(averages),
        "max_average": max(averages),
        "mean_age": statistics.mean(ages),
    }


#Save a summary of the results
def save_report(students, stats, folder="results", filename="report.txt"):
    folder_path = Path(folder)
    folder_path.mkdir(exist_ok=True)      # create results/ only if it does not exist
    path = folder_path / filename

    with open(path, "w", encoding="utf-8") as f:
        f.write("=== CLASS REPORT ===\n\n")
        f.write(f"Number of students : {stats['number_of_students']}\n")
        f.write(f"Mean average       : {stats['mean_average']:.2f}\n")
        f.write(f"Median average     : {stats['median_average']:.2f}\n")
        f.write(f"Standard deviation : {stats['std_average']:.2f}\n")
        f.write(f"Minimum average    : {stats['min_average']:.2f}\n")
        f.write(f"Maximum average    : {stats['max_average']:.2f}\n")
        f.write(f"Mean age           : {stats['mean_age']:.2f}\n\n")

        f.write("=== STUDENTS ===\n")
        for s in students:
            f.write(f"{s['id']} | born {s['birth_date']} | age {s['age']} | "
                    f"grades {s['grade1']}, {s['grade2']}, {s['grade3']} | "
                    f"average {s['average']}\n")
    return str(path)
