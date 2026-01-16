# Vacuum Cleaner Problem using Simple Reflex Agent

# 0 -> Clean, 1 -> Dirty
environment = {
    'A': 1,
    'B': 1
}

current_location = 'A'

print("Initial Environment Status:")
print(environment)
print("Vacuum Cleaner is at location:", current_location)
print("-" * 40)

while environment['A'] == 1 or environment['B'] == 1:

    # If current room is dirty, clean it
    if environment[current_location] == 1:
        print(f"Room {current_location} is Dirty. Performing SUCK operation.")
        environment[current_location] = 0
        print(f"Room {current_location} is now Clean.")

    # Move to the other room
    if current_location == 'A':
        print("Moving RIGHT to Room B.")
        current_location = 'B'
    else:
        print("Moving LEFT to Room A.")
        current_location = 'A'

    print("Current Environment Status:", environment)
    print("-" * 40)

print("All rooms are clean. Goal achieved!")
