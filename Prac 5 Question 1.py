### Q1: A
def reverse_text(text):
    return text[::-1]


def process_name(first_name, last_name):
    """Function to process first and last name"""
    return first_name + " " + last_name


# Question 1:C
def main():
    # Ask the user for input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Use the function from name_processor.py
    full_name = process_name(first_name, last_name)
    print("Your full name is:", full_name)

    # Use the function from text_reverser.py
    reversed_name = reverse_text(full_name)
    print("Your reversed full name is:", reversed_name)


def process_name(first_name, last_name):
    return first_name + " " + last_name


def reverse_text(text):
    return text[::-1]


main()
