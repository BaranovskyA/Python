import os

path = input("Input directory: ")
result = ''
search = 'TODO'

for i in os.walk(path):
    for file in i[2]:
        try:
            file_path = f'{i[0]}\\{file}'
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension == '.c' or file_extension == '.cpp' or file_extension == '.js' or file_extension == '.cls' or file_extension == '.vbp' or file_extension == '.py':
                with open(file_path) as f:
                    for i, line in enumerate(f):
                        if search in line:
                            result += f'[{file_path}]: line {i}, text: {line[line.find(search):]}\n'
        except:
            pass

with open('result.txt', 'w') as f:
    f.write(result)
