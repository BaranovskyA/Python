import re

pattern = '(([\da-zA-Z])([_\w-]{,61})\.)(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.(([a-zA-Z\d]+)|([a-zA-Z\d])))'
string = input('String: ')

domains = []
check = 1

while check != 0:
    try:
        start, end = re.search(pattern, string).span()
        domains.append(string[start:end])
        string = string.replace(string[start:end], ' ')
    except Exception as e:
        break


print(domains)
