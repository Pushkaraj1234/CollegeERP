students = {}

def add_student(student_id, name, course):
    student_id = str(student_id).strip()
    if not student_id or student_id in students:
        return False
    students[student_id] = {"name": name, "course": course}
    return True

def get_student(student_id):
    return students.get(str(student_id).strip())

def list_students():
    return list(students.items())
