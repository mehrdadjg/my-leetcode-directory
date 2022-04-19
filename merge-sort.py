def sort(items):
    n = len(items)
    if n < 2:
        return items
    
    left = sort(items[:n//2])
    right = sort(items[n//2:])

    i = 0
    j = 0

    output = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    while i < len(left):
        output.append(left[i])
        i += 1
    
    while j < len(right):
        output.append(right[j])
        j += 1
    
    return output

print(sort([0,2,3,1,-1]))