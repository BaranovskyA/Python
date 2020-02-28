currencies = [
    {'KZT': {'USD': 0.0026}},
    {'USD': {'KZT': 381.84}}
]


def checkValue():
    try:
        listarg = input().split(' ')
        if len(listarg) == 3:
            val, fcurr, scurr = listarg
            val = float(val)
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
        elif len(listarg) == 4:
            val, fcurr, newVal, scurr = listarg
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
        else:
            print('Ошибка ввода.')
            exit()
    except Exception as e:
        print(e)




checkValue()
