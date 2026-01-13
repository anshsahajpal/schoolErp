from os.path import exists

class User:
    def __init__(self,username,password,email,ph_no,user_type):
        self.username = username
        self.password = password
        self.email = email
        self.ph_no = ph_no
        self.user_type = user_type

    @staticmethod
    def save_users(user_list):
        with open("./data/users.csv", "w") as f:
            f.write("username,password,email,ph_no,user_type\n")
            for user in user_list:
                user_data = f"{user.username_text},{user.password_text},{user.email},{user.ph_no},{user.user_type}\n"
                f.write(user_data)

    @staticmethod
    def load_users(school):
        if exists("./data/users.csv"):
            with open("./data/users.csv", "r") as f:
                f.readline()
                for line in f.readlines():
                    user_data = line.split(",")
                    school['users'][user_data[0]] = User(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4])
