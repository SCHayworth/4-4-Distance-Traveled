# Program 4-4 Distance Traveled
# Shaun Hayworth
# CIS 2
# 10-20-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-4-Distance-Traveled

# Gets the speed of a vehicle and the total time of travel from the user and displays the total distance
# traveled at each hour.

# Create a multiline header for output formatting.
header = '''
Hour            Distance Traveled
---------------------------------
'''

# Prompt the user for the vehicle's speed in mph
speed = int(input('What is the speed of the vehicle in mph? '))

# Prompt user for the total time of travel
time = int(input('How many hours has it traveled? '))

# Print the header
print(header)

# Calculate the total distance traveled at each hour of travel and display the results in two columns.
for hour in range(time):
    distance = hour * speed
    print(f'{hour:<10f} {distance:>10f}')
