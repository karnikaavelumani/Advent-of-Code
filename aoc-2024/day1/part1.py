nums1 = []
nums2 = []
diff = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split()
        nums1.append(line[0])
        nums2.append(line[1])

    for a, b in zip(sorted(nums1), sorted(nums2)):
        diff.append(abs(int(a) - int(b)))
    
    print(sum(diff))