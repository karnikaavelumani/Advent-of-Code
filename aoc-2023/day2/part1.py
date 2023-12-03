def solution(lines):
    colors = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for line in lines:
        game_id = line[0].replace("Game ", "")
        line = line[1].split("; ")
        line = [x.split(", ") for x in line]
        have_we_failed = False
        for pull in line:
            for cur_color in pull:
                cur_color = cur_color.split(" ")
                if int(cur_color[0]) > colors[cur_color[1]]:
                    have_we_failed = True
        if not have_we_failed:
            total += int(game_id)
    print(total)


with open("input.txt") as text:
    lines = [x.strip() for x in text.readlines()]
    lines = [x.split(": ") for x in lines]
    solution(lines)
