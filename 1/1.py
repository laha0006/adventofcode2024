from collections import Counter

data = open("part_one_data.txt", "r")
lines = data.read().splitlines()



total_distance = 0
left = []
right = []
for line in lines:
    x,y = line.split("   ")
    left.append(x)
    right.append(y)


# part one
left.sort()
right.sort()
#
# for i in range(len(left)):
#     distance = abs(int(right[i]) - int(left[i]))
#     total_distance += distance
#
# print(left)
# print(right)

# print(total_distance)

counts = {}
for i in range(len(right)):
    x = right[i]
    counts[x] = counts.get(x, 0) + 1

similarity = {}
similarity_score = 0
for i in range(len(left)):
    x = left[i]
    print(x)
    # similarity[x] = int(similarity.get(x, 0)) + (int(x) * int(counts.get(x,0)))
    similarity_score += (int(x) * int(counts.get(x,0)))

# similarity_score = 0
# for k,v in similarity.items():
#     similarity_score += int(v)

print(counts)
print(similarity)
print(similarity_score)


test = Counter()
test[0] += 1
print(test)
