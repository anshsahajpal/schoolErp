from entities import school
from login_window import LoginWindow

school.load_school_data()

login_window = LoginWindow()

login_window.mainloop()