
anbani = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

anbani_list = []



for char in anbani:
    anbani_list.append(char)


def cezar(text, biji):

    text = text.upper()
    code_char = []
    numb = []
    result = []
    resultword = []


    for item in text:
        code_char.append(item)
        numb.append(anbani_list.index(item))


    for item in numb:
        result.append(item+biji)


    for item in result:
        if item < len(anbani_list):
            resultword.append(anbani_list[item])
        else:
            ricxvi = item-len(anbani_list)
            resultword.append(anbani_list[ricxvi])
    print(resultword)





def main():
    cezar("kvati",15)


main()