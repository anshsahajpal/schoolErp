import tkinter as tk
from tkinter import ttk
from entities import school

school.load_school_data()

class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("School ERP System (Grid Edition)")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")
        self.minsize(400, 200)

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

        self.status_label = tk.Label(self.main_display, text="Select an option from the left to begin.",
                                     font=("Arial", 12), bg="white", fg="#666")
        self.status_label.grid(row=1, column=0)


    def create_table(self,table_data,table_columns):
        # Create a Treeview widget
        table = ttk.Treeview(self.main_display)

        # Define the columns
        table['columns'] = table_columns

        # Format the columns
        for column in table_columns:
            table.column(column, width=150)
            table.heading(column, text=column)
        # Sample data
        data = [
            "T1,Ansh,11/11/11,11,Junior,1A,C1".split(","),
            "T1,Ansh,11/11/11,11,Junior,1A,C1".split(",")
        ]

        # Configure alternating row colors
        table.tag_configure('oddrow', background='#E8E8E8')
        table.tag_configure('evenrow', background='#FFFFFF')


        # Add data with alternating row colors
        for i in range(len(data)):
            if i % 2 == 0:
                table.insert(parent='', index=i, values=data[i], tags=('evenrow',))
            else:
                table.insert(parent='', index=i, values=data[i], tags=('oddrow',))
        table.grid(row=2,column=0, sticky="nsew")

    def change_view(self, title):
        self.header_label.config(text=f"{title} Management")
        self.status_label.config(text=f"Loading {title} dashboard...")
        table_data = None
        table_columns = None
        if title == "Teacher":
            table_columns = "Id,Name,Date of Birth, Contact, Designation, Teaches Standard, Subject".split(",")
            table_data = school.school["teachers"]
        elif title == "Student":
            table_data = school.school["students"]
        elif title == "Standard":
            table_data = school.school["standards"]
        elif title == "Subject":
            table_data = school.school["subjects"]
        self.create_table(table_data,table_columns)


if __name__ == "__main__":
    app = HomeWindow()
    app.mainloop()
