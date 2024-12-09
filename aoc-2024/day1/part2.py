from collections import Counter

nums1 = []
nums2 = []
diff = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split()
        nums1.append(line[0])
        nums2.append(line[1])
    
freq = Counter(nums2)
for num in nums1:
    diff.append(int(num) * freq[num])

print(sum(diff))