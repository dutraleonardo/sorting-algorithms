def sel_sort(data):

    for i in range(len(data)-1, 0, -1):
        max_position = 0
        for location in range(1, i+1):
            if data[location] > data[max_position]:
                max_position = location

        temp = data[i]
        data[i] = data[max_position]
        data[max_position] = temp
