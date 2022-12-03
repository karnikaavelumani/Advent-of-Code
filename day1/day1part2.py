# read text file
with open('day1.txt') as text:
    lines = [x.strip() for x in text.readlines()] # strip file (removes '\n')

    # initialize variables
    sum = 0 # sum of each individual groups
    total = 0 # sum of the last three largest groups
    groups = [] # list of summed groups

    # loop through each element
    for val in lines:
        # add all values in a group
        if val != '':
            sum += int(val)
        # update list with summed groups
        else:
            groups.append(sum)
            sum = 0 
    
    # sort and print max of largest three
    groups.sort()
    total = groups[-1] + groups[-2] + groups[-3]
    print(total)
