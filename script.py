from typing import TextIO

def ADVNEWLINE(file: TextIO) -> list[str]:
    return [x for x in file.readline().strip().split(' ')]

with open('./diag.txt', 'r') as file:
    line = ADVNEWLINE(file)
    while line[0] != '':
        while line[0] == '#':
            line = ADVNEWLINE(file)
        print(f'{line[1]}, {line[2]} / {line[4]}', end='')
        if (line[0] != line[3]):
            print(f' ({line[3]})', end='')
        print()
        line = ADVNEWLINE(file)