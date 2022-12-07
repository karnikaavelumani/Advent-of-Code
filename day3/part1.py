def solution(lines):
    lst = []
    for line in lines:
        middle = len(line)//2
        left, right = line[:middle], line[middle:]
        for i in left:
            for j in right:
                if i == j:
                    if j.isupper():
                        upper = ord(j) - 38
                        lst.append(upper)
                    if j.islower():
                        lower = ord(j) - 96
                        lst.append(lower)
    total = 0
    for x in lst:
        total += x
    print(total)
    
with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)
