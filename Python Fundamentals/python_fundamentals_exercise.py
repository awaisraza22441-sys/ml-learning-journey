'''Objective: Build a program that reads student records, analyses their academic performance, and generates a report.'''

subjects = ("Python", "Statistics", "Mathematics")


def create_file():
    with open("students.txt", "w") as file:
        file.write("Ali,85,78,92\n")
        file.write("Ahmed,65,70,68\n")
        file.write("Sara,90,95,88\n")
        file.write("Usman,45,55,50\n")
        file.write("Ayesha,72,80,75\n")
        file.write("Hamza,35,40,45\n")


def read_and_process():
    students = []
    try:
        with open("students.txt", "r") as file:
            for entry in file:
                grade = ""
                status = ""
                total_marks = 0
                avg_marks = 0
                content = entry.strip()
                cleaned_content = content.split(",")
                student_record = {}

                try:
                    name, python_marks, statistics_marks, mathematics_marks = cleaned_content
                    total_marks += int(python_marks) + int(statistics_marks) + int(mathematics_marks)
                except ValueError:
                    print("Invalid data found in line:", content)
                    continue

                avg_marks = total_marks / len(subjects)

                if avg_marks >= 80:
                    grade = "A"
                    status = "Passed"
                elif avg_marks >= 70:
                    grade = "B"
                    status = "Passed"
                elif avg_marks >= 60:
                    grade = "C"
                    status = "Passed"
                elif avg_marks >= 50:
                    grade = "D"
                    status = "Passed"
                elif avg_marks < 50:
                    grade = "F"
                    status = "Failed"
                else:
                    print("Invalid Result")

                student_record["name"] = name
                student_record["total"] = total_marks
                student_record["average"] = round(avg_marks, 2)
                student_record["grade"] = grade
                student_record["status"] = status
                students.append(student_record)

    except FileNotFoundError:
        print("Error: students.txt file not found.")

    return students


def analyze_performance(students):
    passed_students = [student for student in students if student["status"] == "Passed"]
    total_students = len(students)
    passed_count = len(passed_students)
    failed_count = total_students - passed_count

    total_class_avg = 0
    lowest = students[0]
    highest = students[0]
    unique_grades = set()
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for student in students:
        total_class_avg += student["average"]

        if student["total"] > highest["total"]:
            highest = student
        if student["total"] < lowest["total"]:
            lowest = student

        unique_grades.add(student["grade"])
        grade_counts[student["grade"]] += 1

    class_avg = round(total_class_avg / total_students, 2)

    return passed_students, total_students, passed_count, failed_count, class_avg, highest, lowest, unique_grades, grade_counts


def generate_reports(students, passed_students, total_students, passed_count, failed_count, class_avg, highest, lowest, unique_grades, grade_counts):
    with open("passed_students.txt", "w") as file:
        file.write("Passed Students:\n")
        for student in passed_students:
            file.write(f"{student['name']} - Total: {student['total']}, Average: {student['average']}, Grade: {student['grade']}\n")

    with open("performance_report.txt", "w") as file:
        file.write("Class Performance Report\n")
        file.write("-------------------------\n")
        file.write(f"Subjects: {subjects}\n")
        file.write(f"Total Students: {total_students}\n")
        file.write(f"Passed Students: {passed_count}\n")
        file.write(f"Failed Students: {failed_count}\n")
        file.write(f"Class Average: {class_avg}\n")
        file.write(f"Highest Scoring Student: {highest['name']} ({highest['total']})\n")
        file.write(f"Lowest Scoring Student: {lowest['name']} ({lowest['total']})\n")
        file.write(f"Unique Grades: {unique_grades}\n")
        file.write("Grade Counts:\n")
        for grade, count in grade_counts.items():
            file.write(f"  {grade}: {count}\n")


create_file()
students = read_and_process()
passed_students, total_students, passed_count, failed_count, class_avg, highest, lowest, unique_grades, grade_counts = analyze_performance(students)
generate_reports(students, passed_students, total_students, passed_count, failed_count, class_avg, highest, lowest, unique_grades, grade_counts)

print("Reports generated successfully!")

with open("performance_report.txt","r") as file:
    content = file.read()
    print(content)
