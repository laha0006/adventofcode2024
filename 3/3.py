data = open("input.txt", "r")
line = data.read()

#ex instructions produce = 161
# 2*4 + 5*5 + 11*8 + 8*5)

custom_ex = "}}+{where()mul(873,602) mul(954,447)^where()~mul(548,799)"


instruction_start = "mul("
ins_enable = "do()"
ins_disable = "don't()"


enabled = True
curr_number = ""
first_found = False
nums = []
for i in range(4,len(line)):
    curr_char = line[i]
    start = line[i-4:i]
    enb = line[i-4:i]
    dis = line[i-4:i+3]

    if enb == ins_enable:
        enabled = True
    if dis == ins_disable:
        enabled = False
    print("enable: ", enb)
    print("disable: ", dis)
    print("enabled: ", enabled)
    print("-- info --")
    if enabled:
        if not first_found:
            print("not first")
            print("curr_char:", curr_char)
            if start == instruction_start and curr_char.isdigit():
                curr_number += curr_char
            elif len(curr_number) > 0 and curr_char.isdigit():
                curr_number += curr_char
            elif len(curr_number) > 0 and not curr_char.isdigit():
                if curr_char == ",":
                    nums.append(int(curr_number))
                    first_found = True
                    curr_number = ""
                else:
                    curr_number = ""
            print("curr_number:", curr_number)
            print("----- first ------")
        else:
            print("first found!")
            print("curr_char:", curr_char)
            if curr_char.isdigit():
                curr_number += curr_char
            elif len(curr_number) > 0 and not curr_char.isdigit():
                if curr_char == ")":
                    nums.append(int(curr_number))
                    curr_number = ""
                    first_found = False
                else:
                    nums.pop()
                    first_found = False
                    curr_number = ""
            print("curr_number:", curr_number)
            print("----- second ------")
# total = 0
# for i in range(1,len(nums),2):
#     total += nums[i-1] * nums[i]


print("lne nums:" , len(nums))
print("nums:")
print(nums)

print(5*5*True)


# print(total)