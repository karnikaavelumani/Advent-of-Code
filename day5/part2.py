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

    temp = []
    count = 0
    for line in lines:
        sets = line.split(" ")
        move_sets = int(sets[1])
        from_sets = int(sets[3])
        to_sets = int(sets[5])

        for i in range(move_sets):
            index = stack[from_sets-1].pop(-1)
            temp.extend(index)
            
        temp.reverse()
        stack[to_sets-1].extend(temp)
        temp = []

        print(stack)

with open('input.txt') as text:
    lines = text.read().split("\n")
    solution(lines)
