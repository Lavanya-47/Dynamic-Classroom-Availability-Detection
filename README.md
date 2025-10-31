# 🧠 Dynamic Classroom Availability Detection Using Real-Time Data Analysis

## 📘 Project Overview
This project aims to automatically detect and display **real-time classroom availability** using timetable data.  
It helps students and faculty quickly identify which classrooms are **free or occupied**, reducing manual searching and improving space utilization.

## 📁 Project Structure
Dynamic-Classroom-Availability-Detection/
│
├── code/
│   └── app.py
│
├── database/
│   └── dynamic.sql
│
├── data/
│   └── timetable.xlsx
│
└── README.md



## ⚙️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Python (Flask Framework)  
- **Database:** MySQL  
- **Libraries:** Pandas, mysql-connector-python, datetime  
- **Data Source:** Excel files (.xlsx) containing timetable data  



## 🏗️ System Architecture
The system follows a **three-tier architecture**:
1. **Frontend Layer** – Web interface for displaying classroom status  
2. **Backend Layer** – Flask server handling logic and data processing  
3. **Database Layer** – MySQL storing timetable and classroom details  



## 🔄 Workflow
1. Timetable data from Excel sheets is imported into MySQL using SQL scripts.  
2. Flask connects to the database and retrieves class schedules.  
3. The system compares the current day and time with timetable entries.  
4. Classrooms are marked as **Available** or **Occupied** dynamically.  
5. The results are displayed on the web page using Flask’s Jinja2 templates.


## 🧰 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/dynamic-classroom.git
   cd dynamic-classroom

2. Install dependencies

pip install flask mysql-connector-python pandas


3. Import database schema

source dynamic.sql;


4. Update database credentials in app.py

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="dynamic_classroom"
)

5. Run the application

python app.py

6. Access the app

http://127.0.0.1:5000/


# 🧩 Core Logic

from datetime import datetime

current_time = datetime.now().time()
current_day = datetime.now().strftime('%A')

# Fetch timetable entries from MySQL
cursor.execute("SELECT * FROM timetable WHERE day = %s", (current_day,))
for record in cursor.fetchall():
    if start_time <= current_time <= end_time:
        status = "Occupied"
    else:
        status = "Available"


# 🖥️ Output

Displays a list of classrooms with their real-time status:

🟢 Available

🔴 Occupied


# 🚀 Features

Real-time classroom availability detection

Dynamic data analysis using current date/time

Database-driven system (MySQL)

Clean and responsive UI with Bootstrap

Modular Flask architecture


# 💡 Future Enhancements

Integrate IoT sensors for actual room occupancy detection

Add auto-refresh or live updates using AJAX/WebSockets

Develop a mobile app version

Implement search and filter features by department or time
