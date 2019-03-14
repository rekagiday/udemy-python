class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."

    def likes(self, thing):
        return f"{self.first_name} likes {thing}"

    def is_senior(self):
        return self.age > 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first_name}"

user1=User("Joe", "Smith", 73)
user2=User("Anne", "Perry", 20)
print(user1.full_name())
print(user2.initials())
print(user2.likes("coffee"))
print(user1.is_senior())
print(user2.birthday())