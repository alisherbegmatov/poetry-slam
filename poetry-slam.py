import random

#get_file_lines: Takes in a file name and returns the lines of the file as a list of strings.
def get_file_lines(filename):

    file_lines = open(filename, 'r')
    lines_list = file_lines.readlines()
    return lines_list

#lines_printed_backworlds: Takes in a list of strings containing lines of the poem and prints them out backwards with line numbers.
def lines_printed_backwards(lines_list):

    num_list = range(len(lines_list))
    num_list = list(num_list)
    for num in reversed(num_list):
        print(f"{num_list[num]} {lines_list[num]}")

#lines_printed_random: Takes in a list of strings containing lines of the poem and prints them out in random order.
def lines_printed_random(lines_list):

    num_list = range(len(lines_list))
    num_list = list(num_list)
    for i in num_list:
        num = random.randrange(26)
        print(lines_list[num])

#lines_printed_custom: A function which takes in a list of strings containing lines of the poem and prints them out in some unique way. ( takes one line from top and bottom until reaches the end of poem )
def lines_printed_custom(lines_list):

    nl = '/n'
    for x in range(int(len(lines_list)/2)):
        print(f"{x+1} {lines_list[x]}")
        print(f"{len(lines_list) - x} {lines_list[len(lines_list) - x - 1]} {nl}")

p_list = get_file_lines("poem.txt")

lines_printed_backwards(p_list)
lines_printed_random(p_list)
lines_printed_custom(p_list)
