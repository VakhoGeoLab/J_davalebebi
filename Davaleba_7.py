
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

        if item == " ":
            numb.append(item)
        else:
            numb.append(anbani_list.index(item))


    for item in numb:
        if item == " ":
            result.append(item)
        else:
            result.append(item+biji)


    for item in result:
        if item == " ":
            resultword.append(item)
        else:
            if item < len(anbani_list):
                resultword.append(anbani_list[item])
            else:
                ricxvi = item-len(anbani_list)
                resultword.append(anbani_list[ricxvi])
    print(resultword)

    word_string = "".join(resultword)

    print(word_string)





def main():
    cezar("kvati vakho",15)


main()