"""Raise a custom exception when an invitee is under eighteen."""


class UnderAge(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(age)

    def __str__(self):
        return f"Age {self.age} is under 18; wait {18 - self.age} years."


def send_invitation(name, age):
    age = int(age)
    if age < 18:
        raise UnderAge(age)
    print("You should send an invite to " + name)


if __name__ == "__main__":
    for age in (17, 20):
        try:
            send_invitation("Alice", age)
        except UnderAge as error:
            print(error)
