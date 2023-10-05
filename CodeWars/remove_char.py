
"""
It's pretty straightforward. Your goal is to create a function that
removes the first and last characters of a string. You're given one
parameter, the original string. You don't have to worry with strings
with less than two characters.
"""

# simulating input to test it locally
def main():
    user_input = input("User input: ")
    function_return = find_smallest_int(user_input)
    print(function_return)


def remove_char(s):
    return s[1:-1]





if __name__ == "__main__":
    main()