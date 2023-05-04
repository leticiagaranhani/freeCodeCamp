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
# handle = open('/Users/leticiadegaranhani/freeCodeCamp/ScientificComputingWithPython/PythonForEverybody/ex_07_01/mbox-short.txt')
# counts = dict()
# for line in handle:
#     words = line.lower().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# # print("words : ", words)
# print("counts : ", counts)
#
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print('bigword: ', bigword, ' e bigcount:', bigcount)

# # formas de ordenar/reordenar dicionários pelos valores
# fhand = open('ex_09/intro.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
#
# for val, key in lst[:10]:
#     print(key, val)
#
#
# # formas MAIS CURTA de ordenar/reordenar dicionários pelos valores
# c = {'a':10, 'b':1, 'c':22}
# print('\n',sorted ( [(v, k) for k,v in c.items() ]))
# print('\n',sorted ( [(v, k) for k,v in c.items() ], reverse=True))

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)
#
# x = 'My 2 favorite numbers are 19 and 42. E agora talvez insira um A. Testando $esd2as5. E também um us365ABBEC.'
# # o "+" abaixo exibe os caracteres numericos unidos, como exibidos na string
# y = re.findall('[0-9]+', x)
# print("y:",y)
# #  retirando o "+", são exibidos individualmente
# y = re.findall('[0-9]', x)
# print("y:",y)
# y = re.findall('[AEIOU]+', x)
# print("y:",y)
#
# # abaixo exibe repetição de caracteres "não em branco" após encontrar "@"
# lin = 'From stephen.marquar@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('@([^ ]*)', lin)
# print('\n y =', y)
#
# # iniciando do começo da linha (^), procurando por 'From', exibe repetição de caracteres "não em branco" após encontrar "@"
# y = re.findall('^From .*@([^ ]*)', lin)
# print('\n y =', y)
#
# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+', x)
# print('\n y =', y)

# this one did not work
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# # this worked, and you will write a web browser in 10 lines
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='' )
# mysock.close()

# The ord() function tells us the num eric value os a simple ASCII character
# print(ord('H'))
# print(ord('e'))
# print(ord('\n'))
# print(ord(' '))
# print(ord('A'))
# print(ord('a'))
# print(ord('A')-ord('a'))
# print(ord('B')-ord('b'))

# You will write a web browser in 4 lines
# urllib faz o trabalho do socket, apresentando a página web como um arquivo.
# import urllib.request, urllib.parse, urllib.error
#
# # fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# usando BeautifulSoup pela primeira vez, para web scrapping
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))