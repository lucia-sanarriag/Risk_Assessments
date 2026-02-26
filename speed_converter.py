# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

START_SPEED = 60            # Starting speed
END_SPEED = 131             # Ending speed
INCREMEMT = 10              # Speed increment
CONVERSION_FACTOR = 0.6214  # Conversion factor

# Print the table headings.
print('KPH\tMPH')
print('--------------')

# Print the table headings.
for kph in range(START_SPEED, END_SPEED, INCREMEMT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')
