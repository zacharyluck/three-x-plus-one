lowestFail = 1

def threeXPlusOne(num):
    startNum = num
    numlist = []
    looped = False
    global lowestFail

    # iterate on number
    while num > 1:
        # check condition: have I failed?
        if num <= lowestFail:
            break

        # do work: iterate on the number
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = num * 3
            num = num + 1

        # post work condition: have we looped?
        if (num in numlist):
            looped = True
            break

        # do work: append to display list
        numlist.append(num)

    # loop ends, print the results
    lowestFail = startNum
    if looped:
        return (True, startNum, numlist)
    return (False, startNum, numlist)

if __name__ == '__main__':
    for x in range(1, 10000000, 2):
        data = threeXPlusOne(x)

        if data[0]:
            # if the infinite loop is found, stop there
            print(f'Possible infinite loop found at {data[1]}')
            print(f'{data[1]}: {data[2]}')
            break
        else:
            print(f'{data[1]}: {data[2]}')