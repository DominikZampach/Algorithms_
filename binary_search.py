def binary_search(array, target):
    array.sort()
    low = 0
    high = len(array)
    target_ascii = ord(target) - 96
    while low <= high:
        middle = ((high-low)//2)+low
        if array[middle] == target:
            return middle
        elif target_ascii > ord(array[middle]) - 96:
            low = middle + 1
        elif target_ascii < ord(array[middle]) - 96:
            high = middle - 1
    # Using ord() here isn't perfect, but for demonstration works :D
    return -1

print(binary_search(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z'], 'l'))