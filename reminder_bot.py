import time
from datetime import datetime, timedelta
from plyer import notification

# Function to convert the date string into a datetime object
def parse_date(day, month, year, hour, minute):
    try:
        return datetime(year, month, day, hour, minute)
    except ValueError as e:
        print(f"\033[91mError parsing the date: {e}\033[0m")
        return None

# Function to add a reminder
def add_reminder(reminders, reminder_text, reminder_time, repeat):
    reminder = {"text": reminder_text, "time": reminder_time, "repeat": repeat}
    reminders.append(reminder)

# Function to remove a reminder
def remove_reminder(reminders, index):
    try:
        reminders.pop(index)
        print("\033[92mReminder removed successfully.\033[0m")
    except IndexError:
        print("\033[91mError: Reminder not found.\033[0m")

# Function to check and display reminders
def check_reminders(reminders):
    while True:
        now = datetime.now()
        for reminder in reminders[:]:
            if reminder["time"] <= now:
                notification.notify(
                    title="Reminder",
                    message=reminder["text"],
                    timeout=10  # Notification will last 10 seconds
                )
                
                if reminder["repeat"]:
                    reminder["time"] = reminder["time"] + timedelta(minutes=10)  # Repeat every 10 minutes
                else:
                    reminders.remove(reminder)  # Remove the reminder after it has been triggered
        time.sleep(60)  # Check every minute

# Function to display the main menu
def show_main_menu():
    print("\n\033[95m====================================\033[0m")
    print("\033[94mWelcome to the Reminder Bot!\033[0m")
    print("\033[92mPlease select an option:\033[0m")
    print("1. Create a new reminder")
    print("2. View my reminders")
    print("3. Remove a reminder")
    print("4. Exit")
    print("\033[95m====================================\033[0m")

# Main function
def main():
    reminders = []

    while True:
        show_main_menu()

        option = input("\033[93mEnter an option (1-4): \033[0m")
        
        if option == "1":
            # Create a new reminder
            print("\n\033[96mCreating a new reminder...\033[0m")
            reminder_text = input("\033[94mEnter the reminder text: \033[0m")
            if reminder_text.lower() == "exit":
                break

            try:
                # Input date
                day = int(input("\033[94mEnter the day of the reminder (1-31): \033[0m"))
                month = int(input("\033[94mEnter the month of the reminder (1-12): \033[0m"))
                year = int(input("\033[94mEnter the year of the reminder (e.g., 2024): \033[0m"))
                hour = int(input("\033[94mEnter the hour of the reminder (0-23): \033[0m"))
                minute = int(input("\033[94mEnter the minutes of the reminder (0-59): \033[0m"))
                
                reminder_time = parse_date(day, month, year, hour, minute)
                if reminder_time is None:
                    continue  # If the date is invalid, show the menu again

                # Check if the reminder is repetitive
                repeat_input = input("\033[94mIs the reminder repetitive every 10 minutes? (yes/no): \033[0m").lower()
                repeat = repeat_input == "yes"

                # Add the reminder
                add_reminder(reminders, reminder_text, reminder_time, repeat)
                print(f"\033[92mReminder added: '{reminder_text}' for {reminder_time}\033[0m")
                
                time.sleep(1)

            except Exception as e:
                print(f"\033[91mError adding the reminder. Make sure the data is correct: {e}\033[0m")
                continue

        elif option == "2":
            # View reminders
            if reminders:
                print("\n\033[93mYour current reminders are:\033[0m")
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['text']} - {reminder['time']}")
            else:
                print("\033[91mYou have no reminders at the moment.\033[0m")
            time.sleep(1)

        elif option == "3":
            # Remove a reminder
            if reminders:
                print("\n\033[93mSelect the number of the reminder you want to remove or type 'cancel' to return to the menu:\033[0m")
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['text']} - {reminder['time']}")
                user_input = input("\033[94mNumber of the reminder to remove: \033[0m")
                
                if user_input.lower() == "cancel":
                    print("\033[91mRemoval operation canceled.\033[0m")
                    continue
                
                try:
                    reminder_idx = int(user_input) - 1
                    remove_reminder(reminders, reminder_idx)
                except ValueError:
                    print("\033[91mPlease enter a valid number.\033[0m")
            else:
                print("\033[91mYou have no reminders to remove.\033[0m")
            time.sleep(1)

        elif option == "4":
            # Exit the program
            print("\033[92mThank you for using the Reminder Bot! See you soon.\033[0m")
            break

        else:
            print("\033[91mInvalid option. Please enter a valid option (1-4).\033[0m")
            time.sleep(1)

    # Start checking reminders (this will execute after exiting the main menu)
    check_reminders(reminders)

if __name__ == "__main__":
    main()
