


def pyramid(number):
    pyr_result = "a" * number
    return pyr_result


def illuminati(number):
    x = 0
    space = 0
    while x <= number:
        space = int((number - x) / 2)
        space_result = " " * space
        print(space_result, pyramid(x))

        x += 2






def main():
    illuminati(14)




main()