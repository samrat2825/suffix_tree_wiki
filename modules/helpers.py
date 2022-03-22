def binarySearch(numbers, searchnum):
    length = len(numbers)
    answer = -1
    start = 0
    end = length - 1
    # print(start, end)
    while start <= end:
        middle = (start + end)//2
        # print(numbers[middle], searchnum)
        if numbers[middle] >= searchnum:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    return answer
