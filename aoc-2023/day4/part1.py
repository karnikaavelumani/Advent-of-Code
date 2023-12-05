def solution(lines):
    total = 0
    for line in lines:
        line = [x.split(" ") for x in line]

        for inner_list in line:
            for element in inner_list:
                # Remove the word 'Card' from the list
                if element == "Card":
                    inner_list.remove(element)
                # Remove any empty strings from the list
                if element == "":
                    inner_list.remove(element)
            print(inner_list)


with open("sample.txt") as text:
    lines = [x.strip() for x in text.readlines()]
    lines = [x.split(" | ") for x in lines]
    solution(lines)
