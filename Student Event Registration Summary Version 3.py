# Version 3 : Added date formatting
from datetime import datetime


def registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    section = input("Enter your section: ")
    event_name = input("Enter the name of event: ")
    event_year = int(input("Enter the year of the event: "))
    event_month = int(input("Enter the month of the event: "))
    event_day = int(input("Enter the day of the event: "))

    clean_firstname = first_name.strip().title()
    clean_lastname = last_name.strip().title()
    full_name = f"{clean_firstname} {clean_lastname}".strip()
    name_code = full_name.upper()
    clean_section = section.strip().upper()
    clean_eventname = event_name.strip().title()

    date_formatting = datetime(event_year, event_month, event_day)
    formatted_date = f"{date_formatting.strftime('%B')} {date_formatting.day}, {date_formatting.year}"

    clean_language = "Python".strip().title()
    sfeatures_used = "strip(), title(), upper()"
    dfeatures_used = "datetime"

    print("\nStudent Event Registration Summary")
    print("Name:", full_name)
    print("Name Code:", name_code)
    print("Section:", clean_section)
    print("Event:", clean_eventname)
    print("Event Date:", formatted_date)
    print("Language Used:", clean_language)
    print("String Feature Used:", sfeatures_used)
    print("Date/Time Features Used:", dfeatures_used)
    print("\nRegistration record created successfully.")


registration()
