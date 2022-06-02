def min_coast(a, b, matrix: list) -> tuple:
    total_coast = matrix[a[0]][a[1]]
    path = [total_coast]

    def rek_path(start, stop) -> list:
        nonlocal total_coast
        while True:
            if start[0] == stop[0] and start[1] == stop[1]:
                return ["end"]
            if start[1] < (len(matrix[0])) - 1 and start[0] < (len(matrix) - 1) \
                    and start[1] != stop[1] and start[0] != stop[0]:
                next_right = total_coast + matrix[start[0]][start[1] + 1]
                next_down = total_coast + matrix[start[0] + 1][start[1]]
                if next_right < next_down:
                    total_coast = next_right
                    return [matrix[start[0]][start[1] + 1]] + rek_path((start[0], start[1] + 1), stop)
                else:
                    total_coast = next_down
                    return [matrix[start[0] + 1][start[1]]] + rek_path((start[0] + 1, start[1]), stop)
            if start[1] == (len(matrix[0])) - 1 and start[0] < (len(matrix) - 1) or start[1] == stop[1]:
                next_down = total_coast + matrix[start[0] + 1][start[1]]
                total_coast = next_down
                return [matrix[start[0] + 1][start[1]]] + rek_path((start[0] + 1, start[1]), stop)
            if start[1] < (len(matrix[0])) - 1 and start[0] == (len(matrix) - 1) or start[0] == stop[0]:
                next_right = total_coast + matrix[start[0]][start[1] + 1]
                total_coast = next_right
                return [matrix[start[0]][start[1] + 1]] + rek_path((start[0], start[1] + 1), stop)

    return path + rek_path(a, b), total_coast


if __name__ == "__main__":
    coasts = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    c = (0, 1)
    n = (1, 3)
    print(min_coast(c, n, coasts))
