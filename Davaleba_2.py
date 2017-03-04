


def Calculus_Nums(number):

    result = 0

    if number % 2 == 0:
        result = number/2
    else:
        result = number * 3 + 1
    return result






def main():

   result = Calculus_Nums(5)

   while result != 1:
       print(result)
       result = Calculus_Nums(result)
       print(result)

print("test phrase 2")





main()