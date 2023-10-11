"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""

def digital_root(n):
    str_n = str(n)
    um_of_n = 0
    
    while len(str_n) > 1:
        sum_of_n = 0

        for digits in str_n:
            sum_of_n = int(digits) + sum_of_n
        
        str_n = str(sum_of_n)

    return n if sum_of_n == 0 else sum_of_n