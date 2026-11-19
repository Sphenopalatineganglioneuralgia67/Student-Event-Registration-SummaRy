# Version 1:
def registration():
    first_name = input("Enter your first name: ")
    last_name = input ("Enter your last name: ")
    section = input("Enter your section: ")
    event_name = input("Enter the name of event: ")
    event_year = input("Enter the year of the event: ")
    event_month = input("Enter the month of the event: ")
    event_day = input("Enter the day of the event: ")
   

    full_name = first_name + " " + last_name
    event_date = event_day + " " + event_month + " " + event_year
    language_used = "Python"
    string_features = "none yet"
    date_features = "none yet"

    print("\n Student Event Registration Summary")
    print("Name: ", full_name)
    print("Name Code: ",  full_name)
    print("Section:", section)
    print("Event:", event_date)
    print("Language Used:", language_used )
    print("String Feature Used:", string_features )
    print("Date/Time Features Used:", date_features)

registration()
