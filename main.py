# Un tableau comporte 100 valeurs déterminé aléatoirement (soit 0, soit 1), nous allons ensuite déterminé le nombre de 1 présent 6 fois d'affilé dans le tableau. Nous allons réalisez ces opérations x fois. Puis nous déterminerons la probabilité d'avoir 6 fois d'affilé 1

import random

print('********* INITIALISATION *********')

def countGroupOfSix(sumIfOne):
    monTableau = []
    for i in range(100):
        monTableau.append(random.randint(0, 1))

    groupOfSix = 0

    j = 0
    while j < len(monTableau):
        nbSix = 0
        if (monTableau[j] == 1):
            nbSix += 1

            counter = 1
            while nbSix != 6 or counter != 6:
                if j+counter < len(monTableau):
                    if monTableau[j+counter] == 1:
                        nbSix += 1
                    if (monTableau[j+counter] == 0):
                        break
                    counter += 1
                else:
                    break
            if nbSix == 6:
                groupOfSix += 1
                j += 5
        j += 1
    return (sumIfOne+groupOfSix)


nbLoop = 10000
k = 0
sumIfOne = 0
while k < nbLoop:
    sumIfOne = countGroupOfSix(sumIfOne)
    k += 1
proba = sumIfOne / nbLoop
print(proba)