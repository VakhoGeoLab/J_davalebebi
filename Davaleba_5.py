
def acronym(string):
    word_list = string.split()
    #print(word_list)


    char_list = []

    for item in word_list:
        char_list.append(item[0])

    acro = "".join(char_list)
    print(acro)



def main():
    #print("hello world")

    sentence = "trakshi pari"

    acronym(sentence)


main()