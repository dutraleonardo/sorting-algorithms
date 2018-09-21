def insertionSort(alist):

    for index in range(1, len(alist)):

        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current_value


alist = ["fuck", "the", "police"]
insertionSort(alist)
print(alist)
