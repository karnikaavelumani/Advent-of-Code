with open('input.txt') as text:
    lines = [x.strip() for x in text.readlines()] # strip file (removes '\n')

    total = 0
    # loop through each element
    for val in lines:
        if val == 'A X': # rock vs scissors (lose)
            total += 3
        if val == 'A Y': # rock vs rock (draw)
            total += 4
        if val == 'A Z': # rock vs paper (win)
            total += 8

        if val == 'B X': # paper vs scissors (win)
            total += 1
        if val == 'B Y': # paper vs rock (lose)
            total += 5
        if val == 'B Z': # paper vs paper (draw)
            total += 9

        if val == 'C X': # scissors vs scissors (draw)
            total += 2
        if val == 'C Y': # scissors vs rock (win)
            total += 6
        if val == 'C Z': # scissors vs paper (lose)
            total += 7

    print(total)