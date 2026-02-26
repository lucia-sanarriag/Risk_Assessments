# Named constants to represent the base hours and
# the overtime multiplioer.
BASE_HOURS = 40      # Base hours per week
OT_MULTIPLIER = 1.5  # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the mumber of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print(f'The gross pay is ${gross_pay:,.2f}.')
