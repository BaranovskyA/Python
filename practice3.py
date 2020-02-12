pull = input()

if(pull[0].isdigit() is True):
    print('Начинается с цифры.')
elif(pull == 'class' or pull == 'def' or pull == 'global' or pull == 'pass' or pull == 'return' or pull == 'except' or pull == 'import'):
    print('Ключевое слово.')
else:
    if(pull[:2] == "__"):
        print('Так называют приватные идентификаторы.')
    elif(pull.isupper()):
        print('Так называют константы.')
    elif(pull[0].isupper()):
        print('Так называют классы.')
