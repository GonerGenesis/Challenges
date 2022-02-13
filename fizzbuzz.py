# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+8 to toggle the breakpoint.


def fizzbuzz(iv_number):
    if iv_number % 3 == 0:
        if iv_number % 5 == 0:
            return "fizzbuzz"
        else:
            return "fizz"
    elif iv_number % 5 == 0:
        return "buzz"
    else:
        return iv_number


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(fizzbuzz(15))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
