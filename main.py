from models import Student
from manager import StudentManager
from utils import (
    get_non_empty_input,
    get_integer_input,
    get_float_input,
    confirm_action
)


def display_header(title):
    """Display a formatted section header."""
    print("\n" + "=" * 55)
    print(title.center(55))
    print("=" * 55)


def display_student(student):
    """Display a single student's details."""
    print(
        f"ID: {student.student_id} | "
        f"Name: {student.name} | "
        f"Age: {student.age} | "
        f"Course: {student.course} | "
        f"Marks: {student.marks:.2f}"
    )


def display_students(students):
    """Display a collection of students."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 85)
    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Marks':>10}"
    )
    print("-" * 85)

    for student in students:
        print(
            f"{student.student_id:<10}"
            f"{student.name:<20}"
            f"{student.age:<8}"
            f"{student.course:<20}"
            f"{student.marks:>10.2f}"
        )

    print("-" * 85)


def add_student(manager):
    """Collect details and add a new student."""
    display_header("ADD STUDENT")

    student_id = get_non_empty_input("Enter student ID: ")

    if manager.find_by_id(student_id):
        print("A student with this ID already exists.")
        return

    name = get_non_empty_input("Enter student name: ")
    age = get_integer_input("Enter student age: ", minimum=1, maximum=100)
    course = get_non_empty_input("Enter course: ")
    marks = get_float_input("Enter marks: ", minimum=0, maximum=100)

    student = Student(
        student_id,
        name,
        age,
        course,
        marks
    )

    if manager.add_student(student):
        print("\nStudent added successfully.")


def view_students(manager):
    """Display all students."""
    display_header("ALL STUDENTS")
    display_students(manager.get_all_students())


def search_student(manager):
    """Search for a student by ID or name."""
    display_header("SEARCH STUDENT")

    print("1. Search by ID")
    print("2. Search by Name")

    choice = get_integer_input(
        "Enter your choice: ",
        minimum=1,
        maximum=2
    )

    if choice == 1:
        student_id = get_non_empty_input("Enter student ID: ")
        student = manager.find_by_id(student_id)

        if student:
            print("\nStudent found:")
            display_student(student)
        else:
            print("\nNo student found with that ID.")

    else:
        name = get_non_empty_input("Enter student name: ")
        students = manager.search_by_name(name)

        if students:
            display_students(students)
        else:
            print("\nNo matching students found.")


def update_student(manager):
    """Update details of an existing student."""
    display_header("UPDATE STUDENT")

    student_id = get_non_empty_input("Enter student ID: ")
    student = manager.find_by_id(student_id)

    if not student:
        print("No student found with that ID.")
        return

    print("\nCurrent details:")
    display_student(student)

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Age")
    print("3. Course")
    print("4. Marks")
    print("5. Update all fields")
    print("6. Cancel")

    choice = get_integer_input(
        "Enter your choice: ",
        minimum=1,
        maximum=6
    )

    if choice == 6:
        print("Update cancelled.")
        return

    if choice == 1:
        name = get_non_empty_input("Enter new name: ")
        manager.update_student(student_id, name=name)

    elif choice == 2:
        age = get_integer_input(
            "Enter new age: ",
            minimum=1,
            maximum=100
        )
        manager.update_student(student_id, age=age)

    elif choice == 3:
        course = get_non_empty_input("Enter new course: ")
        manager.update_student(student_id, course=course)

    elif choice == 4:
        marks = get_float_input(
            "Enter new marks: ",
            minimum=0,
            maximum=100
        )
        manager.update_student(student_id, marks=marks)

    elif choice == 5:
        name = get_non_empty_input("Enter new name: ")
        age = get_integer_input(
            "Enter new age: ",
            minimum=1,
            maximum=100
        )
        course = get_non_empty_input("Enter new course: ")
        marks = get_float_input(
            "Enter new marks: ",
            minimum=0,
            maximum=100
        )

        manager.update_student(
            student_id,
            name=name,
            age=age,
            course=course,
            marks=marks
        )

    print("Student updated successfully.")


def delete_student(manager):
    """Delete a student after confirmation."""
    display_header("DELETE STUDENT")

    student_id = get_non_empty_input("Enter student ID: ")
    student = manager.find_by_id(student_id)

    if not student:
        print("No student found with that ID.")
        return

    print("\nStudent to be deleted:")
    display_student(student)

    if confirm_action("Are you sure you want to delete this student?"):
        manager.delete_student(student_id)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def show_statistics(manager):
    """Display student statistics and sorting options."""
    display_header("STUDENT STATISTICS")

    students = manager.get_all_students()

    if not students:
        print("No student records available.")
        return

    average = manager.calculate_average_marks()
    top_student = manager.get_top_student()

    print(f"Total Students   : {len(students)}")
    print(f"Average Marks    : {average:.2f}")

    if top_student:
        print(
            f"Top Student      : "
            f"{top_student.name} ({top_student.marks:.2f})"
        )

    print("\n1. Sort by Name")
    print("2. Sort by Marks")
    print("3. Return")

    choice = get_integer_input(
        "Enter your choice: ",
        minimum=1,
        maximum=3
    )

    if choice == 1:
        display_students(manager.sort_by_name())

    elif choice == 2:
        display_students(manager.sort_by_marks())


def display_menu():
    """Display the main application menu."""
    print("\n")
    print("=" * 55)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")
    print("=" * 55)


def main():
    """Run the Student Management System."""
    manager = StudentManager()

    while True:
        display_menu()

        choice = get_integer_input(
            "Enter your choice: ",
            minimum=1,
            maximum=7
        )

        if choice == 1:
            add_student(manager)

        elif choice == 2:
            view_students(manager)

        elif choice == 3:
            search_student(manager)

        elif choice == 4:
            update_student(manager)

        elif choice == 5:
            delete_student(manager)

        elif choice == 6:
            show_statistics(manager)

        elif choice == 7:
            print("\nThank you for using the Student Management System.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()