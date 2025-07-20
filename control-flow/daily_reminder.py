task = input("Enter a your task: ")
time_bound = input("Is the task time-bound? (yes or no): " 
priority = input("What's the task's priority? ,(high/medium/low): ").lower()

reminder_message = [f"'{task}' is a "]

match priority:
  case "high":
    reminder_message.append("high priority task ")
  case "medium":
    reminder_message.append("medium priority task ")
  case "low":
    reminder_message.append("low priority task ")
  case _:
    reminder_message.append("task lacks priority")
    print("Error: invalid priority")

if time_bound == "yes":
  reminder_message.append("that requires immediate attention today!")
elif time_bound == "no" and priority == "low":
  reminder_message.append(". Consider completing it when you have free time.")
elif time_bound != "no":
  print("Invalid time bound input!")

if priority == "low" and time_bound == "no":
  print(f"Note: {''.join(reminder_message)}")
else:
  print(f"Reminder: {''.join(reminder_message)}")
