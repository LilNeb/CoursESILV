import math
import time

def Exo0():
    print("voila mon Exo de bienvenue")

def Exo1():
    print("Exo1")
    temps=6.892
    distance=19.7 
    vitesse=distance/temps;
    #vitesse =round (vitesse,2) #je n'ai pas formatter le pri
    print("vitesse=", vitesse)
    print(f"vitesse = {vitesse: .2f}")



def Exo2a(n1, n2):
    if(n1>n2):
        print(n1)
    else:
        print(n2)  

def Exo2b(n1,n2):
    if(n1>n2):
        print(n1)
    print(n2)

def Exo2c(n1, n2):
    print(n1 if n1 > n2 else n2)


def Exo3(x1 = None, x2 = None, x3 = None):
    if x1 == None:
        return None
    if x2 == None:
        return (x1*x1*x1)
    if x3 == None:
        return(x1*x1*x2)
    if x3:
        return(x1*x2*x3)



#Passe dans tous les index en vérifiant si la valeur est plus grande que la valeur max
def Exo4(liste, debut=0, fin=None):
    if fin is None:
        fin = len(liste) - 1
    max_val = liste[debut]
    for i in range(debut, fin + 1):
        if liste[i] > max_val:
            max_val = liste[i]
    return max_val


#Exo4 ez way avec la fonction max()

# def Exo4(liste, debut=0, fin=None):
#     if fin is None:
#         fin = len(liste) 
#     return max(liste[debut:fin])

#Exo5
def Exo5(l1 =[], l2 =[]):
    len1 = len(l1)
    len2 = len(l2)
    t3 = []
    if len1 != len2:
        return None
    if not l1 or not l2:
        if l1 == l2:
            return []
        else :
            if not l1:
                return l2
            else:
                return l1
    else:
        t3 = [0] * len1
        for i in range(len1):
            t3[i] = str(l2[i]) + str(l1[i])
        return t3



#Exo6 ez way avec la fonction str[::-1]
# def Exo6(str):
#     return str[::-1]

#Exo6
def Exo6(str):
    len1 = len(str)
    str2 = ""
    for i in range(len1):
        str2 += str[len1 - i - 1]
    return str2

#Exo7

def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


#Exo7 ez way avec la fonction sort()
# def mafonction(arr):
#     arr.sort()

#Exo7 ez way avec la fonction sorted()
# def mafonction(arr):
#     arr = sorted(arr)

#Exo8 : display the countdown from start to 1 included, then "GO!"
def Exo8(start):
    for i in range(start, 0, -1):
        print(i)
        time.sleep(1)
    print("GO!")

#Exo9() : IsPalindrome
def Exo9(str):
    len1 = len(str)
    for i in range(len1):
        if str[i] != str[len1 - i - 1]:
            return False
    return True

#Exo9 ez way avec la fonction str[::-1]
# def Exo9(str):
#     return str == str[::-1]

#Exo10 : weird array manipulations
def Exo10(arr,n = 1):
    if n == 1:
        return (arr+arr[::-1])
    if n == 2:
        arr[0], arr[1], arr[2] = arr[0], arr[0], arr[0]
        return arr
    if n == 3: #l2 is only composed of elements with index multiple of 3
        l2 = []
        for i in range(len(arr)):
            if i % 3 == 0:
                l2.append(arr[i])
        return l2

#Exo10 ez way avec la fonction str[::-1]
# def Exo10(arr,n = 1):
#     if n == 1:
#         return (arr+arr[::-1])
#     if n == 2:
#         arr[0], arr[1], arr[2] = arr[0], arr[0], arr[0]
#         return arr
#     if n == 3: #l2 is only composed of elements with index multiple of 3
#         return arr[::3]

#Exo11 : EstPaire
def Exo11():
    x = int(input("Entrez un nombre entier : "))
    if x % 2 == 0:
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")

#Exo12 : Acronym
def Exo12():    
    phrase = input("Entrez une phrase : ")
    phrase = phrase.upper()
    phrase = phrase.split()
    acronym = ""
    for i in range(len(phrase)):
        acronym += phrase[i][0]
    print(acronym)

#Exo13 : count c iterations
def Exo13():
    c = input("Entrez un caractère : ")
    phrase = input("Entrez une phrase : ")
    count = 0
    for i in range(len(phrase)):
        if phrase[i] == c:
            count += 1
    print("'c' apparaît  ",count, " fois dans ", phrase) 

#Exo14 : vowel count
def Exo14(phrase):
    count = 0
    for i in range(len(phrase)):
        if phrase[i] in "aeiouy":
            count += 1
    return count

#Exo15 : dictionnary
def Exo15():
    print(dico)
    c = input("Entrez un mot : ")
    if c in dico:
        print(dico[c])
    else:
        print("Le mot n'est pas une clé du dictionnaire")

#Exo16 : key in dict print value
def Exo16():
    print(dico)
    c = input("Entrez une clé : ")
    if c in dico:
        print(dico[c])
    else:
        print("Le mot n'est pas une clé de ", dico)

#Exo17 : dict mods
def Exo17():    
    dico["hello"] = "world"
    print(dico)
    dico["nombre"] = 0
    del dico["pi"]

#Exo18 : set creation
def Exo18():
    s1 = {1,2,3}
    s2 = set()
    s2.add("hello")
    s2.add("world")
    s3 = {10,20,30,40,10,2,40}
    s4 = set(range(5,16))








# %% zone du main
if __name__ == '__main__' :
#Exo0()
    Exo1()

    Exo2a(7,0)
    Exo2b(0,7)
    Exo2b(3,7)
    print(Exo3())
    print(Exo3(2))
    print(Exo3(2,4))
    print(Exo3(2,5,8))

    serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print(Exo4(serie))
    print(Exo4(serie, 2, 5))
    print(Exo4(serie, 2))
    print(Exo4(serie, fin=3, debut=1))

    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
    'Décembre']
    print(Exo5(t1,t2))

    print(Exo6("zorglub"))

    print(mafonction(arr = [64, 34, 25, 12, 22, 11, 90]))
    #C'est une fonction de tri à bulle

    #Exo8(3)

    Exo9("kayak")

    print(Exo10([0, 1, 2, 3, 4], 1))
    print(Exo10([0, 1, 2, 3, 4], 2))
    print(Exo10([0, 1, 2, 3, 4], 3))

    #Exo11()
    #Exo12()
    #Exo13()
    print(Exo14("Bonjour"))

    dico = {}
    dico["pi"] = 3.141592653589793
    dico["mot"] = "mot"
    dico["nombre"] = 42
    dico["liste"] = [1, 2, 3]
    #Exo15()

    





    