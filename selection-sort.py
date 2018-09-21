def selection_sort(alist):

    for i in range(len(alist)-1, 0, -1):

        max_position = 0

        for location in range(1, i+1):
            if alist[location] > alist[max_position]:
                max_position = location

        temp = alist[i]
        alist[i] = alist[max_position]
        alist[max_position] = temp


alist = ["fuck", "the", 4, "police"]
selection_sort(alist)
print(alist)
