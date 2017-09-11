
from pig import piggy


def read_file(file_path):

    with open(file_path, 'r') as file:
        # contents = file.readlines()
        return file.readlines()
    #         print(line)
    # print(contents)

def write_file(file_path, new_lines):
    with open(file_path, 'w+') as file:
        for line in new_lines:
            file.write(line + '\n')

def append_to_file(file_path):
    with open(file_path, 'a') as file:
        times = int(input('how many'))
        ran = 0
        list_of_lines = []
        while ran < times:
            list_of_lines.append(input('what word: '))
            ran += 1
        for line in list_of_lines:
            file.write(line + '\n')


def trans_pig(origin_file, dest_file):
    origin_lines_list = read_file(origin_file)
    dest_file_lines = []
    for line in origin_lines_list:
        new_line = []
        for word in line.split():
            new_line.append(piggy(word))
        dest_file_lines.append(' '.join(new_line))
    print(dest_file)
    write_file(dest_file, dest_file_lines)

origin_file = 'sample.txt'
new_file = 'trans_to_pig.txt'

trans_pig('sample.txt', new_file)
# write_file('sample.txt')
# read_file('sample.txt')
for line in read_file(new_file):
    print(line)
