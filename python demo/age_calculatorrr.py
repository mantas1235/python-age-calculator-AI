from datetime import datetime

# Ask the user to enter their birth date
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")

# Convert input string to a date object
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

# Get today's date
today = datetime.today()

# Calculate age
age = today.year - birth_date.year

# Adjust if the birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Print result
print(f"You are {age} years old.")

if age < 18:
    print("You are underage.")
else:
    print("You are not underage.")