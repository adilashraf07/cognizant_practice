import json
import re


class InvalidStudentRecordError(Exception):
    """Raised when a student record is malformed."""


students = [
    "101,Arun,Math:80|Physics:70|Chemistry:90",
    "102,Meera,Math:45|Physics:55|Chemistry:60",
    "103,Ravi,Math:30|Physics:25|Chemistry:40",
    "104,Anu,Math:80|Physics:95|Chemistry:85",
]


RECORD_PATTERN = re.compile(r"^(\d+),([A-Za-z][A-Za-z\s]*),(.+)$")
SUBJECT_PATTERN = re.compile(r"^([A-Za-z]+):([0-9]{1,3})$")


def calculate_grade(average):
    if average >= 80:
        return "A"
    if average >= 60:
        return "B"
    if average >= 40:
        return "C"
    return "F"


def parse_student_record(record):
    match = RECORD_PATTERN.fullmatch(record.strip())
    if not match:
        raise InvalidStudentRecordError(f"Invalid record format: {record}")

    student_id_text, student_name, subject_data = match.groups()
    student_name = student_name.strip()

    if not student_name:
        raise InvalidStudentRecordError("Student name is empty")

    if not subject_data:
        raise InvalidStudentRecordError("Subject data is missing")

    subjects = {}
    for item in subject_data.split("|"):
        subject_entry = item.strip()
        if not subject_entry:
            raise InvalidStudentRecordError("Empty subject entry")

        subject_match = SUBJECT_PATTERN.fullmatch(subject_entry)
        if not subject_match:
            raise InvalidStudentRecordError(f"Invalid subject entry: {subject_entry}")

        subject, mark_text = subject_match.groups()
        mark = int(mark_text)

        if not 0 <= mark <= 100:
            raise InvalidStudentRecordError(f"Mark out of range: {mark}")

        subjects[subject] = mark

    if not subjects:
        raise InvalidStudentRecordError("No valid subjects found")

    total_marks = sum(subjects.values())
    average_marks = round(total_marks / len(subjects), 2)

    return {
        "student_id": int(student_id_text),
        "student_name": student_name,
        "subjects": subjects,
        "total_marks": total_marks,
        "average_marks": average_marks,
        "grade": calculate_grade(average_marks),
    }


def build_student_result(records):
    student_objects = []
    invalid_records = []

    for record in records:
        try:
            student_object = parse_student_record(record)
        except InvalidStudentRecordError as exc:
            invalid_records.append({"record": record, "error": str(exc)})
            continue

        student_objects.append(student_object)

    class_average = round(
        sum(student["average_marks"] for student in student_objects) / len(student_objects),
        2,
    ) if student_objects else 0.0

    return {
        "students": student_objects,
        "class_average": class_average,
        "invalid_records": invalid_records,
    }


if __name__ == "__main__":
    result = build_student_result(students)
    print(json.dumps(result, indent=2))

 