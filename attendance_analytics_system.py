





import pandas as pd
import os
from datetime import datetime

FILE = "attendance.csv"

if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["StudentID", "Name", "Date", "Status"])

print("""
====================================
    ATTENDANCE ANALYTICS SYSTEM
====================================

Add Attendance Record              enter --- > 1
View All Records                   enter --- > 2
Student-wise Attendance            enter --- > 3
Low Attendance List (< 75%)        enter --- > 4
Date-wise Trend                    enter --- > 5
Exit                               enter --- > 6
""")

while True:

    try:

        print("=================================")

        option = input("Choose: ")

        if option == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            date = input("Date (DD-MM-YYYY): ")
            status = input("Status (Present/Absent): ").capitalize()

            if status not in ["Present", "Absent"]:
                print("❌ Invalid status! Enter Present or Absent.")
                continue

            new_record = pd.DataFrame([{
                "StudentID": student_id,
                "Name": name,
                "Date": date,
                "Status": status
            }])

            df = pd.concat([df, new_record], ignore_index=True)
            df.to_csv(FILE, index=False)
            print(f"✅ Record added for {name}!")

        elif option == "2":
            if df.empty:
                print("❌ No records found!")
            else:
                print(df.to_string(index=False))

        elif option == "3":
            search_id = input("Enter Student ID: ").upper()
            student_df = df[df["StudentID"] == search_id]

            if student_df.empty:
                print("❌ Student not found!")
            else:
                total = len(student_df)
                present = len(student_df[student_df["Status"] == "Present"])
                percentage = (present / total) * 100
                name = student_df["Name"].iloc[0]
                print(f"\nStudent: {name}")
                print(f"Total Days: {total}")
                print(f"Present: {present}")
                print(f"Absent: {total - present}")
                print(f"Attendance: {percentage:.2f}%")

        elif option == "4":
            if df.empty:
                print("❌ No records found!")
            else:
                print("\n--- Low Attendance (< 75%) ---")
                found = False
                for sid in df["StudentID"].unique():
                    student_df = df[df["StudentID"] == sid]
                    total = len(student_df)
                    present = len(student_df[student_df["Status"] == "Present"])
                    percentage = (present / total) * 100
                    name = student_df["Name"].iloc[0]
                    if percentage < 75:
                        found = True
                        print(f"{sid} - {name}: {percentage:.2f}%")
                if not found:
                    print("✅ No students below 75% attendance!")

        elif option == "5":
            if df.empty:
                print("❌ No records found!")
            else:
                print("\n--- Date-wise Trend ---")
                for date in df["Date"].unique():
                    date_df = df[df["Date"] == date]
                    present = len(date_df[date_df["Status"] == "Present"])
                    absent = len(date_df[date_df["Status"] == "Absent"])
                    print(f"{date} → Present: {present}, Absent: {absent}")

        elif option == "6":
            print("👋 Bye!")
            break

        else:
            print("❌ Invalid option!")

    except ValueError:
        print("❌ Invalid input!")







