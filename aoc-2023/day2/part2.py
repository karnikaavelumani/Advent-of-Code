def solution(lines):
    total = 0
    for line in lines:
        line = line[1].split("; ")
        line = [x.split(", ") for x in line]
        colors = {"red": 0, "green": 0, "blue": 0}
        for pull in line:
            for cur_color in pull:
                cur_color = cur_color.split(" ")
                if int(cur_color[0]) > colors[cur_color[1]]:
                    colors[cur_color[1]] = int(cur_color[0])
        total += colors["red"] * colors["green"] * colors["blue"]
    print(total)


with open("input.txt") as text:
    lines = [x.strip() for x in text.readlines()]
    lines = [x.split(": ") for x in lines]
    solution(lines)
