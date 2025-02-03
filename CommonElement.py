# Ellery, Miles

def CommonElement(array1, array2):
    array3 = []
    for i in array1:
        for j in array2:
            if i == j:
                array3.append(i)
    return array3


print(CommonElement([1,9,6,4,5],[6,7,8,9]))