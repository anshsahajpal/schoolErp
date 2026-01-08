import tkinter as tk

def login_user():
    print("Logging user in now")
    print("checking password")
    print(username.get())
    print(password.get())
    print("Successfully logged in")

root = tk.Tk()
root.title("School ERP")
root.geometry("300x200")

# Create labels
label1 = tk.Label(root, text="Username", font=("Arial", 12))
username = tk.Entry(root, width=20, font=("Arial", 12))
label2 = tk.Label(root, text="Password", font=("Arial", 12))
password = tk.Entry(root, width=20, font=("Arial", 12))
login = tk.Button(root, text="Login", command=login_user)
cancel = tk.Button(root, text="Cancel", bg="red", fg="white", command=root.destroy)

# Arrange them in a grid
label1.grid(row=0, column=0)
username.grid(row=0, column=1)
label2.grid(row=1, column=0)
password.grid(row=1, column=1)
login.grid(row=2, column=0)
cancel.grid(row=2, column=1)

root.mainloop()