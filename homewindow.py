import tkinter as tk
from tkinter import ttk
from entities import school


class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("School ERP System (Grid Edition)")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")
        self.minsize(400, 200)
        self.active_view = "Main"
        # Define grid weights so the main display expands but the sidebar stays fixed
        self.columnconfigure(0, weight=0)  # Sidebar column (fixed)
        self.columnconfigure(1, weight=100)  # Main display column (stretches)
        self.rowconfigure(0, weight=1)  # Stretch vertically

        self.create_layout()

    def create_layout(self):
        # 1. Sidebar Frame
        # We use sticky="nsew" to make it fill the entire height
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Sidebar Title
        tk.Label(self.sidebar, text="ERP MENU", font=("Arial", 14, "bold"),
                 bg="#2c3e50", fg="white").grid(row=0, column=0, pady=25, padx=10)

        # Navigation Buttons
        buttons = ["Teacher", "Student", "Standard", "Subject"]
        for i, btn_text in enumerate(buttons):
            # i + 1 because the title is at row 0
            tk.Button(self.sidebar, text=btn_text, font=("Arial", 11),
                      bg="#34495e", fg="white", bd=0, pady=10,
                      activebackground="#1abc9c", cursor="hand2",width=20,
                      command=lambda a=btn_text: self.change_view(a)
                      ).grid(row=i + 1, column=0, sticky="ew", padx=10, pady=5)

        # 2. Main Display Area
        self.main_display = tk.Frame(self, bg="white", bd=0)
        self.main_display.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Content inside Main Display (also using grid)
        self.main_display.columnconfigure(0, weight=1)

        self.header_label = tk.Label(self.main_display, text="Welcome to School ERP",
                                     font=("Arial", 18, "bold"), bg="white", fg="#333")
        self.header_label.grid(row=0, column=0, pady=(40, 10))


        self.main_content = tk.Frame(self.main_display, bg="white", bd=0)
        self.main_content.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.main_content.columnconfigure(0, weight=1)



    def create_table(self,table_data,table_columns):
        # Create a Treeview widget
        table = ttk.Treeview(self.main_content)
        table['show'] = 'headings'
        # Define the columns
        table['columns'] = table_columns
        # Format the columns
        for column in table_columns:
            table.column(column, width=80, anchor= "center")
            table.heading(column, text=column)
        # Configure alternating row colors
        table.tag_configure('oddrow', background='#E8E8E8')
        table.tag_configure('evenrow', background='#FFFFFF')


        # Add data with alternating row colors
        for i in range(len(table_data)):
            if i % 2 == 0:
                table.insert(parent='', index=i, values=table_data[i], tags=('evenrow',))
            else:
                table.insert(parent='', index=i, values=table_data[i], tags=('oddrow',))
        table.bind("<Double-1>", lambda event: self.on_row_double_click(table_columns,table))
        table.grid(row=0,column=0, sticky="nsew")


    def change_view(self, title):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        self.header_label.config(text=f"{title} Management")
        self.active_view = title
        table_data = None
        table_columns = None
        if title == "Teacher":
            table_columns = "Id,Name,Date of Birth, Contact, Designation, Teaches Standard, Subject".split(",")
            table_data = []
            for teacher in school.school["teachers"].values():
                subject_names = []
                for subject in teacher.subjects:
                    subject_names.append(subject.name)
                teaches_standard = []
                for standard in teacher.teaches_standard:
                    teaches_standard.append(standard.grade+"-"+standard.section)
                table_data.append([teacher.teacher_id, teacher.name,teacher.date_of_birth,teacher.contact_number,teacher.designation,",".join(teaches_standard),",".join(subject_names)])
        elif title == "Student":
            table_columns = "first_name, last_name, date_of_birth, parent_name, parent_contact, student_contact,enrolment_number, admission_date".split(",")
            students = school.school["students"].values()
            table_data = []
            for student in students:
                table_data.append([student.first_name,student.last_name,student.date_of_birth,student.parent_name, student.parent_contact,student.student_contact ,student.enrolment_number, student.admission_date, student.standard])
        elif title == "Standard":
            table_columns = "Grade,Section,Class Teacher,Room No".split(",")
            table_data = []
            standards = school.school["standards"].values()
            for standard in standards:
                table_data.append([standard.grade, standard.section, standard.class_teacher, standard.room_no])
        elif title == "Subject":
            table_columns = "Code,Name,Practical,Grade,Optional".split(",")
            table_data = []
            subjects = school.school["subjects"].values()
            for subject in subjects:
                table_data.append([subject.code, subject.name, subject.has_practical, subject.grade_level, subject.is_optional])
        self.create_table(table_data,table_columns)

    def on_row_double_click(self, table_columns, table):
        # Get the selected item ID
        selected_item = table.selection()
        if not selected_item:
            return

        # Get the data values of the row
        item_data = table.item(selected_item, "values")

        # Clear the main content and show details
        self.show_details_view(table_columns, item_data)

    def show_details_view(self,table_columns, data):
        # 1. Clear current content in main_content
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # 2. Update Header
        self.header_label.config(text=f"Detailed {self.active_view} View")

        # 3. Create a Detail Container
        details_frame = tk.Frame(self.main_content, bg="white")
        details_frame.grid(row=0, column=0, sticky="nsew")

        # 4. Loop through data and show as labels
        for index, value in enumerate(data):
            tk.Label(details_frame, text=f"{table_columns[index]}:", font=("Arial", 10, "bold"),
                     bg="white").grid(row=index, column=0, sticky="w", pady=5)
            tk.Label(details_frame, text=value, font=("Arial", 10),
                     bg="white").grid(row=index, column=1, sticky="w", padx=10)
        # Here we will make standard table
        if  self.active_view == 'Standard':
            standard_id = data[0]+data[1]
            standard = school.get_standard_by_id(standard_id)
            self.create_student_table(standard.students, index)
        # 5. Add a "Back" button
        tk.Button(details_frame, text="<< Back to List", command=self.refresh_current_view,
                  bg="#34495e", fg="white", padx=10).grid(row=len(data), column=0, pady=20)

    def refresh_current_view(self):
        # Extracts the current category from the header label to "go back"
        self.change_view(self.active_view)

    def create_student_table(self,students, row_index):
        print("Creating table")
        table_columns = "first_name, last_name, date_of_birth, parent_name, parent_contact, student_contact,enrolment_number, admission_date".split(
            ",")
        table_data = []
        print(students)
        for student in students:
            table_data.append([student.first_name, student.last_name, student.date_of_birth, student.parent_name,
                               student.student_contact, student.enrolment_number, student.admission_date,
                               student.standard])
        table = ttk.Treeview(self.main_content)
        table['show'] = 'headings'
        # Define the columns
        table['columns'] = table_columns
        # Format the columns
        for column in table_columns:
            table.column(column, width=80, anchor="center")
            table.heading(column, text=column)
        # Configure alternating row colors
        table.tag_configure('oddrow', background='#E8E8E8')
        table.tag_configure('evenrow', background='#FFFFFF')

        # Add data with alternating row colors
        for i in range(len(table_data)):
            if i % 2 == 0:
                table.insert(parent='', index=i, values=table_data[i], tags=('evenrow',))
            else:
                table.insert(parent='', index=i, values=table_data[i], tags=('oddrow',))
        table.grid(row=row_index+1, column=0, sticky="nsew")
        pass