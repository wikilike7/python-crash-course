class User:
    def __index__(self, first_name, last_name, user_info):
        self.first = first_name
        self.last = last_name
        self.info = user_info

    def describ_user(self):
        print('The user info is ' + self.info)

    def greet_user(self):
        print('Hello ' + self.first + ' ' + self.last)


# error, but i don't know why and how to fix it
user_ins = User('shichao', 'wang', 'a man')


