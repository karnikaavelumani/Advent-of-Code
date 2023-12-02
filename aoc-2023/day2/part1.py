def solution(lines):
    colors = {"red": 12, "green": 13, "blue": 14}
    for line in lines:
        game_id = line[0].replace("Game ", "")
        line = line[1].split("; ")
        line = [x.split(", ") for x in line]
        # print(line)

        for l in line:
            line = l.split(" ")

        print(line)
        # print(l)

        # new_dict = {"id": game_id, "cubes": []}
        # cube = {"red": [], "green": [], "blue": []}

        # Create a frequency map for the given list
        # freq_map = {}
        # for l in line:
        #     freq_map[l[0]] = freq_map.get(l[0], 0) + 1
        # print(freq_map)


with open("sample.txt") as text:
    # Remove new line characters
    lines = [x.strip() for x in text.readlines()]
    # Split lines by colon
    lines = [x.split(": ") for x in lines]
    solution(lines)
