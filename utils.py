def get_non_empty_input(prompt):
    """Get a non-empty string from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer_input(prompt, minimum=None, maximum=None):
    """Get a valid integer within an optional range."""
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_float_input(prompt, minimum=None, maximum=None):
    """Get a valid floating-point number within an optional range."""
    while True:
        try:
            value = float(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def confirm_action(prompt):
    """Ask the user to confirm an action."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter 'y' or 'n'.")