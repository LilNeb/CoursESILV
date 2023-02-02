import math

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
def Exo5(liste, debut=0, fin=None):
    if fin is None:
        fin = len(liste) - 1
    max_val = liste[debut]
    for i in range(debut + 1, fin + 1):
        if liste[i] > max_val:
            max_val = liste[i]
    return max_val


#ez way avec la fonction max()

# def Exo5(liste, debut=0, fin=None):
#     if fin is None:
#         fin = len(liste) 
#     return max(liste[debut:fin])


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