import tkinter as tk
from entities import school
from homewindow import HomeWindow


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School ERP")

        # Calculate center position
        width, height = 300, 200

        self.geometry(f"{width}x{height}")
        self.create_widgets()

    def create_widgets(self):
        # 1. Configure the grid to expand and center content
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1) # Row after the buttons

        # Username section
        self.username_label = tk.Label(self, text="Username", font=("Arial", 12))
        # Use 'sticky="e"' to align label to the right (east)
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.username_entry = tk.Entry(self, width=20, font=("Arial", 12))
        # Use 'sticky="w"' to align entry to the left (west)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Password section
        self.password_label = tk.Label(self, text="Password", font=("Arial", 12))
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.password_entry = tk.Entry(self, width=20, font=("Arial", 12), show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Buttons - Putting them in their own frame or centering them
        self.login_button = tk.Button(self, text="Login", command=self.login_user)
        self.login_button.grid(row=3, column=0, pady=20, sticky="e")

        self.cancel_button = tk.Button(self, text="Cancel", bg="red", fg="white", command=self.destroy)
        self.cancel_button.grid(row=3, column=1, pady=20, sticky="w")

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
            HomeWindow()
            self.destroy()
        else:
            print("Incorrect username or password")