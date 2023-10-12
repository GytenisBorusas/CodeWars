"""

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal 
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

"""

# simulating input to test it locally
def main():
    user_input = input("User input: ")
    ui1, ui2, ui3 = user_input.split(",")
    function_return = rgb(ui1, ui2, ui3)
    print(function_return)



def rgb(r, g, b):
    
    r = int(r)
    g = int(g)
    b = int(b)

    #checks if "r" is within the range of 0 to 255
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    else:
        r = r

    #checks if "g" is within the range of 0 to 255
    if g > 255:
        g = 255
    if g < 0:
        g = 0
    else:
        g = g

    #checks if "b" is within the range of 0 to 255
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    else:
        b = b

    hex_r = "{:02X}".format(r)
    hex_g = "{:02X}".format(g)
    hex_b = "{:02X}".format(b)

    print(hex_r)
    print(hex_g)
    print(hex_b)

    hexadecimal = hex_r + hex_g + hex_b
    hexadecimal = hexadecimal.upper()
    print(hexadecimal)

    return hexadecimal





if __name__ == "__main__":
    main()