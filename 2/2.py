data = open("input.txt", "r")
lines = data.read().splitlines()

lines = [[int(y) for y in x.split()] for x in lines]


def is_safe(report):
    # print(report)
    is_inc = True
    is_dec = True
    safe = True
    last_num = int(report[0])
    for num in report[1:]:
        num = int(num)
        # print("last_num : ", last_num)
        # print("num :      ", num)
        abs_diff = abs(num-last_num)
        if abs_diff > 3 or abs_diff < 1:
            safe = False


        if num > last_num and is_dec:
            is_dec = False

        if num < last_num and is_inc:
            is_inc = False


        last_num = num
        # print("is_inc: ", is_inc)
        # print("is_dec: ", is_dec)
        # print("--- ---")
    # print(safe and (is_inc or is_dec))
    return safe and (is_inc or is_dec)


# is_safe(lines[0].split())


def is_safe_with_damp(report):
    res = [is_safe(report)]
    print("report: " , report)
    # print("report: ", report)
    for i in range(len(report)):
        damp_report = report[:i] + report[i+1:]
        res.append(is_safe(damp_report))
    # print(res)
    return True in res
# is_safe_with_damp(lines[3].split())
# is_safe_with_damp(lines[4].split())


# my_test = [16, 18, 20, 22, 23,22]
# # print(is_safe(my_test))
# print(is_safe_with_damp(my_test))



# some_test = lines[3]
#
# print(some_test)

#
total_safe = 0
total_damp_safe = 0
for line in lines:
    safe = is_safe(line)
    safe_with_damp = is_safe_with_damp(line)

    if safe:
        total_safe += 1
    if safe_with_damp:
        total_damp_safe += 1
    if safe and not safe_with_damp:
        print("oops")
    if not safe_with_damp and not safe:
        print("---")
        print(line)

print(total_safe)
print(total_damp_safe)

