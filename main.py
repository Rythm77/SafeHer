import datetime

contacts = {
    "Police": "112",
    "Women Helpline": "181",
    "Ambulance": "108"
}
sos_history = []
incident_history = []


def main():
    while True:
        show_header()
        show_menu()
        command = input("Select an option: ").strip().upper()
        if command == "SOS":
            emergency_sos()
        elif command == "REPORT":
            report_incident()
        elif command == "CONTACT":
            show_contacts()
        elif command == "HISTORY":
            show_history()
        elif command == "TIPS":
            safety_tips()
        elif command == "TIME":
            show_time()
        elif command == "EXIT":
            print()
            print("=" * 60)
            print("SAFEGUARD SYSTEM CLOSED")
            print("=" * 60)
            print("STAY SAFE - STAY ALERT")
            print("=" * 60)
            break
        else:
            print()
            print("Unknown command.")
            print()
            print("Available commands:")
            print("SOS")
            print("REPORT")
            print("CONTACT")
            print("HISTORY")
            print("TIPS")
            print("TIME")
            print("EXIT")
        input("\nPress ENTER to continue...")


def show_header():
    print()
    print("=" * 60)
    print("                  S A F E G U A R D")
    print("                 WOMEN SAFETY SYSTEM")
    print("=" * 60)
    print("          DETECT | DOCUMENT | ESCALATE | PROTECT")
    print("=" * 60)


def show_menu():
    print()
    print("+----------------------------------------------------------+")
    print("|                  SAFETY COMMAND CENTER                  |")
    print("+----------------------------------------------------------+")
    print("|                                                          |")
    print("|   SOS       - Emergency SOS Alert                       |")
    print("|   REPORT    - Report Suspicious Activity                |")
    print("|   CONTACT   - Emergency Contacts                        |")
    print("|   HISTORY   - Incident and SOS History                  |")
    print("|   TIPS      - Safety Guidelines                         |")
    print("|   TIME      - Current Date and Time                     |")
    print("|   EXIT      - Close System                              |")
    print("|                                                          |")
    print("+----------------------------------------------------------+")


def get_time():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def show_contacts():
    print()
    print("=" * 60)
    print("                   EMERGENCY CONTACTS")
    print("=" * 60)
    print()
    for name, number in contacts.items():
        print(f"{name:<20} : {number}")
    print()
    print("In a real emergency, contact the appropriate")
    print("emergency service immediately.")


def safety_tips():
    tips = [
        "Keep your phone charged and accessible.",
        "Share your travel plans with a trusted person.",
        "Avoid isolated places whenever possible.",
        "Keep emergency numbers easily accessible.",
        "Move towards a safe and populated location.",
        "Do not confront or chase an unknown person.",
        "Contact emergency services during immediate danger."
    ]
    print()
    print("=" * 60)
    print("                    SAFETY GUIDELINES")
    print("=" * 60)
    for number, tip in enumerate(tips, 1):
        print(f"{number}. {tip}")


def emergency_sos():
    print()
    print("=" * 60)
    print("                       SOS MODE")
    print("=" * 60)
    print()
    print("Please enter the following information.")
    print()

    name = input("Name: ").strip()
    location = input("Current Location: ").strip()
    reason = input("Emergency Reason: ").strip()

    if name == "":
        name = "Unknown User"

    if location == "":
        location = "Location Not Provided"

    if reason == "":
        reason = "Emergency Assistance Required"

    print()
    print("-" * 60)
    print("                    SOS CONFIRMATION")
    print("-" * 60)
    print()
    print("Name     :", name)
    print("Location :", location)
    print("Reason   :", reason)

    confirmation = input("\nType CONFIRM to activate SOS: ").strip().upper()

    if confirmation != "CONFIRM":
        print()
        print("SOS Alert cancelled.")
        return

    alert_time = get_time()
    alert = {
        "name": name,
        "location": location,
        "reason": reason,
        "time": alert_time
    }

    sos_history.append(alert)
    with open("SOS_Report", "a") as file:
        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("                 SAFEGUARD SOS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Name: {name}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Reason: {reason}\n")
        file.write(f"Alert Time: {alert_time}\n")
        file.write("=" * 60 + "\n")

    print()
    print("=" * 60)
    print("                SOS ALERT GENERATED")
    print("=" * 60)

    print()
    print("EMERGENCY ASSISTANCE REQUESTED!")

    print()
    print("Name       :", name)
    print("Location   :", location)
    print("Reason     :", reason)
    print("Alert Time :", alert_time)

    print()
    print("EMERGENCY NUMBERS")
    print("-" * 30)
    print("Police          : 112")
    print("Women Helpline  : 181")
    print("Ambulance       : 108")

    print()
    print("[OK] SOS recorded in history")
    print("[OK] Report saved as SOS_Report.txt")

    print()
    print("NOTE: This is an SOS simulation.")
    print("It does not automatically call or message")
    print("emergency services.")


def report_incident():
    print()
    print("=" * 60)
    print("              SUSPICIOUS ACTIVITY REPORT")
    print("=" * 60)
    print()
    print("Describe only what you actually observed.")
    print("Do not confront or chase an unknown person.")
    print()
    person = input("Person Description: ").strip()
    location = input("Location: ").strip()
    activity = input("What Happened?: ").strip()

    print()
    print("RISK LEVEL")
    print("-" * 40)
    print()
    print("[LOW]")
    print("Unusual activity with no immediate danger.")
    print()
    print("[SUSPICIOUS]")
    print("Concerning or repeated unwanted behaviour.")
    print()
    print("[DANGER]")
    print("Immediate threat or emergency.")
    risk = input("\nSelect Risk Level: ").strip().upper()

    if risk not in ["LOW", "SUSPICIOUS", "DANGER"]:
        print()
        print("Invalid risk level.")
        print("Incident was not recorded.")
        return

    if person == "":
        person = "Description Not Provided"

    if location == "":
        location = "Location Not Provided"

    if activity == "":
        activity = "Activity Not Provided"

    incident_time = get_time()

    incident = {
        "person": person,
        "location": location,
        "activity": activity,
        "risk": risk,
        "time": incident_time
    }

    incident_history.append(incident)
    with open("Incident_Report.txt", "a") as file:
        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("              SAFEGUARD INCIDENT REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Person Description: {person}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Observed Activity: {activity}\n")
        file.write(f"Risk Level: {risk}\n")
        file.write(f"Time: {incident_time}\n")
        file.write("=" * 60 + "\n")

    print()
    print("=" * 60)
    print("                  RESPONSE ACTIVATED")
    print("=" * 60)

    if risk == "LOW":
        print()
        print("LOW RISK")
        print()
        print("Recommended Response:")
        print("- Stay aware of your surroundings.")
        print("- Avoid unnecessary interaction.")
        print("- Move to a safe location if needed.")
        print("- Incident has been documented.")

    elif risk == "SUSPICIOUS":
        print()
        print("SUSPICIOUS ACTIVITY")
        print()
        print("Recommended Response:")
        print("- Move to a safe and populated location.")
        print("- Inform a trusted person or security personnel.")
        print("- Do not confront the person.")
        print("- Keep the incident details recorded.")
        print("- Contact emergency services if danger increases.")

    elif risk == "DANGER":
        print()
        print("IMMEDIATE DANGER")
        print()
        print("PRIORITY RESPONSE")
        print("- Move to a safe location immediately.")
        print("- Do NOT confront or chase the person.")
        print("- Contact Police: 112")
        print("- Women Helpline: 181")
        print("- Ambulance: 108")
        print("- Inform security personnel if available.")

    print()
    print(" Incident recorded successfully.")
    print(" Report saved as Incident_Report")


def show_history():
    print()
    print("=" * 60)
    print("                 SAFETY ACTIVITY HISTORY")
    print("=" * 60)
    print()
    print("---------------- SOS ALERTS ----------------")
    print()
    if len(sos_history) == 0:
        print("No SOS alerts in this session.")
    else:
        for number, alert in enumerate(sos_history, 1):
            print("-" * 50)
            print(f"SOS ALERT #{number}")
            print("-" * 50)
            print("Name     :", alert["name"])
            print("Location :", alert["location"])
            print("Reason   :", alert["reason"])
            print("Time     :", alert["time"])
    print()
    print("------------- INCIDENT REPORTS -------------")
    print()
    if len(incident_history) == 0:
        print("No incidents in this session.")
    else:
        for number, incident in enumerate(incident_history, 1):
            print("-" * 50)
            print(f"INCIDENT #{number}")
            print("-" * 50)
            print("Person   :", incident["person"])
            print("Location :", incident["location"])
            print("Activity :", incident["activity"])
            print("Risk     :", incident["risk"])
            print("Time     :", incident["time"])


def show_time():
    now = datetime.datetime.now()
    print()
    print("=" * 60)
    print("                 CURRENT DATE & TIME")
    print("=" * 60)
    print()
    print("Date :", now.strftime("%d-%m-%Y"))
    print("Time :", now.strftime("%H:%M:%S"))


if __name__ == "__main__":
    main()
