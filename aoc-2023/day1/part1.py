def solution(lines):
    for line in lines:
        print(line)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)