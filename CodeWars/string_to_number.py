
"""
Note: This kata is inspired by Convert a Number to a String!. Try that one too.

Description
We need a function that can transform a string into a number. What ways of
 achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is
 a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
"""

# simulating input to test it locally
def main():
    user_input = input("User input: ")
    function_return = string_to_number(user_input)
    print(function_return)


def string_to_number(s):
    int_s = int(s)
    return int_s



if __name__ == "__main__":
    main()