"""
Student Name: Lucia Santillan Arriaga
UTSA ID: vep381
Section: 901/902 Programming 1 lab 3
Description: Texas Road Trip Travel Calculator Game.
"""

# Constants - distances from San Antonio (in miles)
SAT_TO_CORPUS = 150
SAT_TO_HOUSTON = 200
SAT_TO_AUSTIN = 80
HOU_TO_GALVESTON = 50


def main():
    """Main Function"""

    # --- Player Input ---
    player_name = input("What is your name, traveler? ")

    print("Head to the dice generator and roll a number between 1 and 20.")
    roll = int(input("What did you roll? "))
    miles_rolled = roll * 10

    miles_remaining = miles_rolled
    total_distance = 0

    # --- Display destination menu ---
    print("\nWhere would you like to go?")
    print(f"  1. Corpus Christi - {SAT_TO_CORPUS} miles (BEACH!)")
    print(f"  2. Houston - {SAT_TO_HOUSTON} miles")
    print(f"  3. Austin - {SAT_TO_AUSTIN} miles")

    choice = int(input("Enter your choice (1-3): "))

    # --- Determine destination ---
    if choice == 1:
        destination = "Corpus Christi"
        miles_remaining -= SAT_TO_CORPUS
        total_distance = SAT_TO_CORPUS

        if miles_remaining >= 0:
            status = "WINNER"
        else:
            status = "SHORT"

    elif choice == 2:
        destination = "Houston"
        miles_remaining -= SAT_TO_HOUSTON
        total_distance = SAT_TO_HOUSTON

        if miles_remaining >= 0:
            continue_choice = input("Continue to Galveston? (y/n): ")

            if continue_choice == 'y' or continue_choice == 'Y':
                destination = "Galveston"
                miles_remaining -= HOU_TO_GALVESTON
                total_distance += HOU_TO_GALVESTON

                if miles_remaining >= 0:
                    status = "WINNER"
                else:
                    status = "SHORT"
            else:
                status = "STOPPED"
        else:
            status = "SHORT"

    elif choice == 3:
        destination = "Austin"
        miles_remaining -= SAT_TO_AUSTIN
        total_distance = SAT_TO_AUSTIN

        if miles_remaining >= 0:
            status = "DETOUR"
        else:
            status = "SHORT"

    else:
        destination = "Nowhere"
        total_distance = 0
        miles_remaining = miles_rolled
        status = "ERROR"
        print(f"Invalid Choice ({choice})")

    # --- Trip Summary ---
    print("\n" + "=" * 50)
    print("TRIP SUMMARY")
    print("=" * 50)
    print(f"Driver: {player_name}")
    print(f"Final Destination: {destination}")
    print(f"Total Distance: {total_distance} miles")
    print(f"Miles Rolled: {miles_rolled}")
    print(f"Miles Remaining: {miles_remaining}")
    print(f"Status: {status}")
    print("=" * 50)

    # --- Final Message ---
    if status == "WINNER":
        print("Enjoy the beach!")
    elif status == "SHORT":
        print("You ran out of miles. Try again!")
    elif status == "DETOUR":
        print("Austin is fun, but the beach is better!")
    else:
        print("Thanks for playing Texas Road Trip!")


if __name__ == "__main__":
    main()
