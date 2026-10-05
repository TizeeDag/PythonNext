"""Use two greeting-card modules from a separate program."""
from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    birthday_card = BirthdayCard()
    greeting_card = GreetingCard()
    birthday_card.greeting_msg()
    greeting_card.greeting_msg()


if __name__ == '__main__':
    main()
