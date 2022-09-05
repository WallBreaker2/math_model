
def select_sort(data:list):
    n = len(data)
    for i in range(0,n):
        minIdx = i
        for j in range(i+1,n):
            if data[j] < data[minIdx]:
                minIdx = j
        temp = data[i]
        data[i] = data[minIdx]
        data[minIdx] = temp
    return data


print(select_sort([2,3,1,0,4,5]))