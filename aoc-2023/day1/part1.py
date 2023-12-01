def solution(lines):
    arr = []
    t = 0
    for line in lines:
        arr = list(line)
        for x in arr[:]:
            if x.isalpha():
                arr.remove(x)
        if len(arr) >= 1:
            c = int(arr[0] + arr[-1])
            t += c
    print(t)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)
