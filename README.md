




# 🗓️ Attendance Analytics System

A menu-driven command-line application built with **Python** and **Pandas** for recording, tracking, and analyzing student attendance — from daily entries to class-wide trends and low-attendance alerts.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 🚀 Overview

Attendance Analytics System is a lightweight, terminal-based tool for logging daily attendance and instantly surfacing insights — individual attendance percentages, students falling below the 75% threshold, and day-by-day presence trends — without touching a spreadsheet manually.

Built to be **crash-proof and data-safe**: every input is validated, duplicate entries are caught before they corrupt the record, and IDs are handled consistently whether they're loaded fresh from disk or entered live.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | ➕ **Add Attendance Record** | Log a student's daily status with full input validation |
| 2 | 👀 **View All Records** | Instantly view the complete attendance log |
| 3 | 🎯 **Student-wise Attendance** | Look up any student's total days, presents, absents, and attendance % |
| 4 | ⚠️ **Low Attendance List** | Flags every student below the 75% attendance threshold |
| 5 | 📅 **Date-wise Trend** | Shows Present/Absent counts for every recorded date |
| 6 | 🚪 **Exit** | Safely closes the session |

---

## 🛠️ Tech Stack

- **Python 3** — core logic
- **Pandas** — data storage, filtering & analysis
- **datetime** — strict date format validation

---

## 🧠 What Makes This Robust

- ✅ **Auto-recovery** — missing or empty `attendance.csv` is detected and a fresh file is created automatically
- ✅ **Strict date validation** — only valid `DD-MM-YYYY` dates are accepted; malformed or impossible dates (e.g. month 13) are rejected and re-prompted
- ✅ **Strict status validation** — only `Present` or `Absent` (case-insensitive) are accepted
- ✅ **Duplicate protection** — adding a record for a Student ID + Date that already exists triggers a confirmation prompt instead of silently duplicating data
- ✅ **Consistent ID handling** — Student IDs are always treated as text, even purely numeric ones (e.g. `123456`) — preventing a subtle bug where IDs loaded from disk (as numbers) would fail to match IDs typed live (as text), which silently broke duplicate detection and student lookups after a restart
- ✅ **Clean data separation** — only raw attendance data is ever written to disk
- ✅ **Full exception handling** — every menu action is wrapped so unexpected errors never crash the session

---

## 💻 Sample Run

```
************************************************
╔══════════════════════════════════════════════╗
║         ATTENDANCE ANALYTICS SYSTEM          ║
╚══════════════════════════════════════════════╝
************************************************

    Add Attendance Record        enter ---> 1
    View All Records             enter ---> 2
    Student-wise Attendance      enter ---> 3
    Low Attendance List (<75%)   enter ---> 4
    Date-wise Trend              enter ---> 5
    Exit                         enter ---> 6

************************************************

Enter your choice: 3
Enter Student ID: 123456

Student: charan
Total Days: 3
Present: 2
Absent: 1
Attendance: 66.67%
```

---

## ⚙️ Getting Started

**1. Install dependencies:**
```bash
pip install pandas
```

**2. Run the program:**
```bash
python attendance_analytics_system.py
```

That's it — no setup required. The program creates `attendance.csv` automatically on first run.

---

## 📁 Project Structure

```
📦 attendance-analytics-system
 ┣ 📜 attendance_analytics_system.py   # Main application
 ┣ 📜 attendance.csv                   # Auto-generated attendance log
 ┗ 📜 README.md                        # You are here
```

---

## 🧪 Testing

This project was manually tested end-to-end, covering:
- File auto-creation and empty-file recovery
- Date and status input validation
- Duplicate-record detection (including after a program restart, to catch ID type-mismatch issues)
- Student-wise lookups for both existing and unknown IDs
- Low-attendance flagging across multiple students and dates
- Date-wise trend accuracy across multiple records
- Invalid menu choices

---

## 👤 Author

**Charan**
Self-taught Python & Data Analysis Developer | Building real-world projects on the path to AI/ML freelancing

🔗 [GitHub](https://github.com/Charan-Code600)







