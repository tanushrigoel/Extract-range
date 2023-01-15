def solution(lst):
    ranges = []
    start = lst[0]
    end = lst[0]
    for i in range(1, len(lst)):
        if end==lst[i]-1:
            end = lst[i]
        else:
            ranges.append((start, end))
            start = lst[i]
            end = lst[i]
    ranges.append((start, end))
    # print(ranges)
    formatted_ranges = []
    for r in ranges:
        if r[0] == r[1]:
            formatted_ranges.append(str(r[0]))
        elif r[0] + 1 == r[1]:
            formatted_ranges.append(str(r[0]) + "," + str(r[1]))
        else:
            formatted_ranges.append(str(r[0]) + "-" + str(r[1]))
    return (",".join(formatted_ranges))

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))