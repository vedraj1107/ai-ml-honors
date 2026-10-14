import sqlite3

class Employee:
    def __init__(self):
        self.conn = sqlite3.connect("employee.db")
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists employee(id int, name text, dept text, salary int)")

    def find(self, id):
        self.cur.execute("select * from employee where id=?", (id,))
        return self.cur.fetchone()

    def add(self, id, name, dept, salary):
        if self.find(id):
            print("ID already exists")
        else:
            self.cur.execute("insert into employee values(?,?,?,?)", (id, name, dept, salary))
            self.conn.commit()
            print("Added")

    def view(self):
        self.cur.execute("select * from employee")
        for r in self.cur.fetchall():
            print(r)

    def search(self, id):
        r = self.find(id)
        if r:
            print(r)
        else:
            print("Not found")

    def update(self, id, name, dept, salary):
        if self.find(id):
            self.cur.execute("update employee set name=?, dept=?, salary=? where id=?", (name, dept, salary, id))
            self.conn.commit()
            print("Updated")
        else:
            print("Not found")

    def delete(self, id):
        if self.find(id):
            self.cur.execute("delete from employee where id=?", (id,))
            self.conn.commit()
            print("Deleted")
        else:
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
