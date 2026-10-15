import pandas as pd
import os

FILE = "employee_pandas.csv"

# first run: create empty csv with columns
if not os.path.exists(FILE):
    pd.DataFrame(columns=["id", "name", "dept", "salary"]).to_csv(FILE, index=False)


def load():
    return pd.read_csv(FILE)


def save(df):
    df.to_csv(FILE, index=False)


def add_employee():
    df = load()
    eid = int(input("Enter ID: "))
    if eid in df["id"].values:
        print("ID already exists!")
        return
    name = input("Enter name: ")
    dept = input("Enter dept: ")
    salary = int(input("Enter salary: "))
    df.loc[len(df)] = [eid, name, dept, salary]
    save(df)
    print("Employee added.")


def view_employees():
    df = load()
    if df.empty:
        print("No employees found.")
    else:
        print(df.to_string(index=False))


def search_employee():
    df = load()
    eid = int(input("Enter ID to search: "))
    result = df[df["id"] == eid]
    if result.empty:
        print("Employee not found.")
    else:
        print(result.to_string(index=False))


def update_employee():
    df = load()
    eid = int(input("Enter ID to update: "))
    if eid not in df["id"].values:
        print("Employee not found.")
        return
    name = input("New name: ")
    dept = input("New dept: ")
    salary = int(input("New salary: "))
    df.loc[df["id"] == eid, ["name", "dept", "salary"]] = [name, dept, salary]
    save(df)
    print("Employee updated.")


def delete_employee():
    df = load()
    eid = int(input("Enter ID to delete: "))
    if eid not in df["id"].values:
        print("Employee not found.")
        return
    df = df[df["id"] != eid]
    save(df)
    print("Employee deleted.")


while True:
    print("\n--- Employee Management ---")
    print("1. Add employee")
    print("2. View all employees")
    print("3. Search employee by ID")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
