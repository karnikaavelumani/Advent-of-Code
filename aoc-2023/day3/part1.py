def solution(broken_down):
    symbols = ["@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "/"]
    # Check to see what number is adjacent to the symbol
    for i in range(len(broken_down)):
        for j in range(len(broken_down[i])):
            
        # for j in range(len(broken_down[i])):
        #     if broken_down[i][j] in symbols:
        #         print(broken_down)


with open("sample.txt") as text:
    lines = text.read().split("\n")
    lst = []
    for line in lines:
        lst.append(line.split(" "))
        broken_down = [[list(cell) for cell in row] for row in lst]
    solution(broken_down)
