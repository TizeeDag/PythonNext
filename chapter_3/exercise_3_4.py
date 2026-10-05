"""Validate usernames and passwords with detailed custom exceptions."""
import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, character, index):
        self.character, self.index = character, index
        super().__init__(character, index)

    def __str__(self):
        return f"The username contains an illegal character {self.character!r} at index {self.index}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    for index, character in enumerate(username):
        if character not in string.ascii_letters + string.digits + "_":
            raise UsernameContainsIllegalCharacter(character, index)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    for characters, exception in (
        (string.ascii_uppercase, PasswordMissingUppercase),
        (string.ascii_lowercase, PasswordMissingLowercase),
        (string.digits, PasswordMissingDigit),
        (string.punctuation, PasswordMissingSpecial),
    ):
        if not any(character in characters for character in password):
            raise exception()
    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordTooShort, PasswordTooLong, PasswordMissingCharacter) as error:
            print(error)
        else:
            break


if __name__ == "__main__":
    main()
