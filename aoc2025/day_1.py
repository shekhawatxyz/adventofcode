import math

# input_list = ["L68", "R51"]
input_list = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99"]
# input_list = ["L68"]
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     input_list.append(line)
# print(contents)
print(input_list)
converted_input = 0
dial = 50
c = 0
for input_dir in input_list:
    print(input_dir)
    print(f"dial is at {dial}")
    if input_dir[0] == "R":
        dial = (dial + int(input_dir[1:])) % 100
        print(f"dial is now at {dial}")

    elif input_dir[0] == "L":
        dial = (dial - int(input_dir[1:])) % 100
        print(f"dial is now at {dial}")
    dial = dial
    #    if converted_input >=0:
    if dial == 0 or abs(dial) % 100 == 0:
        c += 1
        dial = 0
    print(f"crossed 0 {c} times, now at {dial}")
