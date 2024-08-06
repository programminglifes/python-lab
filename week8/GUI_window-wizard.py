import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return

    def get_students(self):
        return self.students

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database")
        self.database = StudentDatabase()

        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)
        self.frame3 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Add Student")
        self.notebook.add(self.frame2, text="View Students")
        self.notebook.add(self.frame3, text="Remove Student")

        # Create add student form
        tk.Label(self.frame1, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.frame1, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.frame1, text="Grade:").grid(row=2, column=0, padx=5, pady=5)

        self.name_field = tk.Entry(self.frame1)
        self.name_field.grid(row=0, column=1, padx=5, pady=5)
        self.age_field = tk.Entry(self.frame1)
        self.age_field.grid(row=1, column=1, padx=5, pady=5)
        self.grade_field = tk.Entry(self.frame1)
        self.grade_field.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.frame1, text="Add Student", command=self.add_student).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Create view students table
        self.tree = ttk.Treeview(self.frame2)
        self.tree["columns"] = ("Name", "Age", "Grade")

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Name", anchor=tk.W, width=100)
        self.tree.column("Age", anchor=tk.W, width=50)
        self.tree.column("Grade", anchor=tk.W, width=50)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Age", text="Age", anchor=tk.W)
        self.tree.heading("Grade", text="Grade", anchor=tk.W)

        self.tree.pack(pady=10)

        tk.Button(self.frame2, text="Refresh", command=self.refresh_table).pack(pady=10)

        # Create remove student form
        tk.Label(self.frame3, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.remove_name_field = tk.Entry(self.frame3)
        self.remove_name_field.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.frame3, text="Remove Student", command=self.remove_student).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def add_student(self):
        name = self.name_field.get()
        age = self.age_field.get()
        grade = self.grade_field.get()

        if name and age and grade:
            student = Student(name, age, grade)
            self.database.add_student(student)
            self.name_field.delete(0, tk.END)
            self.age_field.delete(0, tk.END)
            self.grade_field.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        students = self.database.get_students()
        for student in students:
            self.tree.insert("", "end", values=(student.name, student.age, student.grade))

    def remove_student(self):
        name = self.remove_name_field.get()
        if name:
            self.database.remove_student(name)
            self.remove_name_field.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in the name field.")

if __name__ == "__main__":
    root = tk.Tk()
    gui
