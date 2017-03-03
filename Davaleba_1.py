import math


def ConsoleProgram(gverdi1, gverdi2):
    if type(gverdi1) and type(gverdi2) != int:
        print("Gaajvi")
    else:
        gverdi3 = math.sqrt(gverdi1**2+gverdi2**2)
        print (gverdi3)




def main():

    ConsoleProgram(3,4)



main()