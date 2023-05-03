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
        di[w] = di.get(w, 0) + 1
print(di)

x = di.items()
print(x)
# ou
y = sorted(di.items())
print(y)
# ou
tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

print("Flipped: ", tmp)

tmp = sorted(tmp)
print("Sorted: ", tmp)

tmp = sorted(tmp, reverse=True)
print("Reverse: ", tmp)


