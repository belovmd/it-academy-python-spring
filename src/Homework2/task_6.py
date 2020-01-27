def rgb(r, g, b):
    """Instructions

    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3
    """
    r1, g1, b1 = map(lambda x: max(0, min(x, 255)), [r, g, b])
    r1, g1, b1 = map(lambda x: '%02X' % x, [r1, g1, b1])
    return r1 + g1 + b1


if __name__ == '__main__':
    red = int(input('Enter the value of red color: '))
    green = int(input('Enter the value of green color: '))
    blue = int(input('Enter the value of blue color: '))
    print(rgb(red, green, blue))
