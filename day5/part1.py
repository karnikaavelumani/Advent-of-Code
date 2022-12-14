def solution(lines):
    stack = [
        ['Z', 'P', 'M', 'H', 'R'],
        ['P', 'C', 'J', 'B'],
        ['S', 'N', 'H', 'G', 'L', 'C', 'D'], 
        ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'], 
        ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
        ['T', 'F', 'S', 'Z', 'B', 'G'], 
        ['N', 'R', 'V'],
        ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'], 
        ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
    ]

    for line in lines:
        sets = line.split(" ")
        move_sets = int(sets[1])
        from_sets = int(sets[3])
        to_sets = int(sets[5])

        for i in range(move_sets):
            index = stack[from_sets-1].pop(-1)
            stack[to_sets-1].append(index)

        print(stack)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)
