def hourglass(arr, i, j):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    arr_height = len(arr)
    arr_width = len(arr[0])
    hourglass_max = max([hourglass(arr, x, y) for x in range(arr_width - 2) for y in range(arr_height -2)])
    print(hourglass_max)