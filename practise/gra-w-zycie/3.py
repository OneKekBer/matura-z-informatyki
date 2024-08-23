def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
        siatka = []
        for line in content:
            arr = []
            for i in range(len(line)):
                arr.append(line[i])
            siatka.append(arr)
        return siatka

def count_alive(data):
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                counter += 1
    return counter

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def count_neighbors(arr):
    counter = 0
    for item in arr:
        if item == "X":
            counter += 1
    return counter

def get_neighbors(arr, coords):
    y = coords[0]
    x = coords[1]
    answer_coords = []
    neighbors_vectors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for vector in neighbors_vectors:
        new_y = y + vector[1]
        new_x = x + vector[0]

        if new_y >= len(arr):
            new_y = 0
        if new_x >= len(arr[0]):
            new_x = 0

        if new_y < 0:
            new_y = len(arr) - 1
        if new_x < 0:
            new_x = len(arr[0]) - 1

        answer_coords.append(arr[new_y][new_x])
    return answer_coords

def one_generation(data):
    cols = len(data)
    rows = len(data[0])
    alive_coords = []
    dead_coords = []
    
    for i in range(cols):
        for j in range(rows):
            item = data[i][j]
            neighbors_arr = get_neighbors(data, (i, j))
            neighbors_count = count_neighbors(neighbors_arr)

            if item == "." and neighbors_count == 0:
                continue
            if item == "X" and neighbors_count in [2, 3]:
                continue

            if item == "." and neighbors_count == 3:
                alive_coords.append((i, j))
                continue

            if item == "X" and (neighbors_count > 3 or neighbors_count < 2):
                dead_coords.append((i, j))
                continue

    for coords in alive_coords:
        data[coords[0]][coords[1]] = "X" 
    for coords in dead_coords:
        data[coords[0]][coords[1]] = "."

    alive_count = count_alive(data) 
    return [data, alive_count]

def main():
    data = get_data()
   
    i = 0
    while i != 50:
      
        info = one_generation(data)
        data = info[0]
        alive_count = info[1]

        print(f"Generation {i}: Alive cells = {alive_count}")
        print_matrix(data)
        print()

        if alive_count == 120:
            print(f"Target reached at generation {i}")
            break

        i += 1

main()
