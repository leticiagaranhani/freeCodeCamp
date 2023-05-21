split_list = []
list = []

for _ in range(20):
    string = input('Enter your arithmetic problem: ')
    if string != '':
        if string.find('*') != -1 or string.find('/') != -1:
            print("Error: Operator must be '+' or '-'.")
        else:
            if len(split_list) == 5:
                print("Error: Too many problems.")
                break
            else:
                list.append(string)
                split_list.append(string.split())
                for i in split_list:
                    # verificar se posição 0 e 2, da cada item do split_list é digito
                    if i[0].isdigit() is False or i[2].isdigit() is False:
                        print("Error: Numbers must only contain digits.")
                        split_list.pop()
                        list.pop()
                    if len(i[0]) > 4 or len(i[2]) > 4:
                        print("Error: Numbers cannot be more than four digits.")
                        split_list.pop()
                        list.pop()
    else:
        break

print("split_list = ", split_list)
print("list = ", list)

line1 = []
line2 = []
line_dashes = []
line_result = []

for item in split_list:
    len_oper1 = len(item[0])
    len_oper2 = len(item[2])
    if len(item[0]) >= len(item[2]):
        len_max_item = len(item[0])
        line1.append('  ' + item[0] + '    ')
        line2.append(item[1] + ' ' + ((len(item[0])-len(item[2])) * ' ') + item[2] + '    ')
    else:
        len_max_item = len(item[2])
        line1.append('  ' + ((len(item[2])-len(item[0])) * ' ') + item[0] + '    ')
        line2.append(item[1] + ' ' + item[2] + '    ')
    # print("len_max_item = ", len_max_item)
    # construir line_result
    if item[1] == '+':
        result = int(item[0]) + int(item[2])
    else:
        result = int(item[0]) - int(item[2])
    str_result = str(result)
    line_result.append(((len_max_item + 2 - len(str_result)) * ' ') + str_result + '    ')

    # para imprimir dashes, é sempre len_max_item+2'-'.
    dashes = '--'
    for a in range(len_max_item):
        dashes = dashes + '-'
    line_dashes.append(dashes + '    ')


# operador é sempre na posição 0 do array line2
# se o len_max_item for o 1o. operando, concatenar 2 espaços à frente e dar append no array line1
#                                       concatenar operador+1+espaço+(len(item[0])-len(item[2]))espaços+operando2, e dar append no array line2
# se o len_max_item for o 2o. operando, concatenar operador+espaço+operando2 e dar append no array line2
#                                       concatenar 2 espaços+(len(item[2])-len(item[0]))espaços+operando1 e dar append no array line1

print("len(split_list) = ", len(split_list))
print('\n')
print("line1: ", line1)
print("line2: ", line2)
print("line_dashes: ", line_dashes)
print("line_result: ", line_result)
# forma correta de impressão para este exercício
print('\n')
print(*line1)
print(*line2)
print(*line_dashes)
# no caso do 2o. paramentro ser True, imprime esta linha
print(*line_result)


# try:  # para refatorar
#     str.isdigit()
# except ValueError:
#     print("Error: Numbers must only contain digits.")
