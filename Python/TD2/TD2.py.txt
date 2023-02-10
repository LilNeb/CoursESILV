import math

pathToTableau = "./TD2/tab.dat"


#Exo1
dataRaw = [open(pathToTableau).read().split('\n')]
data = [dataRaw[0]]
print(data)
print("\n" + "------------------")

#Exo2

pathToReals = "./TD2/reals.dat"
pathToRoundedReals = "./TD2/RoundedReals.dat"

realsRaw = [open(pathToReals).read().split('\n')]
reals = []

for i in range(len(realsRaw[0])):
    reals.append(round(float(realsRaw[0][i])))

roundedReals = open(pathToRoundedReals, "w")
for i in range(len(reals)):
    roundedReals.write(str(reals[i]) + "\n")
roundedReals.close()

#Exo3
semestre2 = {"Janvier": 31, "Fevrier": 28, "Mars": 31, "Avril": 30, "Mai": 31, "Juin": 30}


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def switchFebDays(year):
    if isLeapYear(year):
        semestre2["Fevrier"] = 29
    else:
        print("Pas bissextile")
        semestre2["Fevrier"] = 28


semestre1 = {"Septembre": 26, "Octobre": 31, "Novembre": 30, "Decembre": 31, "Janvier": 31, "Fevrier": 28}
anneeScolaire = {**semestre1, **semestre2}

#Nb jours de vacances scolaire par mois
vacances = {"Janvier": 0, "Fevrier": 0, "Mars": 0, "Avril": 0, "Mai": 0, "Juin": 0, "Septembre": 0, "Octobre": 0, "Novembre": 0, "Decembre": 0}

class CompteBancaire:
    cb_count = 0
    def __init__(self, nom, iban, solde =0):
        self.nom = nom
        self.solde = solde
        self.iban = iban
        CompteBancaire.cb_count += 1

    def Affichage(self):
        print("Appartenant à : " + self.nom + " Solde : " + str(self.solde) + " IBAN : " + self.iban)
    def __eq__(self, autrecompte):
        return self.solde == autrecompte.iban
    def __str__(self):
        return f"Compte appartenant à {self.nom} avec un solde de {self.solde} et un IBAN : {self.iban}"
   



 


# %% zone du main
if __name__ == '__main__' :
#TD2

    #Exo3
    print("Liste des mois : " + str(list(semestre2.keys())))
    print("Liste des jours : " + str(list(semestre2.values())))

    switchFebDays(2020)
    print("Fevrier : " + str(semestre2["Fevrier"]))
    switchFebDays(2023)
    print("Fevrier : " + str(semestre2["Fevrier"]))
    print(anneeScolaire)

    c1=CompteBancaire("Jean", "FR123456789", 100)
    c2=CompteBancaire("Paul", "FR987654321", 100000000)
    c3=CompteBancaire("Jacques", "FR123456789", 200)
    c1.Affichage()
    print(c2)
    print(c1==c2)
    print(c1==c3)
    c1.cb_count
    c2.cb_count
    c3.cb_count
    CompteBancaire.cb_count

