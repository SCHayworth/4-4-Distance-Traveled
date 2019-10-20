# Scope
The distane a vehicle travles can be calculated as follows:

    distance = speed * time

For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles. Write a program that asks for the speed of a vehicle (in miles per hour) and the number of hours it has traveled.  It should then use a loop to display the distance the vehicle has traveled for each hour during that time period.

### Example Run
    What is the speed of the vehicle in mph? 40
    How many hours has it traveled? 3
    Hour                Distance Traveled
    -------------------------------------
    1                           40
    2                           80
    3                          120

# Pseudocode
    START
    Set header template string to the following:
        Hour                Distance Traveled
        -------------------------------------
        
    Prompt user for the speed in mph
    Prompt user for the total hours traveled
    Print underline characters
    FOR each hour traveled
        on each line:
            print hour
            print distance traveled = speed * hour
    END
