class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False

    def menu(self):
        user_input = input('''Welcome to chatbook!! How would you like to proceed?"
                            1. Press1 to signup
                            2. Press2 to signin
                            3. Press 3 to write a post
                            4. Press4 to message a friend
                            5. Press any other key to exit''')
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit

    def signup(self):
        email = input("enter your email: ")
        pwd = input("enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully! ")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password=='':
            print("please signup first")
        else:
            uname = input("enter your email/username: ")
            pwd = input("enter your password: ")
            if self.username == uname and self.password == pwd:
                print("you have signed in successfully")
                self.loggedin = True
            else:
                print("please input correct credentials")
            print("\n")
            self.menu()
    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your message here: ")
            print(f"your content has been posted -> {txt}")
        else:
            print("you need to signin first to post something")
            print("\n")
            self.menu()
    def send_msg(self):
        if self.loggedin == True:
            txt = input("enter your message: ")
            frnd = input("whom to send message here?")
            print(f"your message has been sent to {frnd}")
            print("\n")
            self.menu()
        else:
            print("you need to signin first to post something")
            print("\n")
            self.menu()
obj = chatbook()
obj.menu()
exit()