
anbani = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def cezar(text, biji):

    text = text.upper()

    result_numbers = []
    result_code = []

    for item in text:
        if item == " ":
            result_code.append(item)
        else:
            number = (anbani.index(item) + biji)
            result_numbers.append(number)
            if number < len(anbani):
                result_code.append(anbani[number])
            else:
                number = number - len(anbani)
                result_code.append(anbani[number])

    print(result_code)


    word_string = "".join(result_code)

    print(word_string)




def main():
    cezar("kvati vakho",2)


main()