def solution(lines):
    lst = []
    for line in lines:
        middle = len(line)//2
        left, right = line[:middle], line[middle:]
        for elem in line:
            if elem in left and elem in right:
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
