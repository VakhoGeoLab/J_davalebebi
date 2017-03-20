

def addComma(number):
    number = int(number)
    number_text = str(number)
    number_list = list(number_text)
    multiple = len(number_list)/3


    if len(number_list)/3 <= 1:
        print(number)
    elif len(number_list)%3 != 0:

        numb = int(len(number_list)/3)

        while numb > 0:
            number_list.insert(-3*numb,',')
            numb -= 1

        number_list = ''.join(number_list)
        print(number_list)
    else:
        numb = int(len(number_list) / 3) - 1

        while numb > 0:
            number_list.insert(-3 * numb, ',')
            numb -= 1

        number_list = ''.join(number_list)
        print(number_list)




def main():
    addComma(10000)




main()
