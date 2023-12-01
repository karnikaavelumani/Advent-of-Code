import re

def solution(lines):
    words = {'one': 1, 
             'two': 2,
             'three': 3, 
             'four': 4, 
             'five': 5, 
             'six': 6, 
             'seven': 7, 
             'eight': 8, 
             'nine': 9 }
    add = 0
    for line in lines:
        result = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))', line)
        if len(result) > 1:
            left = result[0]
            right = result[-1]
            if left in words:
                left = str(words[left])
            if right in words:
                right = str(words[right])
            t = left + right
        elif len(result) == 1:
            center = result[0]
            if center in words:
                center = str(words[center])
            t = center + center
        else:
            print("Error")
        t_int = int(t)
        add += t_int
    print(add)
        

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)
