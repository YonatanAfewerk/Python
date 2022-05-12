import random


def main():
    # get level to determine the complexity of the question
    lev = get_level("Level: ")


def get_level(prompt):
    while True:
        try:
            lev = int(input(prompt))
            if lev > 3 or lev <= 0:
                raise ValueError
            else:
                return lev
        except ValueError:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
