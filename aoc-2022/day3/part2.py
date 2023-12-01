def solution(lines):
    lst = []

    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i], lines[i+1], lines[i+2]
        for elem in l1:
            if elem in l2 and elem in l3:
                if elem.isupper():
                    upper = ord(elem) - 38
                    lst.append(upper)
                    break
                if elem.islower():
                    lower = ord(elem) - 96
                    lst.append(lower)
                    break
        
    total = 0 
    for x in lst:
        total += x
    print(total)
    
with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)