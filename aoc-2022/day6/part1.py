def solution(lines):
    lst = []
    for line in lines:
        for elem in line:
            lst.append(ord(elem))
    for x in lst:
        if lst[x] == lst[x+1]:
            print("yes")
    # for x in lst:
    #     if ord(lst[x]) == ord(lst[x+1]):
    #         print("yes")
    #     else:
    #         print("no")

    #     for elem in line:
    #         if elem == elem-1 or elem == elem-2 or elem == elem-3:
    #             count += 1
    # print(count)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)