def convertToTernary(N):
    if N == 0:
        return
    x = N % 3
    N //= 3
    if x < 0:
        N += 1
    convertToTernary(N)
    if x < 0:
        print(x + (3 - 1), end="")
    else:
        print(x, end="")


def convert(dec):
    print("Ternary number of ", dec, " is: ", end="")
    if dec != 0:
        convertToTernary(dec)
    else:
        print("o", end="")


if __name__ == '__main__':
    Decimal = 3
    convert(Decimal)
