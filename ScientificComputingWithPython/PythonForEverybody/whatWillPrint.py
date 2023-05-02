# width = 15
# height = 12.0
# print (height/3)


# smallest = None
# print("Before: ", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop: ", itervar, smallest)
# print("Smallest: ", smallest)

# print("0 == 0.0: ", 0 == 0.0)
# print("0 is 0.0: ", 0 is 0.0)
# print("0 is not 0.0: ", 0 is not 0.0)
# print("0 = 0.0: ", 0 = 0.0) #dá erro aqui

# Abrir e ler as linhas do arquivo.
# x1file = open('file.txt')
# print(x1file)
# for line in x1file:
#     print(line)
# x1file.close()
# print("-------------------")

# x2file = open('file.txt')
# ler_x = x2file.read()
# print(ler_x)
# print("len do arquivo:", len(ler_x))
# # funcionou de primeira, mas este código é substituído pela função read()
# x2file.close()
# print("-------------------")

# x3file = open('file.txt')
# print(x3file)
# for line in x3file:
#     if line.startswith('Aqui'):
#         print(line)
# x3file.close()

# Abrir e ler as linhas do arquivo, sem espaços
# x4file = open('file.txt')
# print("***Abrir arquivo, ler linha a linha no loop, e usar strip()  para matar backslash N:")
# for line in x4file:
#     print(line.strip())
# x4file.close()
# print("-------------------")

# Abrir arquivo em uma diferente localização
# print("Abrir arquivo em diferente localização...", "\n")
# f = open("/Users/leticiadegaranhani/freeCodeCamp/ScientificComputingWithPython/fileTeste.txt", "r")
# print(f.read())
# f.close()
# print("-------------------")

# Exemplo de abertura de arquivo, dado o nome do arquivo, buscando x ocorrências de "Subject:" em linhas
# fname = input("Enter the file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened:", fname)
#     quit()
# # quit serve para o programa terminar naquele ponto caso não encontre o arquivo, para não dar erro no resto da execução.
# count = 0
# for line in fhand:
#     if line .startswith('Subject:'):
#         count = count + 1
# print("There were", count, "subject lines in", fname)
print("-------------------")

# outro exemplo
# words = 'His e-mail is q-latr@freecodecamp.org'
# pieces = words.split()
# print("pieces: ", pieces)
# parts = pieces[3].split('-')
# print("parts:", parts)
# n = parts[1]
# print(n)

# print("-------------------")
# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# print(dict)
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9
# print(dict, '\n')
#
# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts)
# print(counts.get('kris', 0))
# print('len(counts):',len(counts))
# print(counts.get('mrugesh', 0))

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# Lê o arquivo, separa as palavras de cada linha, insere em um dicionário e contabiliza as ocorrência de cada palavra
handle = open('/Users/leticiadegaranhani/freeCodeCamp/ScientificComputingWithPython/PythonForEverybody/ex_07_01/mbox-short.txt')
counts = dict()
for line in handle:
    words = line.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# print("words : ", words)
print("counts : ", counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('bigword: ', bigword, ' e bigcount:', bigcount)