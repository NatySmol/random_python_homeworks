import sys
for line in sys.stdin:
    list = []
    radek = line.split()
    system = int(radek[0])
    num = int(radek[1])
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W","X",\
           "Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y","z"]

    zaporne = num < 0
    num = abs(num)

    if num == 0:
        list.append(num)
    if system > 10:
        x = {i + 10: abc[i] for i in range(system - 10)}

    while num > 0:
        list.append(num % system)
        num = num // system

    if system > 10:
        for j in range(len(list)):
            if list[j] >= 10:
                list[j] = x[list[j]]
    if zaporne:
        list.append("-")
    print("".join(reversed([str(k) for k in list])))















