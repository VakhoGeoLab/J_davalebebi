import sys

def get_number():
    print('hi')

def main():

    def hello():
        var = 1
        var_list = []

        while True:
            var = input("Es programa poulobs udides da umceres ricxvebs. \nSheikvane ricxvi: ")
            var = int(var)

            if var == 0:
                print("fuck off")
                break
            else:

                var_list.append(int(var))
                print(var_list)

                max_list = max(var_list)
                min_list = min(var_list)

                print("Minimaluri: ", min_list)
                print("Maximaluri: ", max_list)

    hello()

main()