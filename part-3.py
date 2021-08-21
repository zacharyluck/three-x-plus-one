lowestFail = 1
failList = set()

def threeXPlusOne(num):
    startNum = num
    numlist = []
    looped = False
    global lowestFail
    global failList

    # loop starts
    while num > 1:
        # check condition: have I failed?
        if num <= lowestFail or num in failList:
            numset = set(numlist)
            if num <= lowestFail:
                numset.remove(num)
            newset = set()
            for fnum in numset:
                if fnum % 2 == 1:
                    newset.add(fnum)
            failList.update(newset)
            break

        # do work: iterate on the number
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num *= 3
            num += 1

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
    try:
        for x in range(1, 99999999, 2):
            # check if the number has failed already
            if x in failList:
                failList.remove(x)
                lowestFail = x
                continue

            # get data
            data = threeXPlusOne(x)

            # print results
            if data[0]:
                print(f'Infinite loop found at {data[1]}')
                print(f'{data[1]}: {data[2]}')
                break
            else:
                print(f'{data[1]}: {data[2]}')
    except KeyboardInterrupt:
        print(failList)
        print(x)