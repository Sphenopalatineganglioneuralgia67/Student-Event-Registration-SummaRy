# Version 2 : Added string formatting

def registration():
    first_name = input("Enter your first name: ")
    last_name = input ("Enter your last name: ")
    section = input("Enter your section: ")
    event_name = input("Enter the name of event: ")
    event_year = input("Enter the year of the event: ")
    event_month = input("Enter the month of the event: ")
    event_day = input("Enter the day of the event: ")
   
    clean_firstname = first_name.strip().title()
    clean_lastname = last_name.strip().title()
    full_name = f" {clean_firstname} {clean_lastname}".strip()
    name_code = full_name.upper()
    clean_section = section.upper()
    clean_eventname = event_name.strip().title()
    event_date = event_day + " " + event_month + " " + event_year
    clean_language = "Python".strip().title()
    sfeatures_used = "strip() title() upper()"
    dfeatures_used = "none".strip().title()

    print("\n Student Event Registration Summary")
    print("Name: ", full_name)
    print("Name Code: ", name_code)
    print("Section:", section)
    print("Event: ", clean_eventname)
    print("Event Date: ", event_date)
    print("Language Used: ", clean_language)
    print("String Feature Used: ", sfeatures_used)
    print("Date/Time Features Used: ", dfeatures_used)

    print("\n Registration record created successfully")

registration() 
