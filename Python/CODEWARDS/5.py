"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

def rgb(r, g, b):
    r = sorted([0, round(r), 255])[1]
    g = sorted([0, round(g), 255])[1]
    b = sorted([0, round(b), 255])[1]

    x = f"{r:02X}{g:02X}{b:02X}"

    return x