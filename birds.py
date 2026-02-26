# This program demonstrates two function that
# have local variables with same name.

def main():
    # Call the texas function.
    texas()
    # Call the californai function.
    california()

# Definition of the texas function. It creates
# a local vairable named birds.


def texas():
    birds = 5000
    print(f'texas has {birds} birds.')

# Definition of the california function. It also
# creates a local vairable named birds.


def california():
    birds = 8000
    print(f'california has {birds} birds.')

# Call the main function.


main()