import os

files = os.listdir()
# make homework to end
for f in files:
    try:
        with open(f, 'rt') as file:
            for index, line in enumerate(file):
                if line[0] == '#' or line[0] == '//':
                    print(f'{os.getcwd()}\{f} -> {index} : {line}')
    except:
        print(f'Не удалось прочесть файл {f}')
#
