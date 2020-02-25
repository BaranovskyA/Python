currencies = [
    {'KZT': {'USD': 0.002}},
    {'USD': {'KZT': 377}}
]


def checkValue():
    try:
        val, fcurr, scurr = input().split(' ')
        val = int(val)
        coef = 0
        checks = 0
        for currency in currencies:
            for check in currency.keys():
                if check == fcurr:
                    checks += 1

        for currency in currencies:
            if checks == 0:
                print('Такой пары валют нет.')
                checkValue()
            else:
                for innerCurren in currency.values():
                    if innerCurren.get(scurr) != None:
                        coef = innerCurren.get(scurr)
        val = val * coef
        print(val)
    except:
        print(
            'Для добавления новой пары введите еще раз в формате "Сумма, валюта суммы, сумма в новой валюте, вторая" Для возврата введите 4 нуля через пробел')
        val, fcurr, newVal, scurr = input().split(' ')
        if int(val) <= 0:
            checkValue()
        innCurr = ''
        for curr in currencies:
            for innerCurr in curr.values():
                innCurr = innerCurr.keys()
            if f"{curr.keys()}" == f"dict_keys(['{fcurr}'])" and f"{innCurr}" == f"dict_keys(['{scurr}'])":
                print("Такая пара уже существует")
                exit()
        newVal = int(newVal)
        currencies.append({fcurr: {scurr: newVal}})
        print('OK')
        checkValue()


checkValue()
