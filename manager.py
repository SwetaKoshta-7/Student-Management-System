import json
from pathlib import Path

from models import Student


class StudentManager:
    """Manage student records and perform CRUD operations."""

    def __init__(self, file_path=None):
        self.students = []

        if file_path is None:
            file_path = Path(__file__).parent / "students.json"

        self.file_path = Path(file_path)
        self.load_from_file()

    def add_student(self, student):
        """Add a new student if the ID is unique."""
        if self.find_by_id(student.student_id):
            return False

        self.students.append(student)
        self.save_to_file()
        return True

    def get_all_students(self):
        """Return all student records."""
        return self.students

    def find_by_id(self, student_id):
        """Find a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def search_by_name(self, name):
        """Find students whose names contain the search text."""
        search_text = name.lower()

        return [
            student
            for student in self.students
            if search_text in student.name.lower()
        ]

    def update_student(self, student_id, **updated_fields):
        """Update one or more fields of a student."""
        student = self.find_by_id(student_id)

        if not student:
            return False

        allowed_fields = {"name", "age", "course", "marks"}

        for field, value in updated_fields.items():
            if field in allowed_fields:
                setattr(student, field, value)

        self.save_to_file()
        return True

    def delete_student(self, student_id):
        """Delete a student by ID."""
        student = self.find_by_id(student_id)

        if not student:
            return False

        self.students.remove(student)
        self.save_to_file()
        return True

    def sort_by_name(self):
        """Return students sorted alphabetically by name."""
        return sorted(
            self.students,
            key=lambda student: student.name.lower()
        )

    def sort_by_marks(self, descending=True):
        """Return students sorted by marks."""
        return sorted(
            self.students,
            key=lambda student: student.marks,
            reverse=descending
        )

    def calculate_average_marks(self):
        """Calculate the average marks of all students."""
        if not self.students:
            return 0

        total_marks = sum(student.marks for student in self.students)
        return total_marks / len(self.students)

    def get_top_student(self):
        """Return the student with the highest marks."""
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.marks)

    def save_to_file(self):
        """Save all student records to the JSON file."""
        data = [student.to_dict() for student in self.students]

        try:
            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print(f"Error saving student data: {error}")

    def load_from_file(self):
        """Load student records from the JSON file."""
        if not self.file_path.exists():
            self.students = []
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            self.students = [
                Student.from_dict(student_data)
                for student_data in data
            ]

        except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
            print(f"Warning: Could not load student data: {error}")
            self.students = []