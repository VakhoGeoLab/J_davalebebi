import math

def palindrome(word):

    word_len = len(word)
    #print(word_len)

    dividor = int(word_len/2)


    #print(dividor)

    first_half_word = word[:int(dividor)]
    second_half_word = word[-int(dividor):][::-1]
    #print(first_half_word, second_half_word)

    print(first_half_word == second_half_word)



def main():

    word = "maddam"

    palindrome(word)



main()