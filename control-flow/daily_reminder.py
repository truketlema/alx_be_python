# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Modify reminder if time-bound or low-priority non-time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print(reminder)

