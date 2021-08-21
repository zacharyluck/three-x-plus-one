from sys import maxsize

def threeXPlusOne(num):
    startNum = num
    loopcatch = 0
    numlist = []

    # iterate on number
    while num > 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = num * 3
            num = num + 1
        
        # check for infinite loops
        loopcatch += 1
        if loopcatch == maxsize:
            break

        # numlist for display purposes
        numlist.append(num)

    print(f'{startNum}: {numlist}')

if __name__ == '__main__':
    for x in range(1, 1000):
        threeXPlusOne(x)