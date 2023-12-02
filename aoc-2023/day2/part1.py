def solution(lines):
    colors = {"red": 12, "green": 13, "blue": 14}
    for line in lines:
        game_id = line.replace("Game ", "")
        print(line)
    

with open('sample.txt') as text:
    lines = [x.strip() for x in text.readlines()]
    solution(lines)