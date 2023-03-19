# # python3

def build_heap(data):
    swaps = []
    # Create heap using sift-down operation
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    # Helper function to sift-down a node to maintain the heap property
    min_index = i
    left_child = 2 * i + 1
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def main():
    # Input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # Checks if length of data is the same as the said length
    assert len(data) == n

    # Calls function to assess the data and give back all swaps
    swaps = build_heap(data)

    # Output how many swaps were made
    print(len(swaps))

    # Output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

# def build_heap(data):
#     swaps = []
#     # TODO: Creat heap and heap sort
#     # try to achieve  O(n) and not O(n2)


#     return swaps


# def main():
    
#     # TODO : add input and corresponding checks
#     # add another input for I or F 
#     # first two tests are from keyboard, third test is from a file


#     # input from keyboard
#     n = int(input())
#     data = list(map(int, input().split()))

#     # checks if lenght of data is the same as the said lenght
#     assert len(data) == n

#     # calls function to assess the data 
#     # and give back all swaps
#     swaps = build_heap(data)

#     # TODO: output how many swaps were made, 
#     # this number should be less than 4n (less than 4*len(data))


#     # output all swaps
#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)


# if __name__ == "__main__":
#     main()
