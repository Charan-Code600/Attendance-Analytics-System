




import pandas as pd
from datetime import datetime

FILE = "attendance.csv"
RAW_COLUMNS = ["StudentID", "Name", "Date", "Status"]

print("""

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
""")

def main():
    df = load_data()

    while True:
        print()
        print("*"*60)
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                df = add_record(df)
            elif choice == "2":
                view_all_records(df)
            elif choice == "3":
                student_wise_attendance(df)
            elif choice == "4":
                low_attendance_list(df)
            elif choice == "5":
                date_wise_trend(df)
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")
        except Exception as e:
            print(f"\nSomething went wrong: {e}")
            print("Please try again.")


def load_data():
        try:
            return pd.read_csv(FILE, dtype={"StudentID": str})
        except (FileNotFoundError, pd.errors.EmptyDataError):
            print(f"\n'{FILE}' not found or empty. Creating a new file...")
            data = pd.DataFrame(columns=RAW_COLUMNS).astype({"StudentID": str})
            data.to_csv(FILE, index=False)
            return data


def save_data(df):
    df[RAW_COLUMNS].to_csv(FILE, index=False)


def get_valid_date():
    while True:
        date_str = input("Enter Date (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print()
            print("⚠️ Warning")
            print("Invalid date format! Please use DD-MM-YYYY (e.g. 15-08-2026).")
            print("-"*50)


def get_valid_status():
    while True:
        status = input("Status (Present/Absent): ").strip().capitalize()
        if status in ["Present", "Absent"]:
            return status
        print()
        print("⚠️ Warning")
        print("Invalid status! Enter Present or Absent.")
        print()

def add_record(df):
    student_id = input("Student ID: ").strip().upper()
    if student_id == "":
        print("Student ID cannot be empty!")
        return df

    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return df

    date = get_valid_date()

    existing = df[(df["StudentID"] == student_id) & (df["Date"] == date)]
    if not existing.empty:
        confirm = input(
            f"Attendance for '{student_id}' on {date} already exists. Add anyway? (y/n): "
        ).strip().lower()
        if confirm != "y":
            print("Add cancelled.")
            return df

    status = get_valid_status()

    new_record = pd.DataFrame([{
        "StudentID": student_id,
        "Name": name,
        "Date": date,
        "Status": status
    }])

    df = pd.concat([df, new_record], ignore_index=True)
    save_data(df)
    print(f"\nRecord added for {name}!")
    return df


def view_all_records(df):
    if df.empty:
        print("\nNo records found yet. Add one first (Option 1).")
        return
    print(f"\nAvailable columns: {list(df.columns)}\n")
    print(df.to_string(index=False))


def student_wise_attendance(df):
    if df.empty:
        print("\nNo records found yet.")
        return

    search_id = input("Enter Student ID: ").strip().upper()
    student_df = df[df["StudentID"] == search_id]

    if student_df.empty:
        print("Student not found!")
        return

    total = len(student_df)
    present = len(student_df[student_df["Status"] == "Present"])
    percentage = (present / total) * 100
    name = student_df["Name"].iloc[0]

    print(f"\nStudent: {name}")
    print(f"Total Days: {total}")
    print(f"Present: {present}")
    print(f"Absent: {total - present}")
    print(f"Attendance: {percentage:.2f}%")


def low_attendance_list(df):
    if df.empty:
        print("\nNo records found yet.")
        return

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
        print("No students below 75% attendance!")


def date_wise_trend(df):
    if df.empty:
        print("\nNo records found yet.")
        return

    print("\n--- Date-wise Trend ---")
    for date in df["Date"].unique():
        date_df = df[df["Date"] == date]
        present = len(date_df[date_df["Status"] == "Present"])
        absent = len(date_df[date_df["Status"] == "Absent"])
        print(f"{date} -> Present: {present}, Absent: {absent}")


if __name__ == "__main__":
    main()









