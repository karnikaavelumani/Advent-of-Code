# read text file
with open('input.txt') as text:
    lines = [x.strip() for x in text.readlines()] # strip file (removes '\n')

    # initialize variables
    max = 0 # largest summed group
    sum = 0 # sum of each individual group

    # loop through each element
    for val in lines:
        # add all values in a group
        if val != '':
            sum += int(val)
        # set largest value as max
        else:
            if sum > max:
                max = sum
            sum = 0
            
    print(max) # print max