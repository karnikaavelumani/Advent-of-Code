# read text file
with open('day1.txt') as text:
    lines = [x.strip() for x in text.readlines()] # strip file (removes '\n')

    # set max and sum to 0
    max = 0
    sum = 0

    # loop through each element
    for val in lines:
        # add all values in a group
        if val != '':
            sum = int(val) + sum
        # set largest value as max
        else:
            if sum > max:
                max = sum
            sum = 0
            
    print(max) # print max