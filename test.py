import random


# etudiant = {
#     "nom": "fatima",
#     "age": 24,
#     "ville": "Paris"
# }


# print(etudiant["ville"])

# list=[11,10,9]
# for nomber in list :
#     print(nomber)


# def addition():
#     print(a+b)
#     return a+b
# sum =addition(1,3)



# def addition():
#     valeur1 = random.randint(0, 100)  
#     valeur2 = random.randint(0, 100)  
#     somme = valeur1 + valeur2
#     return somme
    

# resultat = addition()
# print(resultat)





# def addition():
#     valeurs = [10, 20, 30, 40, 50]  
#     valeur1 = random.choice(valeurs)  
#     valeur2 = random.choice(valeurs)  

#     return {"v1":valeur1,
#             "v2":valeur2,
#             "res":valeur1+valeur2
            
#             }
# print(addition())

# #     somme = valeur1 + valeur2
# #     return somme

# # resultat = addition()
# # print( resultat)



def aleatoire(boolen,liste,min,max) :
    if boolen == True :
        res =  random.choice(liste)
        return res

    else: 
        res = random.randint(min,max)
        return res;


liste=[1,20,30]
resultat =aleatoire(False,liste,1,8)

print(resultat)
