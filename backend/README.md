# HRMS Lite - Human Resource Management System

A lightweight, full-stack Human Resource Management System designed to simplify employee tracking and attendance management. This application was built as part of a Full-Stack Coding Assignment.

## 🚀 Live Demo
- **Live Application:** https://hrms-lite-app-7m04.onrender.com/
- **GitHub Repository:** https://github.com/ANKISH1/HRMS-Lite-Final

---

## 🛠️ Tech Stack
- **Backend:** Python (Django 5.0)
- **Database:** PostgreSQL (Production), SQLite (Local)
- **Frontend:** Django Templates (HTML5, CSS3, JavaScript)
- **Deployment:** Render (Web Service + PostgreSQL)
- **Styling:** Custom CSS / Bootstrap

---

## 📋 Features
### 1. Employee Management
- **View Employees:** See a list of all active employees.
- **Add Employee:** Form to add new staff (ID, Name, Email, Department).
- **Delete Employee:** Remove records instantly.
- **Validation:** Prevents duplicate Employee IDs and Emails.

### 2. Attendance Management
- **Mark Attendance:** Log daily status (Present/Absent).
- **History:** View past attendance records.
- **Date Tracking:** Automatically records the date of entry.

## 🔑 Admin Access
To access the admin panel and manage employee data:
- **Login URL:** [PASTE YOUR RENDER URL HERE]/admin
- **Username:** `admin2`
- **Password:** `admin123`

*Note: Please use these credentials to test the backend management features.*

---

## ⚙️ How to Run Locally

If you want to run this project on your own machine:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/ANKISH1/HRMS-Lite-Final.git](https://github.com/ANKISH1/HRMS-Lite-Final.git)
   cd HRMS-Lite-Final

2. **Create a Virtual Environment**
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

Install Dependencies
pip install -r backend/hrmslite/requirements.txt

Apply Migrations
cd backend/hrmslite
python manage.py migrate

Create Admin User
python manage.py createsuperuser

Run Server
python manage.py runserver

Access the app at http://127.0.0.1:8000

📝 Assumptions & Limitations
Single Admin: The system is designed for a single administrator. Authentication is handled via the Django Admin panel.

Deployment: The app is hosted on Render's free tier, so it may take 30-50 seconds to wake up after inactivity.


### **Step 3: Push to GitHub**
Once you have saved the file with your links:

1.  Open your terminal.
2.  Run:
    ```bash
    git add README.md
    git commit -m "Added project documentation"
    git push origin main
    ```

### **Step 4: Verify**
Go to your GitHub repository page. You should now see this beautiful documentation displayed right on the front page.

**You are done!** You have a deployed app, a working database, correct code structure, and professional documentation. Good luck with the submission!