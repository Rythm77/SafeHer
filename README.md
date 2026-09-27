#  Safeguard – Women Safety System

##  About the Project

**Safeguard – Women Safety System** is a beginner-level Python mini project developed as part of an **educational Vityarthi project**.

The main purpose of this project is to demonstrate how Python can be used to create a simple command-line safety assistance system. It provides features such as an SOS alert simulation, emergency contacts, suspicious activity reporting, safety guidelines, activity history, and current date and time.

> **Educational Purpose:**
> This project is created for learning and academic demonstration purposes as part of a Vityarthi/B.Tech CSE project. It is **not a replacement for real emergency services or professional safety applications.**

---

## Objectives

The main objectives of the project are:

* To develop a simple women safety assistance system using Python.
* To understand Python functions and conditional statements.
* To practice user input and menu-driven programming.
* To demonstrate the use of lists and dictionaries.
* To record SOS and incident information.
* To provide easily accessible emergency contact numbers.
* To demonstrate basic file handling in Python.
* To understand how a real-world problem can be approached using programming.

---

##  Features

### 1. SOS Emergency Alert

The SOS feature allows the user to enter:

* Name
* Current location
* Emergency reason

The system asks the user to type `CONFIRM` before generating the SOS alert.

The alert contains the user's information, emergency reason, and the current date and time. The SOS information is also stored in the application's session history and written to a report file.

**Important:** The SOS feature is a **simulation only**. It does not automatically call, SMS, or notify emergency services.

---

### 2.  Emergency Contacts

The system displays emergency numbers including:

| Service        | Number |  
| -------------- | -----: |  
| Police         |    112 |  
| Women Helpline |    181 |  
| Ambulance      |    108 |  

The project stores these contacts using a Python dictionary.

---

### 3.  Suspicious Activity Report

Users can report suspicious activity by entering:

* Person description
* Location
* Observed activity
* Risk level

The available risk levels are:

* `LOW`
* `SUSPICIOUS`
* `DANGER`

The system provides different recommended responses depending on the selected risk level.

The incident is also stored in the session history and saved to an incident report file.

---

### 4.  Safety Activity History

The `HISTORY` option displays:

* Previous SOS alerts during the current session
* Previous incident reports during the current session

This allows users to review information entered while the program is running.

---

### 5.  Safety Guidelines

The project provides basic safety guidelines such as:

* Keeping the phone charged and accessible.
* Sharing travel plans with a trusted person.
* Avoiding isolated places whenever possible.
* Keeping emergency numbers easily accessible.
* Moving towards a safe and populated location.
* Avoiding confrontation with unknown people.
* Contacting emergency services during immediate danger.

---

### 6.  Date and Time

The `TIME` option displays the current date and time using Python's built-in `datetime` module.

The same module is used to record the time when an SOS alert or incident report is created.

---

##  Technologies Used

* **Python 3**
* **datetime module**
* Python dictionaries
* Python lists
* Functions
* Conditional statements
* Loops
* User input
* File handling

No external Python libraries are required for the current version.

---

##  Project Structure

```text
Women-Safety-System/
│
├── main.py  
├── README.md  
├── STATEMENT.md  
│
├── SOS_Report.txt  
└── Incident_Report.txt  
```

> The report files are generated when SOS alerts or incident reports are recorded.

---

##  How to Run

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the repository

```bash
git clone <your-github-repository-url>
```

### Step 3: Open the project folder

```bash
cd Women-Safety-System
```

### Step 4: Run the program

```bash
python main.py
```

---

##  Available Commands

After starting the program, the following options are available:

```text
SOS       - Emergency SOS Alert
REPORT    - Report Suspicious Activity
CONTACT   - Emergency Contacts
HISTORY   - Incident and SOS History
TIPS      - Safety Guidelines
TIME      - Current Date and Time
EXIT      - Close System
```

---

##  Generated Reports

### SOS Report

When an SOS simulation is confirmed, the system saves information such as:

```text
Name
Location
Reason
Alert Time
```

to `SOS_Report.txt`.

### Incident Report

When a suspicious activity report is submitted, the system saves:

```text
Person Description
Location
Observed Activity
Risk Level
Time
```

to `Incident_Report.txt`.

---

##  Disclaimer

This project is developed **strictly for educational and academic purposes** as a **Vityarthi/B.Tech CSE mini project**.

The SOS functionality is a simulation and **does not automatically contact police, ambulance services, women helplines, or any other emergency service**.

The emergency numbers displayed by the project are provided for educational demonstration. Users should verify appropriate emergency services and numbers for their location in a real emergency.

The project should not be considered a professional emergency response system.

---

##  Future Scope

The project can be improved in the future by adding:

* Graphical User Interface (GUI)
* GPS-based location detection
* SMS notifications
* Automated emergency calling
* Trusted contact management
* User authentication
* Database integration
* Mobile application support
* Cloud-based incident storage
* Real-time location sharing

These features would require additional technologies, APIs, security measures, and appropriate testing.

---

##  Project Type

**Project:** Women Safety System
**Level:** Beginner / Mini Project
**Technology:** Python
**Purpose:** Educational / Academic
**Platform:** Vityarthi / B.Tech CSE

---

##  License

This project is intended primarily for educational use. You may modify and use the code for learning and academic purposes.

