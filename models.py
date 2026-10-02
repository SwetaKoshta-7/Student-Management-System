class Student:
    """Represents a student record."""

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        """Convert the student object into a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["marks"]
        )