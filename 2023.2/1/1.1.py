arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0], [0], [0], [0], [0], [0], [0], [0]]

def change_arr(arr):
    arr[3][2] = 3
    

change_arr(arr)

def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()  # To move to the next line after each row

print_arr(arr)
