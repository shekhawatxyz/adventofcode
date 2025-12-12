# print(c[0:len(str(c))//2])
# print(c[len(str(c))//2:])
import math


# a = "123"
# print(a[1:])
def check_factors(a):
    return None


def check_repetition(a):
    a = str(a)
    print(len(a))
    if len(a) % 2 == 0:
        for i in range((len(a) // 2) + 1):
            first = a[0:i]
            second = a[i : i + i]
            # print(i)
            print(f"first: {first}, second:{second}")
            # print(second)
            # if first == second:
            if first == second:
                print(f"{first} {second}")
                # return True
    else:
        for i in range(math.floor(len(a) / 2) + 1):
            first = a[0:i]
            second = a[i + 1 : i + i + 1]
            # if first == second:
            print(f"{first} {second}")
            # return True
    if a[0 : len(a) // 2] == a[len(a) // 2 :]:
        return True
    return False


print(check_repetition(12121212))

total = 0
count = 0
# ranges = "990244-1009337,5518069-5608946,34273134-34397466,3636295061-3636388848,8613701-8663602,573252-688417,472288-533253,960590-988421,7373678538-7373794411,178-266,63577667-63679502,70-132,487-1146,666631751-666711926,5896-10827,30288-52204,21847924-21889141,69684057-69706531,97142181-97271487,538561-555085,286637-467444,93452333-93519874,69247-119122,8955190262-8955353747,883317-948391,8282803943-8282844514,214125-236989,2518-4693,586540593-586645823,137643-211684,33-47,16210-28409,748488-837584,1381-2281,1-19"
# ranges = "11-22 95-115 998-1012 1188511880-1188511890 222220-222224 1698522-1698528 446443-446449 38593856-38593862"
# ranges = "11-22"
# ranges = ranges.split()
# print(ranges)
# ranges_copy = ranges.copy()
#
# for r in ranges_copy:
#     new_r = r.split("-")
#     # print(new_r)
#     for c in range(int(new_r[0]), int(new_r[1]) + 1):
#         if check_repetition(c):
#             print(c)
#             count += 1
#             total += c
#
# print(total)
# print(count)
