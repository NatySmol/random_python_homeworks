import sys

sys.setrecursionlimit(1000)

# koukni se na https://www.geeksforgeeks.org/expression-tree/
# abys pochopil jak funguje ten strom operaci v postfixu

def par_left(w):  # uzavorkovani nalevo od vlozeneho
    # operatoru v zavislosti na priorite operaci
    p = w.priority
    u = w
    if p > u.left.priority:
        u.value = ')' + u.value
        while u.left != None:
            u = u.left
        u.value = '(' + u.value
    return w


def par_right(w):  # uzavorkovani na pravo od vlozeneho operatoru
    p = w.priority
    u = w
    i = u.value
    if p > u.right.priority:
        u.value += '('
        while u.right != None:
            u = u.right
        u.value += ')'
    elif p == u.right.priority and (u.value[-1] == '/' or u.value[-1] == '-'):
        u.value += '('
        while u.right != None:
            u = u.right
        u.value += ')'
    return w

class Et:

    # node pro tvoreni stromu
    def __init__(self, value):
        self.value = value
        self.priority = priority(self.value)
        self.right = None
        self.left = None



# zjisti zda je prvek vstupu cislo nebo operator
def isOperator(c):
    if (c == '+' or c == '-' or c == '*'
            or c == '/'):
        return True
    else:
        return False

# vytvori prioritu operaci
def priority(g):
    if (g == '+'):
        return 1
    elif (g == '-'):
        return 1
    elif (g == '*'):
        return 2
    elif (g == '/'):
        return 2
    else:
        return 3

# tvori strom v postfixove notaci

def constructTree(postfix):
    stack = []
    postfix = postfix.split(" ") # rozdeli vstup n ajednotliva cisla a znaky
    # Traverse through every character of input expression
    for char in postfix:

        # cislo prida do zasobniku
        if not isOperator(char):
            t = Et(char)
            stack.append(t)

        # kdyz je to znamenko vlozi ho mezi dve cisla a to vlozi
        # zpatky do zasobniku

        else:


            t = Et(char)
            t1 = stack.pop() # vyjme posledni dva nody ze zasobniku
            t2 = stack.pop()

            t.left = t2   # vlozi mezi ne operaci t
            t.right = t1
            par_left(t) # funkce, ktere spravne pridaj zavorky
            par_right(t)

            stack.append(t)

    # vrati koren stromu
    t = stack.pop()

    return t


# vypisuje ten strom, ve kterym je ulozenej vyraz se zavorkama
# rekurzivne

def inorder(t):
    if t is None:
        return

    inorder(t.left)
    print(t.value, end='')
    inorder(t.right)


postfix = input()
r = constructTree(postfix)
inorder(r)

