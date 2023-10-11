
"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""

# simulating input to test it locally
def main():
    user_input = input("User input: ")
    function_return = past(user_input)
    print(function_return)


def past(h, m, s):
    # h = hours, m = minutes, s = seconds
    total_miliseconds = ((h * 60 * 60 * 1000) + (m * 60 * 1000) + (s * 1000))
    return total_miliseconds



if __name__ == "__main__":
    main()