print("PY4E - Exercise 9")

fname = input("Enter File:")
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:

        # pega o valor da chave e retorna o default, se não o encontrar
        # print('**', w, di.get(w, 'Ø'))
        # if w in di:
        #     di[w] = di[w] + 1
        #     print('**Existing**')
        # else:
        #     di[w] = 1
        #     print('**NEW**')

        # retrieve/creat/update the word counter, in just one line
        di[w] = di.get(w, 0) + 1
        # print(w, di[w])
print(di)

# mostrar a palavra mais comum
largest = -1
theword = None
for k,v in di.items():
    print(k, v)
    if v > largest:
        largest = v
        theword = k
print("Largest word: ", theword, largest)