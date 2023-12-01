def solution(lines):
    count = 0
    for line in lines:
        sets = line.split(",")
        sets1 = sets[0].split("-")
        sets2 = sets[1].split("-")

        start1 = int(sets1[0])
        end1 = int(sets1[1])
        start2 = int(sets2[0])
        end2 = int(sets2[1])

        if ((start1 <= start2) and (end1 >= end2)) or ((start1 >= start2) and (end1 <= end2)):
            count += 1
    print(count)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)