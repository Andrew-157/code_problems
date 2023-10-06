
def solution(s: str, num_rows: int):
    rows = [[] for _ in range(num_rows)]
    row = 0
    for i in s:
        rows[row].append(i)
        if row == num_rows - 1:
            row = 0
        else:
            row += 1
        print(row)

    return rows


def solution(s: str, numRows: int):
    rows = [[] for _ in range(numRows)]
    between = numRows - 2
    counter = 0

    if numRows == 1:
        return s

    for i in s:
        if counter == numRows:
            if between:
                rows[between].append(i)
                between -= 1
                continue
            else:
                rows[0].append(i)
                counter = 1
                between = numRows - 2
        else:
            rows[counter].append(i)
            counter += 1

    return ''.join(''.join(sublist) for sublist in rows)


print(solution(s="PAYPALISHIRING", num_rows=3))
print(solution(s="PAYPALISHIRING", num_rows=4))
