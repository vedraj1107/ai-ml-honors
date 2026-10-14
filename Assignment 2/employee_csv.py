import csv
import os

class Employee:
    def __init__(self):
        self.file = "employee.csv"
        if not os.path.exists(self.file):
            f = open(self.file, "w", newline="")
            csv.writer(f).writerow(["id", "name", "dept", "salary"])
            f.close()

    def read(self):
        f = open(self.file, "r")
        rows = list(csv.reader(f))
        f.close()
        return rows

    def write(self, rows):
        f = open(self.file, "w", newline="")
        csv.writer(f).writerows(rows)
        f.close()

    def add(self, id, name, dept, salary):
        f = open(self.file, "a", newline="")
        csv.writer(f).writerow([id, name, dept, salary])
        f.close()
        print("Added")

    def view(self):
        for r in self.read():
            print(r)

    def search(self, id):
        for r in self.read():
            if r[0] == id:
                print(r)
                return
        print("Not found")

    def update(self, id, name, dept, salary):
        rows = self.read()
        for r in rows:
            if r[0] == id:
                r[1], r[2], r[3] = name, dept, salary
                self.write(rows)
                print("Updated")
                return
        print("Not found")

    def delete(self, id):
        rows = self.read()
        for r in rows:
            if r[0] == id:
                rows.remove(r)
                self.write(rows)
                print("Deleted")
                return
        print("Not found")


e = Employee()
while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choice: ")
    if ch == "1":
        e.add(input("ID: "), input("Name: "), input("Dept: "), input("Salary: "))
    elif ch == "2":
        e.view()
    elif ch == "3":
        e.search(input("ID: "))
    elif ch == "4":
        e.update(input("ID: "), input("Name: "), input("Dept: "), input("Salary: "))
    elif ch == "5":
        e.delete(input("ID: "))
    elif ch == "6":
        break
    else:
        print("Invalid choice")
