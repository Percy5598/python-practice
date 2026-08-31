study_hours = [2, 4, 3, 5, 1, 4, 6]
total_hours = 0
count = 0
for hours in study_hours:
    total_hours += hours
    if hours > 4:
        count += 1
print(f"Total study hours: {total_hours}")
print (f"Study days: {len(study_hours)} days")
print (f"Average study hours: {total_hours / len(study_hours):.2f} hours/day")
print (f"Days with more than 4 hours of study: {count}")    

total_hours = 0
study_days = 0

while True:
    hours = float(input("How many hours did you study today? "))

    # Stop the program
    if hours == 0:
        break

    # Reject negative numbers
    if hours < 0:
        print("Hours cannot be negative.")
        continue

    # Add the study hours
    total_hours += hours
    study_days += 1

    # Classify the study day
    if hours <= 2:
        print("Needs improvement")
    elif hours <= 4:
        print("Good")
    else:
        print("Excellent")

# Calculate and display results
if study_days > 0:
    average_hours = total_hours / study_days

    print("\n--- Study Summary ---")
    print(f"Study days: {study_days}")
    print(f"Total hours: {total_hours}")
    print(f"Average hours: {average_hours:.2f}")

    # Check YKI study target
    if average_hours >= 4:
        print("Great! You are meeting your 4-hour study target.")
    else:
        print("Try to increase your daily study time.")
else:
    print("No study days recorded.")

