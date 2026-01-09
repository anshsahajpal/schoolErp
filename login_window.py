import tkinter as tk
import school

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("School ERP")
        self.geometry("300x200")

        # UI Initialization
        self.create_widgets()

    def create_widgets(self):
        # Username section
        self.username_label = tk.Label(self, text="Username", font=("Arial", 12))
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(self, width=20, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password section
        self.password_label = tk.Label(self, text="Password", font=("Arial", 12))
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(self, width=20, font=("Arial", 12), show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        self.login_button = tk.Button(self, text="Login", command=self.login_user)
        self.login_button.grid(row=2, column=0, pady=20)

        self.cancel_button = tk.Button(self, text="Cancel", bg="red", fg="white", command=self.destroy)
        self.cancel_button.grid(row=2, column=1, pady=20)

    def login_user(self):
        """Handle the login logic"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            print("Invalid username or password")
        if username not in school.school['users'].keys():
            print("Username not available")
        user = school.school['users'][username]
        if user.password == password:
            print("Logged in successfully")
        else:
            print("Incorrect username or password")