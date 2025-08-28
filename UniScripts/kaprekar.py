# by Omwekiatl - 2014
# Kaprekar algorithm calculator

def array2int(array=[]):
    # convert to an int an array with a digit in each position
    total = 0
    for i in range(len(array)):
        total += array[i] * pow(10, len(array) - 1 - i)
    return total

def int2array(value=0, arrayMinLen=1):
    # convert an int in an array with each digit in a position
    text = int2str(value, arrayMinLen)
    array = []
    for char in text:
        array.append(int(char))
    return array

def int2str(value=0, strMinLen=1):
    # convert int in str filling with zeros the empty space
    text = str(value)
    while len(text) < strMinLen:
        text = "0" + text
    return text

def kaprekar(value=0, showPrints=True):
    # constant of Kaprekar
    k = 6174
    # obtain the main data to work, in array form from value
    arrayCurrent = int2array(abs(value), 4)
    # this check if is correct size or a bigger number
    if len(arrayCurrent) != 4:
        if showPrints:
            print("   long number")
        return None
    # this check if all digits are the same or is okey
    ok = False
    for i in range(1, 4):
        if arrayCurrent[i] != arrayCurrent[0]:
            ok = True
            break
    if not ok:
        if showPrints:
            print("   repeated number")
        return None
    # here start all, declaring the starting point
    current = array2int(arrayCurrent)
    if showPrints:
        print("   calculating for: " + int2str(current, 4))
    count = 0
    # this is the algorithm loop until find Kaprekar constant
    while current != k:
        # a counter to count iterations
        count += 1
        # ordered the array to obtain descending number
        arrayCurrent.sort(reverse=True)
        descending = array2int(arrayCurrent)
        # ordered the array to obtain ascending number
        arrayCurrent.sort(reverse=False)
        ascending = array2int(arrayCurrent)
        # do the difference to find the new number and its array form
        current = descending - ascending
        arrayCurrent = int2array(current, 4)
        # prints in one line the operations of the current iteration
        if showPrints:
            print("   (" + str(count) + ") " +
                int2str(current, 4) + " = " +
                int2str(descending, 4) + " - " +
                int2str(ascending, 4))
    # the function returns the total interations
    return count

def hardTest():
    # this do all possible operations over Kaprekar
    # to find max possible iterations and its triggered number
    iterMax = 0
    valueMax = 0
    for i in range(10000):
        iters = kaprekar(i, False)
        if iters != None:
            if iters > iterMax:
                iterMax = iters
                valueMax = i
    print("   first number with max iterations")
    print("   (" + str(iterMax) + ") " + int2str(valueMax, 4))

def main():
    print("******Kaprekar calculator******")
    # main loop of the software to do multiple interactions
    while True:
        print("...")
        print("***Menu***")
        print("1- calculate")
        print("2- instructions")
        print("3- algorithm")
        print("4- hard test")
        print("5- credits")
        print("6- exit")
        # tell and wait for the user to do a command
        sel = input("-> selection: ")
        if sel == "1":
            # wait for a number digited by the user
            value = input("-> digit number: ")
            # this try can detect illegal characters typed
            try:
                value = int(value)
                kaprekar(value)
            except:
                print("   wrong number")
        elif sel == "2":
            # information of how use the software
            print("   you should enter a 4 digits number where")
            print("   the 4 digits are not the same, and it")
            print("   will compute the Kaprekar algorithm")
        elif sel == "3":
            # information about the theme
            print("   given a non repeated 4 digit number")
            print("   the difference between the orders")
            print("   descending and ascending of these goes")
            print("   to iteratively reach the constant 6174")
            print("   this was discovered by:")
            print("   D.R. Dattatreya Ramachandra Kaprekar")
        elif sel == "4":
            hardTest()
        elif sel == "5":
            # information about autor and software
            print("   made by: Omar Jordan Jordan - 2024")
        elif sel == "6":
            # exit the main loop, closing the software
            print("   exit")
            return None
        else:
            # in case that input is not recognized
            print("   wrong selection")
        # this wait for interaction to show the menu again
        input("(press any)")

# launch the software
main()
