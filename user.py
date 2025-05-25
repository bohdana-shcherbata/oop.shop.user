class User:
    def __init__(self, first_name, last_name, email, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}, Age: {self.age}, Country: {self.country}")

    def greeting_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- No privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, email, age, country):
        super().__init__(first_name, last_name, email, age, country)
        self.privileges = Privileges()

user1 = User("Olga", "Petrenko", "olga@mail.com", 25, "Ukraine")
user2 = User("Ivan", "Shevchenko", "ivan@mail.com", 30, "Ukraine")

user1.describe_user()
user1.greeting_user()
print()

user2.describe_user()
user2.greeting_user()
print()

print("Login attempts:", user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts after increments:", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)
print()

admin = Admin("Svitlana", "Adminova", "admin@mail.com", 35, "Ukraine")
admin.describe_user()
admin.privileges.privileges = [
    "Allowed to add message",
    "Allowed to delete users",
    "Allowed to ban users"
]
admin.privileges.show_privileges()
