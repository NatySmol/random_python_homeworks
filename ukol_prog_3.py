from fractions import Fraction

koeficienty1 = []
exponenty1 = []
koeficienty2 = []
exponenty2 = []

try:
    operace = input()
    while True:
        line = input()
        vstup = line.split()
        vstup = [int(x) for x in vstup]

        if vstup[0] == (-1) and vstup[1] == (-1):
            break
        else:
            exponenty1.append(int(vstup[0]))
            koeficienty1.append(int(vstup[1]))
    while True:
        line = input()
        vstup = line.split()
        vstup = [int(x) for x in vstup]

        if vstup[0] == (-1) and vstup[1] == (-1):
            break
        else:
            exponenty2.append(int(vstup[0]))
            koeficienty2.append(int(vstup[1]))

except IndexError:
    pass


def add(exponenty1, koeficienty1, exponenty2, koeficienty2):
    exponenty = []
    koeficienty = []
    x = 0
    y = 0
    while x < len(exponenty1) and y < len(exponenty2):
        if exponenty1[x] >= exponenty2[y]:
            if exponenty1[x] == exponenty2[y]:
                exponenty.append(exponenty1[x])
                koeficienty.append(koeficienty1[x] + koeficienty2[y])
                x += 1
                y += 1
            else:
                exponenty.append(exponenty1[x])
                koeficienty.append(koeficienty1[x])
                x += 1
        else:
            exponenty.append(exponenty2[y])
            koeficienty.append(koeficienty2[y])
            y += 1
    while x < len(exponenty1):
        exponenty.append(exponenty1[x])
        koeficienty.append(koeficienty1[x])
        x += 1
    while y < len(exponenty2):
        exponenty.append(exponenty2[y])
        koeficienty.append(koeficienty2[y])
        y += 1

    return exponenty, koeficienty

def mul(exponenty1, koeficienty1, exponenty2, koeficienty2):
    exponenty = []
    koeficienty = []
    exponenty_vysl = []
    koeficienty_vysl = []
    for i in range(len(exponenty1)):
        for j in range(len(exponenty2)):
            exponenty.append(exponenty1[i] + exponenty2[j])
            koeficienty.append(koeficienty1[i] * koeficienty2[j])
    for i in range(len(exponenty) - 1):
        if exponenty[i] not in exponenty[i + 1:] and exponenty[i] != -1:
            exponenty_vysl.append(exponenty[i])
            koeficienty_vysl.append(koeficienty[i])
        elif exponenty[i] in exponenty[i + 1:] and exponenty[i] != -1:
            exponenty_vysl.append(exponenty[i])
            koeficienty_vysl.append(koeficienty[i])
            for j in range(i + 1, len(exponenty)):
                if exponenty[i] == exponenty[j]:
                    koeficienty_vysl[-1] += koeficienty[j]
                    exponenty[j] = -1
    if exponenty[-1] != -1:
        exponenty_vysl.append(exponenty[-1])
        koeficienty_vysl.append(koeficienty[-1])

    j = False
    while not j:
        j = True
        for i in range(len(exponenty_vysl) - 1):
            if exponenty_vysl[i] < exponenty_vysl[i + 1]:
                exponenty_vysl[i], exponenty_vysl[i + 1] = exponenty_vysl[i + 1], exponenty_vysl[i]
                koeficienty_vysl[i], koeficienty_vysl[i + 1] = koeficienty_vysl[i + 1], koeficienty_vysl[i]
                j = False
    i = 0
    while i < len(koeficienty_vysl):
        if koeficienty_vysl[i] == 0:
            koeficienty_vysl.pop(i)
            exponenty_vysl.pop(i)
        else:
            i += 1
    return exponenty_vysl, koeficienty_vysl



def div(exponenty1, koeficienty1, exponenty2, koeficienty2):
    exponenty = []
    koeficienty = []
    zbytek_e = []
    zbytek_k = []
    while exponenty1[0] >= exponenty2[0]:
        mezivysledek_e = []
        mezivysledek_k = []
        exponenty.append(exponenty1[0] - exponenty2[0])
        koeficienty.append(Fraction(koeficienty1[0], koeficienty2[0]))
        for i in range(len(exponenty2)):
            mezivysledek_e.append(exponenty[-1] + exponenty2[i])
            mezivysledek_k.append((-1) * koeficienty[-1] * koeficienty2[i])
        exponenty1, koeficienty1 = add(exponenty1, koeficienty1, mezivysledek_e, mezivysledek_k)
        i = 0
        while i < len(koeficienty1):
            if koeficienty1[i] == 0:
                koeficienty1.pop(i)
                exponenty1.pop(i)
            else:
                i += 1
    return exponenty, koeficienty, exponenty1, koeficienty1




if operace == "add":
    if add(exponenty1, koeficienty1, exponenty2, koeficienty2) == []:
        print("-1 -1")
    else:
        exponenty, koeficienty = add(exponenty1, koeficienty1, exponenty2, koeficienty2)
        for i in range(len(exponenty)):
            print(exponenty[i], koeficienty[i])
        print("-1 -1")

elif operace == "mul":
    if mul(exponenty1, koeficienty1, exponenty2, koeficienty2) == []:
        print("-1 -1")
    else:
        exponenty, koeficienty = mul(exponenty1, koeficienty1, exponenty2, koeficienty2)
        for i in range(len(exponenty)):
            print(exponenty[i], koeficienty[i])
        print("-1 -1")

elif operace == "div":
    exponenty, koeficienty, zbytek_e, zbytek_k = div(exponenty1, koeficienty1, exponenty2, koeficienty2)
    for i in range(len(exponenty)):
        print(exponenty[i], koeficienty[i])
    print("-1 -1")
    for i in range(len(zbytek_e)):
        print(zbytek_e[i], zbytek_k[i])
    print("-1 -1")