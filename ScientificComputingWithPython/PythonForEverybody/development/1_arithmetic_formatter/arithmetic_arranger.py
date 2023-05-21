def arithmetic_arranger(x, y=False):
    split_list = []

    if x != '':
        for a in x:
            # print(a)
            if a.find('*') != -1 or a.find('/') != -1:
                return print("Error: Operator must be '+' or '-'.\n")
            else:
                if len(split_list) == 5:
                    return print("Error: Too many problems.\n")
                else:
                    split_list.append(a.split())
                    for i in split_list:
                        if i[0].isdigit() is False or i[2].isdigit() is False:
                            return print("Error: Numbers must only contain digits.\n")
                        if len(i[0]) > 4 or len(i[2]) > 4:
                            return print("Error: Numbers cannot be more than four digits.\n")

    line1 = []
    line2 = []
    line_dashes = []
    line_result = []

    for item in split_list:
        if len(item[0]) >= len(item[2]):
            len_max_item = len(item[0])
            line1.append('  ' + item[0] + '    ')
            line2.append(item[1] + ' ' + ((len(item[0]) - len(item[2])) * ' ') + item[2] + '    ')
        else:
            len_max_item = len(item[2])
            line1.append('  ' + ((len(item[2]) - len(item[0])) * ' ') + item[0] + '    ')
            line2.append(item[1] + ' ' + item[2] + '    ')
        # build line_result
        if item[1] == '+':
            result = int(item[0]) + int(item[2])
        else:
            result = int(item[0]) - int(item[2])
        str_result = str(result)
        line_result.append(((len_max_item + 2 - len(str_result)) * ' ') + str_result + '    ')

        # to print dashes, is len_max_item+2'-'.
        dashes = '--'
        for a in range(len_max_item):
            dashes = dashes + '-'
        line_dashes.append(dashes + '    ')

    if y == True:
        return print('\n'), print(*line1), print(*line2), print(*line_dashes), print(*line_result)
    else:
        return print('\n'), print(*line1), print(*line2), print(*line_dashes)
