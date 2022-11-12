def print_formatted(number):
    j = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexadecimal = (str(hex(i)[2:])).upper()
        binary = str(bin(i)[2:])
        #j = j + len(binary)
        print(decimal.rjust(j), octal.rjust(j), hexadecimal.rjust(j), binary.rjust(j))

    # print(decimal)
    # print(octal)
    # print(hexadecimal)
    # print(binary)


n = int(input("enter the number: "))
print_formatted(n)

