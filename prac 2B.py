# Initialize variables
day = 1
total_downtime = 0
downtime_list = []

# Collect input for 7 days
while day <= 7:
    hours = float(input(f"Enter load shedding hours for day {day}: "))
    downtime_list.append(hours)
    total_downtime += hours
    day += 1
print()
# Calculate average
average_downtime = total_downtime / 7

# Print total and average
print("-------------------------------------------------------------")
print(f"Total load shedding over 7 days: {total_downtime} hours")
print(f"Average daily load shedding: {average_downtime:.2f} hours")
print()
# Print days with more than 5 hours
print("-------------------------------------------------------------")
print("Days with more than 5 hours of load shedding:")
day = 1
while day <= 7:
    if downtime_list[day - 1] > 5:
        print(f"Day {day}: {downtime_list[day - 1]} hours")
    day += 1


